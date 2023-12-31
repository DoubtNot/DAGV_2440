import maya.cmds as cmds
import random

def placement_generator(x_min, x_max, y_min, y_max, z_min, z_max, num_dups):
    selected_objects = cmds.ls(selection=True) or []

    for obj in selected_objects:
        for _ in range(num_dups):

            duplicate_obj = cmds.duplicate(obj, rr=True)[0]

            rand_x = random.uniform(x_min, x_max)
            rand_y = random.uniform(y_min, y_max)
            rand_z = random.uniform(z_min, z_max)

            cmds.xform(duplicate_obj, worldSpace=True, translation=(rand_x, rand_y, rand_z))

# How To Use: Change the numbers to set a random location
# Number Meanings In Order: x_min, x_max, y_min, y_max, z_min, z_max, num_dups
placement_generator(-10, 10, -20, 40, -10, 10, 5)
