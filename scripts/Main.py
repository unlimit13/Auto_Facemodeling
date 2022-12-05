import os
import time
import bpy

'''left_path = '/mnt/d/Temp/Blender/Left.jpg'
right_path = '/mnt/d/Temp/Blender/Right.jpg'


a=0;

while a<10:
	print(os.path.isfile(left_path))
	print(os.path.isfile(right_path))
	a=a+1
	time.sleep(1)'''
 
for area in bpy.context.screen.areas:
        if area.type == 'TEXT_EDITOR':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'area': area, 'region': region, 'edit_object':bpy.context.edit_object}


bpy.ops.keentools_fb.add_head()
#bpy.context.area.ui_type = 'VIEW_3D'

bpy.ops.keentools_fb.open_multiple_filebrowser_exec()

bpy.context.scene.keentools_fb_settings.heads[0].masks[0] = False
bpy.context.scene.keentools_fb_settings.heads[0].masks[1] = False
bpy.context.scene.keentools_fb_settings.heads[0].masks[4] = False
bpy.context.scene.keentools_fb_settings.heads[0].masks[5] = False
bpy.context.scene.keentools_fb_settings.heads[0].masks[7] = False
bpy.context.scene.keentools_fb_settings.heads[0].tex_uv_shape = 'uv3'
bpy.context.scene.keentools_fb_settings.tex_equalize_brightness = True
bpy.context.scene.keentools_fb_settings.tex_equalize_colour = True

bpy.context.scene.keentools_fb_settings.tex_width = 3840
bpy.context.scene.keentools_fb_settings.tex_height = 2060


#modify fbhead option

#bpy.context.area.ui_type = 'VIEW_3D'

bpy.ops.keentools_fb.pinmode(headnum=0, camnum=0)
bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.keentools_fb.select_current_camera()
#bpy.ops.keentools_fb.select_camera(headnum=0, camnum=0)
bpy.ops.keentools_fb.pickmode_starter(headnum=0, camnum=0)

#align face-1
bpy.ops.keentools_fb.pinmode(headnum=0, camnum=1)
bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.keentools_fb.select_camera(headnum=0, camnum=1)
bpy.ops.keentools_fb.pickmode_starter(headnum=0, camnum=1)

#bpy.ops.keentools_fb.show_solid()
#align face-1


#bpy.ops.keentools_fb.show_solid()

bpy.ops.keentools_fb.bake_tex(headnum=0)
bpy.ops.keentools_fb.tex_selector(headnum=0)
#make face


#bpy.ops.export_scene.obj(filepath='/mnt/d/Temp/Blender/example.obj',use_materials=False)


def context_override():
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        return {'window': window, 'screen': screen, 'area': area, 'region': region, 'scene': bpy.context.scene} 


bpy.data.objects['FBHead'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['FBHead']
bpy.ops.object.mode_set(mode='TEXTURE_PAINT') 
bpy.ops.paint.brush_select(image_tool='SMEAR')

nose_start_y=0
nose_start_x = 600

nose=[]

while nose_start_y<2000:
    nose.append({
    "name": "stiching",
    "location": (0, 0, 0),
    "mouse": (nose_start_x,nose_start_y),
    "mouse_event": (0,0),
    "x_tilt": 0,
    "y_tilt": 0,
    "size": 50,
    "pressure": 100,
    "pen_flip": False,
    "time": 0,
    "is_start": True
    })
    nose_start_y= nose_start_y+5

		
bpy.ops.paint.image_paint(context_override(),stroke=nose)

bpy.ops.export_scene.fbx(filepath='/mnt/d/Temp/Blender/example.fbx', path_mode='COPY', embed_textures=True)