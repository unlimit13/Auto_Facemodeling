import bpy

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

nose_start_y=1080
nose_start_x = 1410

nose=[]

while nose_start_y<1250:
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
    
#ctx_override = bpy.context.copy()
#ctx_override['area'] = the_area
#print(context_override())
#override={'area': 'VIEW_3D', 'region': 'WINDOW'}
bpy.ops.paint.image_paint(context_override(),stroke=nose)


'''mouth_upper_start_y= 320
mouth_upper_start_x = 680

mouth_upper=[]

while mouth_upper_start_x<750:
    mouth_upper.append({
    "name": "stiching",
    "location": (0, 0, 0),
    "mouse": (mouth_upper_start_x,mouth_upper_start_y),
    "mouse_event": (0,0),
    "x_tilt": 0,
    "y_tilt": 0,
    "size": 15,
    "pressure": 80,
    "pen_flip": False,
    "time": 0,
    "is_start": True
    })
    mouth_upper_start_x= mouth_upper_start_x+5


bpy.ops.paint.image_paint(context_override(), stroke=mouth_upper)'''

'''mouth_lower_start_y= 328
mouth_lower_start_x = 620

mouth_lower=[]

while mouth_lower_start_x<760:
    mouth_lower.append({
    "name": "stiching",
    "location": (0, 0, 0),
    "mouse": (mouth_lower_start_x,mouth_lower_start_y),
    "mouse_event": (0,0),
    "x_tilt": 0,
    "y_tilt": 0,
    "size": 30,
    "pressure": 100,
    "pen_flip": False,
    "time": 0,
    "is_start": True
    })
    mouth_lower_start_x= mouth_lower_start_x+5


bpy.ops.paint.image_paint(context_override(), stroke=mouth_lower)'''
