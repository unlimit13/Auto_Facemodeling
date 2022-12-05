from PIL import Image, ImageStat
import math
import os
import sys
# coordinates 2952*1944

import matplotlib.pyplot as plt
from skimage import exposure
from skimage.exposure import match_histograms
import cv2
import numpy as np

if len(sys.argv) ==2:
    image_flatten = sys.argv[1]
else :
    image_flatten = '1'


sr = cv2.dnn_superres.DnnSuperResImpl_create()

path = "ESPCN_x4.pb"

sr.readModel(path)

sr.setModel("espcn",4)

Left_i = cv2.imread('../Left.jpg')
Left_result = sr.upsample(Left_i)
Left_dir='../ISR_Left.jpg' 

Right_i = cv2.imread('../Right.jpg')
Right_result = sr.upsample(Right_i)
Right_dir='../ISR_Right.jpg'

cv2.imwrite(Left_dir,Left_result)
cv2.imwrite(Right_dir,Right_result)

print("---ISR DONE---")

Left_img = cv2.imread('../ISR_Left.jpg')
Right_img = cv2.imread('../ISR_Right.jpg')

if image_flatten=="no_flat":
    cv2.imwrite("../f_Left.jpg", Left_img)
    cv2.imwrite("../f_Right.jpg", Right_img)
    

else :
    #Image flatten

    rows_left, cols_left = Left_img.shape[:2]
    rows_right, cols_right = Right_img.shape[:2]

    print("---image flatten 1---")

    # ---① 설정 값 셋팅
    exp = 0.90       # 볼록, 오목 지수 (오목 : 0.1 ~ 1, 볼록 : 1.1~)
    scale = 1           # 변환 영역 크기 (0 ~ 1)

    # 매핑 배열 생성 ---②
    l_mapy, l_mapx = np.indices((rows_left, cols_left),dtype=np.float32)
    r_mapy, r_mapx = np.indices((rows_right, cols_right),dtype=np.float32)

    # 좌상단 기준좌표에서 -1~1로 정규화된 중심점 기준 좌표로 변경 ---③
    l_mapx = 2*l_mapx/(cols_left-1)-1
    l_mapy = 2*l_mapy/(rows_left-1)-1
    r_mapx = 2*r_mapx/(cols_right-1)-1
    r_mapy = 2*r_mapy/(rows_right-1)-1

    # 직교좌표를 극 좌표로 변환 ---④
    L_r, L_theta = cv2.cartToPolar(l_mapx, l_mapy)
    R_r, R_theta = cv2.cartToPolar(r_mapx, r_mapy)

    # 왜곡 영역만 중심확대/축소 지수 적용 ---⑤
    L_r[L_r< scale] = L_r[L_r<scale] **exp  
    R_r[R_r< scale] = R_r[R_r<scale] **exp  

    # 극 좌표를 직교좌표로 변환 ---⑥
    L_mapx, L_mapy = cv2.polarToCart(L_r, L_theta)
    R_mapx, R_mapy = cv2.polarToCart(R_r, R_theta)

    # 중심점 기준에서 좌상단 기준으로 변경 ---⑦
    L_mapx = ((L_mapx + 1)*cols_left-1)/2
    L_mapy = ((L_mapy + 1)*rows_left-1)/2
    R_mapx = ((R_mapx + 1)*cols_right-1)/2
    R_mapy = ((R_mapy + 1)*rows_right-1)/2

    # 재매핑 변환
    print("---image flatten 2---")
    L_distorted = cv2.remap(Left_img,L_mapx,L_mapy,cv2.INTER_LINEAR)
    R_distorted = cv2.remap(Right_img,R_mapx,R_mapy,cv2.INTER_LINEAR)


    cv2.imwrite("../f_Left.jpg", L_distorted)
    cv2.imwrite("../f_Right.jpg", R_distorted)
    
print("---Image flatten Done---")
# Resized image

Left = Image.open("../f_Left.jpg")
Right = Image.open("../f_Right.jpg")
#imag = imag.convert('L')

stat_l = ImageStat.Stat(Left)
stat_r = ImageStat.Stat(Right)
R1,G1,B1 = stat_l.mean
R2,G2,B2 = stat_r.mean

#temp_br= stat.rms[0]
left_br=math.sqrt( 0.299*math.pow(R1,2) + 0.587*math.pow(G1,2) + 0.114*math.pow(B1,2) )
right_br=math.sqrt( 0.299*math.pow(R2,2) + 0.587*math.pow(G2,2) + 0.114*math.pow(B2,2) )

if(left_br>right_br) : 
    lower = '../f_Right.jpg '
    higher = '../f_Left.jpg'
    gap = left_br-right_br
    gap=str(gap/40)
    os.system('ffmpeg -i '+ lower + ' '+ '-vf eq=brightness=' + gap + ' ../TOTAL_right.jpg' )
    os.system('mv ../TOTAL_right.jpg ./')
    os.rename(higher,'TOTAL_left.jpg')
else:
    lower='../f_Left.jpg '
    higher= '../f_Right.jpg '
    gap = right_br-left_br
    gap=str(gap/40)
    os.system('ffmpeg -i '+ lower + ' '+ '-vf eq=brightness=' + gap + ' ../TOTAL_left.jpg' )
    os.system('mv ../TOTAL_left.jpg ./')
    os.rename(higher,'TOTAL_right.jpg')
    


#os.system('ffmpeg -i '+ lower + ' '+ '-vf eq=brightness=' + gap + ' ../br_' + lower[3:] )
lower = '../br_' + lower[3:]
print("---brightness standardization Done---")
#ffmpeg -i Left.jpg -vf eq=brightness=0.06 OUTPUT.jpg
#br 0.06 = 20.159243397137175 - 6.280247719005359

