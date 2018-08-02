import bpy
from math import radians
from mathutils import Matrix
from os import system

f = open("/Users/Sailesh/Documents/CS/Projects/CDSAML/text2scene/object_path.txt","r")

full_file = f.read()
lines = full_file.split('\n')

i = 0
while i < len(lines)-1:
    path = lines[i]
    i += 1
    num = int(lines[i])
    i += 1
    
    n = 0;
    while n < num:
        pos = int(lines[n+i])
        
        flag = 0
        if (n+1 < num and int(lines[n+i+1]) == pos):
            flag = 1
        
        if (flag == 0):
            #left
            if(pos == -1):
                bpy.ops.import_scene.obj(filepath = path)
                obj_objects = bpy.context.selected_objects[:]
            
                for obj in obj_objects:
                    bpy.context.scene.objects.active = obj
                    obj.location = (0,-1,0.25)
                    obj.rotation_euler = (radians(90), 0, radians(90))
                
            #right
            elif (pos == -2):
                bpy.ops.import_scene.obj(filepath = path)
                obj_objects = bpy.context.selected_objects[:]
            
                for obj in obj_objects:
                    bpy.context.scene.objects.active = obj
                    obj.location = (0,1,0.25)
                    obj.rotation_euler = (radians(90), 0, radians(270))
                
            #front
            elif (pos == -3):
                bpy.ops.import_scene.obj(filepath = path)
                obj_objects = bpy.context.selected_objects[:]
            
                for obj in obj_objects:
                    bpy.context.scene.objects.active = obj
                    obj.location = (1,0,0.25)
                    obj.rotation_euler = (radians(90), 0, radians(180))
                
            #back
            elif (pos == -4):
                bpy.ops.import_scene.obj(filepath = path)
                obj_objects = bpy.context.selected_objects[:]
            
                for obj in obj_objects:
                    bpy.context.scene.objects.active = obj
                    obj.location = (-1,0,0.25)
                    obj.rotation_euler = (radians(90), 0, 0)
                
            #default
            elif (pos == -5):
                bpy.ops.import_scene.obj(filepath = path)
                obj_objects = bpy.context.selected_objects[:]
            
                for obj in obj_objects:
                    bpy.context.scene.objects.active = obj
                    obj.location = (0,0,0.2)
                    obj.rotation_euler = (radians(90), 0, 0)
                    
            #above
            else:
                bpy.ops.import_scene.obj(filepath = path)
                obj_objects = bpy.context.selected_objects[:]
            
                for obj in obj_objects:
                    bpy.context.scene.objects.active = obj
                    obj.location = (0,0,0.65)
                    obj.rotation_euler = (radians(90), 0, 0)
                    
            n += 1
                    
        else:
            count = 2
            k = n+2
            while k < num:
                if (int(lines[k+i]) == pos):
                    count += 1
                    k += 1
                else:
                    break
            
            a = (count-1) / 4
            
            for c in range(count):

                #left
                if(pos == -1):
                    bpy.ops.import_scene.obj(filepath = path)
                    obj_objects = bpy.context.selected_objects[:]
                    
                    for obj in obj_objects:
                        bpy.context.scene.objects.active = obj
                        obj.location = (a,-1,0.25)
                        obj.rotation_euler = (radians(90), 0, radians(90))
                        
                #right
                elif (pos == -2):
                    bpy.ops.import_scene.obj(filepath = path)
                    obj_objects = bpy.context.selected_objects[:]
                
                    for obj in obj_objects:
                        bpy.context.scene.objects.active = obj
                        obj.location = (a,1,0.25)
                        obj.rotation_euler = (radians(90), 0, radians(270))
                    
                #front
                elif (pos == -3):
                    bpy.ops.import_scene.obj(filepath = path)
                    obj_objects = bpy.context.selected_objects[:]
                
                    for obj in obj_objects:
                        bpy.context.scene.objects.active = obj
                        obj.location = (1,a,0.25)
                        obj.rotation_euler = (radians(90), 0, radians(180))
                    
                #back
                elif (pos == -4):
                    bpy.ops.import_scene.obj(filepath = path)
                    obj_objects = bpy.context.selected_objects[:]
                
                    for obj in obj_objects:
                        bpy.context.scene.objects.active = obj
                        obj.location = (-1,a,0.25)
                        obj.rotation_euler = (radians(90), 0, 0)
                    
                #default???
                elif (pos == -5):
                    bpy.ops.import_scene.obj(filepath = path)
                    obj_objects = bpy.context.selected_objects[:]
                
                    for obj in obj_objects:
                        bpy.context.scene.objects.active = obj
                        obj.location = (0,0,0.2)
                        obj.rotation_euler = (radians(90), 0, 0)
                        
                #above???
                else:
                    bpy.ops.import_scene.obj(filepath = path)
                    obj_objects = bpy.context.selected_objects[:]
                
                    for obj in obj_objects:
                        bpy.context.scene.objects.active = obj
                        obj.location = (0,0,0.65)
                        obj.rotation_euler = (radians(90), 0, 0)
                    
                a -= 0.5
            
            n += count

    i += num