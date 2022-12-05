
import cv2


sr = cv2.dnn_superres.DnnSuperResImpl_create()

path = "ESPCN_x4.pb"

sr.readModel(path)

sr.setModel("espcn", 4) # set the model by passing the value and the upsampling ratio
result = sr.upsample("/mnt/d/Temp/Blender/ffmpeg/Right.jpg") # upscale the input image
