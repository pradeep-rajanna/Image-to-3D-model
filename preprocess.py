#!/usr/bin/env python3

import zipfile
import binvox_rw
import numpy as np
from pathlib import Path
from shutil import rmtree

def preprocess():
    # TODO
    # add checks to verify file structure and uncomment the following lines
    #
    # Required file structure:
    #
    # models 
    # ├── models-binvox-solid
    # │   ├── models-binvox-solid (to be deleted)
    # │   └── data
    # └── model-screenshots
    #     ├── screenshots (to be deleted)
    #     ├── view0
    #     │   └── data
    #     ├── view1
    #     │   └── data
    #     ├── view2
    #     │   └──data
    #     └── view3
    #         └── data
    #

    imgs = Path("models/models-screenshots/screenshots")
    voxels = Path("models/models-binvox-solid/models-binvox-solid")
    
    if not (imgs.parent.exists() and voxels.parent.exists()):
        pass   
        #with zipfile.ZipFile('models/models-binvox-solid.zip','r') as zip_ref:
        #    zip_ref.extractall('models/models-binvox-solid')
        #with zipfile.ZipFile('models/models-screenshots.zip','r') as zip_ref:
        #    zip_ref.extractall('models/models-screenshots')
    if not (imgs.exists() and voxels.exists()):
        return
    
    fimgs = [f for f in imgs.iterdir() if f.is_dir()]
    fvoxels = [f for f in voxels.iterdir() if f.is_file()]
    fimgs_stem = [f.stem for f in imgs.iterdir() if f.is_dir()]
    fvoxels_stem = [f.stem for f in voxels.iterdir() if f.is_file()]
    g = [0, 1, 6, 7, 8, 9, 10, 11, 12, 13, 2, 3, 4, 5]
    diff = set(set(fvoxels_stem) - set(fimgs_stem))

    #To remove the files which do not have corresponding images or are unreadable or have zero volume
    if not len(fvoxels) == 11694:
        i = -1
        remove = []
        while i < len(fvoxels)-1:
            i+=1
            if fvoxels[i].stem in diff:
                remove.append(fvoxels[i].stem)
                continue
            try:
                with open(str(fvoxels[i]), 'rb') as f:
                    model = binvox_rw.read_as_3d_array(f)
                if np.sum(model.data) == 0:
                    remove.append(fvoxels[i].stem)
            except:
                remove.append(fvoxels[i].stem)
        
        Path(f"models/models-binvox-solid/data").mkdir(exist_ok=True)
        c = 0
        for fvoxel in fvoxels:
            if not fvoxel.stem in remove:
                c += 1
                fvoxel.rename(Path(f"models/models-binvox-solid/data/{c:05d}.binvox"))
        
        for fimg in fimgs:
            if fimg.stem in remove:
                rmtree(fimg)

    # To create 4 new folders, one for each view
    for ii in range(14):
        Path(f"models/models-screenshots/view{ii}").mkdir(exist_ok=True)
        Path(f"models/models-screenshots/view{ii}/data").mkdir(exist_ok=True)

    # To seperate each view of a model into it's corresponding image
    fimgs = [f for f in imgs.iterdir() if f.is_dir()]
    c = 0
    for j in range(len(fimgs)):
        img_files = [f for f in fimgs[j].iterdir() if f.is_file]
        if len(img_files)==15:
            c += 1
            for k in range(14):
                img_files[g[k]].rename(Path(f"models/models-screenshots/view{k}/data/{c:05d}-{k:02d}.png"))
    
    rmtree(Path("models/models-screenshots/screenshots"))
    rmtree(Path("models/models-binvox-solid/models-binvox-solid"))

if __name__ == "__main__":
    preprocess()
