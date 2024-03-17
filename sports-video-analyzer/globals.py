import os
import json

# =================================
# My videos

MY_VIDEOS = {
    "SBT AO VIVO": "https://www.youtube.com/live/MQFMCR0rJw0?si=D86goJSTSdAXmk8i",
    "GLOBO AO VIVO": "https://www.youtube.com/live/LzszUKieWas?si=yhcIV0KFcbEd37Ds",
    "DESCOVERY KIDS AO VIVO": "https://www.youtube.com/watch?v=UBNNGl-YQ6M",
    "RECORD AO VIVO": "https://www.youtube.com/live/LHcOn-EQx24?si=uWRimzics9_lsLE3",
    "REDE BRASIL AO VIVO" : "https://www.youtube.com/live/eu0ghUdIHlk?si=zG87Fy5dIFPwt1Zu"
    }

if "dict_scenes.json" in os.listdir():
    DICT_SCENES = json.load(open('dict_scenes.json'))
else:
    DICT_SCENES = {j: {} for i, j in MY_VIDEOS.items()}

# for url in MY_VIDEOS.values():
#     if url not in DICT_SCENES.keys():
#         DICT_SCENES[url] = {}
with open('dict_scenes.json', 'w') as f:
    json.dump(DICT_SCENES, f)


# =================================
# My videos
DICT_NOTES = json.load(open('dict_notes.json')) if "dict_notes.json" in os.listdir() else {}
with open('dict_notes.json', 'w') as f:
    json.dump(DICT_NOTES, f)