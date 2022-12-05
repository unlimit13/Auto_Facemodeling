from PIL import Image, ImageStat
import math
# coordinates 2952*1944

imag = Image.open("./output/hist_output_right.jpg")

#imag = imag.convert('L')

stat = ImageStat.Stat(imag)
R,G,B=stat.rms

#temp_br= stat.rms[0]
temp_br=math.sqrt( 0.299*math.pow(R,2) + 0.587*math.pow(G,2) + 0.114*math.pow(B,2) )

print(temp_br)

"""X, Y = 2500,1900

pixelRGB = imag.getpixel((X, Y))
R, G, B = pixelRGB

brightness = sum([R, G, B]) / 3 
brightness1 = 0.2126*R + 0.7152*G + 0.0722*B 
brightness2 = 0.299*R + 0.587*G + 0.114*B 
brightness3 = math.sqrt( 0.299*math.pow(R,2) + 0.587*math.pow(G,2) + 0.114*math.pow(B,2) ) 

print(brightness)
print(brightness1)
print(brightness2)
print(brightness3)"""