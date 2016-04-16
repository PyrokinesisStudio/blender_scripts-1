import bpy

# Renames ManuelBastioniLab characters vertex groups to match rigify
# just select the mesh and run the script

mapping = {
"calf_L" : "DEF-shin.01.L",
"calf_R" : "DEF-shin.01.R",
"clavicle_L" : "DEF-shoulder.L",
"clavicle_R" : "DEF-shoulder.R",
"foot_L" : "DEF-foot.L",
"foot_R" : "DEF-foot.R",
"hand_L" : "DEF-hand.L",
"hand_R" : "DEF-hand.R",
"head" : "DEF-head",
"index00_L" : "DEF-palm.01.L",
"index00_R" : "DEF-palm.01.R",
"index01_L" : "DEF-f_index.01.L.01",
"index01_R" : "DEF-f_index.01.R.01",
"index02_L" : "DEF-f_index.02.L",
"index02_R" : "DEF-f_index.02.R",
"index03_L" : "DEF-f_index.03.L",
"index03_R" : "DEF-f_index.03.R",
"lowerarm_L" : "DEF-forearm.01.L",
"lowerarm_R" : "DEF-forearm.01.R",
"middle00_L" : "DEF-palm.02.L",
"middle00_R" : "DEF-palm.02.R",
"middle01_L" : "DEF-f_middle.01.L.01",
"middle01_R" : "DEF-f_middle.01.R.01",
"middle02_L" : "DEF-f_middle.02.L",
"middle02_R" : "DEF-f_middle.02.R",
"middle03_L" : "DEF-f_middle.03.L",
"middle03_R" : "DEF-f_middle.03.R",
"neck" : "DEF-neck",
"pelvis" : "DEF-hips",
"pinky00_L" : "DEF-palm.04.L",
"pinky00_R" : "DEF-palm.04.R",
"pinky01_L" : "DEF-f_pinky.01.L.01",
"pinky01_R" : "DEF-f_pinky.01.R.01",
"pinky02_L" : "DEF-f_pinky.02.L",
"pinky02_R" : "DEF-f_pinky.02.R",
"pinky03_L" : "DEF-f_pinky.03.L",
"pinky03_R" : "DEF-f_pinky.03.R",
"ring00_L" : "DEF-palm.03.L",
"ring00_R" : "DEF-palm.03.R",
"ring01_L" : "DEF-f_ring.01.L.01",
"ring01_R" : "DEF-f_ring.01.R.01",
"ring02_L" : "DEF-f_ring.02.L",
"ring02_R" : "DEF-f_ring.02.R",
"ring03_L" : "DEF-f_ring.03.L",
"ring03_R" : "DEF-f_ring.03.R",
"spine01" : "DEF-hips00",
"spine02" : "DEF-spine",
"spine03" : "DEF-chest",
"thigh_L" : "DEF-thigh.01.L",
"thigh_R" : "DEF-thigh.01.R",
"thumb01_L" : "DEF-thumb.01.L.01",
"thumb01_R" : "DEF-thumb.01.R.01",
"thumb02_L" : "DEF-thumb.02.L",
"thumb02_R" : "DEF-thumb.02.R",
"thumb03_L" : "DEF-thumb.03.L",
"thumb03_R" : "DEF-thumb.03.R",
"toes_L" : "DEF-toe.L",
"toes_R" : "DEF-toe.R",
"upperarm_L" : "DEF-upper_arm.01.L",
"upperarm_R" : "DEF-upper_arm.01.R"
}

for i in bpy.context.object.vertex_groups:
    try:
        i.name = mapping[i.name]
    except:
        print('nope')
