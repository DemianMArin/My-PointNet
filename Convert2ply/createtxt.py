#!/bin/env python

import os
from pathlib import Path


# airplane, bookshelf, cup
path = Path("./test/")

num_folder = 0
num_files = 0
with open('test3.txt', 'w') as file:
    for subdir in path.iterdir(): 
        if subdir.is_dir():
            relative_path = str(subdir)
            relative_path_name = str(subdir).split('/')[1]
            # print(f" {relative_path}")
            for entry in os.listdir(relative_path):
                # print(f"{entry}")
                if relative_path_name == 'airplane' or relative_path_name == 'bookshelf' or relative_path_name == 'cup':

                    file.write(f"{relative_path_name}/{entry}\n")

                # num_files = num_files + 1
                # if num_files > 0:
                #     break
        #
        # num_folder = num_folder + 1
        # if num_folder > 0:
        #     break

