import bpy
from math import radians
from mathutils import Matrix

full_path_to_file = "/Users/Sailesh/Documents/CDSAML/text2image/ShapeNetCore.v1/03001627/62127325480bec8d2c6c98851414a9d8/model.obj"

bpy.ops.import_scene.obj(filepath=full_path_to_file)
obj_objects = bpy.context.selected_objects[:]

for obj in obj_objects:
    bpy.context.scene.objects.active = obj
    obj.location = (0,0,0.25)
    
bpy.ops.import_scene.obj(filepath=full_path_to_file)
obj_objects = bpy.context.selected_objects[:]

for obj in obj_objects:
    bpy.context.scene.objects.active = obj
    obj.location = (2,0,0.25)
    obj.rotation_euler = (radians(90), 0, radians(180))

full_path_to_file = "/Users/Sailesh/Documents/CDSAML/text2image/ShapeNetCore.v1/04379243/df03ded86df8fbd2ebd284456950c944/model.obj"

bpy.ops.import_scene.obj(filepath=full_path_to_file)
obj_objects = bpy.context.selected_objects[:]

for obj in obj_objects:
    bpy.context.scene.objects.active = obj
    obj.location = (1,0,0.125)
