import bpy
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"



def assign_samples(num_samples):
    preferences = bpy.context.preferences

    if (bpy.context.scene.render.engine == "CYCLES"):
        # cycles_preferences = preferences.addons["cycles"].preferences
        bpy.context.scene.cycles.samples = num_samples

    elif (bpy.context.scene.render.engine == "BLENDER_EEVEE"):
        bpy.context.scene.eevee.taa_render_samples = num_samples
        
    elif (bpy.context.scene.render.engine == "BLENDER_WORKBENCH"):
        bpy.context.scene.render_aa = num_samples

    return num_samples


assign_samples(argv[0]) # assuming that the 1st argument will be samples
