import os
import time

left_path = '/mnt/d/Temp/Blender/Left.jpg'
right_path = '/mnt/d/Temp/Blender/Right.jpg'

a=0;

while a<10:
    print(os.path.isfile(left_path))   # False
    print(os.path.isfile(right_path))
    a= a+1
    time.sleep(1)