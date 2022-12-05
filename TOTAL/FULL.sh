#!/bin/sh

if [ $# = 0 ]
then
    python3 /mnt/d/Temp/Blender/TOTAL/TOTAL.py

elif [ $1 = "no_flat" ]
then
    python3 /mnt/d/Temp/Blender/TOTAL/TOTAL.py $1

fi

/home/unlimit13/blender-3.3.1-linux-x64/blender -b ~/Blender/Empty_Workspace.blend -P /mnt/d/Temp/Blender/scripts/Main.py