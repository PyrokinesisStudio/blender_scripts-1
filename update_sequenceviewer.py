import bpy
import os
import glob
import time


# old and probably totally messed up script
# automatically loads the newest image of a sequence into the viewer... I used it to monitor the renderfarm output
# load a sequence into the viewer (just the first frame and set the range and autoupdate)
# run the script and the viewer will always load the second latest image (the latest might not be finished)


directory = '/some/folder/'
C = bpy.context

class ModalOperator(bpy.types.Operator):
    bl_idname = "object.modal_operator"
    bl_label = "Simple Modal Operator"

    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    def execute(self, context):
        files = sorted(glob.iglob(directory+'*'), key=os.path.getctime)
        newest = files[-1]
        frame = int(newest.split('.')[-2])
        time.sleep(0.2)
        bpy.ops.image.reload()
        C.scene.frame_current = frame
        bpy.ops.image.reload()
        #img_editors = [area for area in C.screen.areas if area.type == 'IMAGE_EDITOR']

        #if len(img_editors) == 0:
        #    bpy.ops.render.view_show("INVOKE_SCREEN")

        #area = (area for area in C.screen.areas if area.type == 'IMAGE_EDITOR').__next__()
        #for region in area.regions:
            #if region.type == 'WINDOW':
        #    region.tag_redraw()

        return {'FINISHED'}



    def modal(self, context, event):
        #print(event.type)
        bpy.ops.image.reload()
        if event.type in ('RIGHTMOUSE', 'ESC'):  # Cancel
            return {'CANCELLED'}
        if event.type == 'TIMER':
            self.execute(context)

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.execute(context)
        self._timer = context.window_manager.event_timer_add(0.5, context.window)
        context.window_manager.modal_handler_add(self)
        
        return {'RUNNING_MODAL'}


bpy.utils.register_class(ModalOperator)

# test call

bpy.ops.object.modal_operator('INVOKE_DEFAULT')

