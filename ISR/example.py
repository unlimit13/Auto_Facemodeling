import matplotlib.pyplot as plt
from skimage import exposure
from skimage.exposure import match_histograms
import cv2

sr = cv2.dnn_superres.DnnSuperResImpl_create()

path = "ESPCN_x4.pb"

sr.readModel(path)

sr.setModel("espcn",4)

img = cv2.imread("/mnt/d/Temp/Blender/ffmpeg/Left_c.jpg")
result = sr.upsample(img)
dir="/mnt/d/Temp/Blender/ffmpeg/output/hist_output_right_direct.jpg"
cv2.imwrite(dir,result)
# Resized image

resized = cv2.resize(img,dsize=None,fx=3,fy=3)
plt.figure(figsize=(12,8))
plt.subplot(1,3,1)

# Original image

plt.imshow(img[:,:,::-1])
plt.subplot(1,3,2)

# SR upscaled

plt.imshow(result[:,:,::-1])
plt.subplot(1,3,3)

# OpenCV upscaled
plt.imshow(resized[:,:,::-1])
plt.show()


