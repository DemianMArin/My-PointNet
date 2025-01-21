#!/bin/env python
import trimesh
import os
from pathlib import Path


path = Path("/home/vanttec/ModelNet40")

num_folders = 0
num_files = 0
for subdir in path.iterdir(): 
    if subdir.is_dir():
        folder_path = str(subdir) + "/test"
        name_folder = str(subdir).split('/')[-1]
        print(f"Name Folder: {name_folder}")
        for entry in os.listdir(folder_path):
            name_file = str(entry).split(".")[0]
            mesh = trimesh.load(folder_path+'/'+entry)
            folder2save = f'./test/{name_folder}/'

            if not os.path.exists(folder2save):
                os.makedirs(folder2save)

            mesh.export(f'{folder2save}{name_file}.ply')


    #         num_files = num_files + 1
    #         if num_files > 0:
    #             break
    #
    # num_folders = num_folders + 1
    # if num_folders > 0:
    #     break

