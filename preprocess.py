#!/usr/bin/env python3

import binvox_rw
import numpy as np
from pathlib import Path

def preprocess():
    imgs = Path("models/models-screenshots/screenshots")
    voxels = Path("models/models-binvox-solid/data")
    fimgs = [f for f in imgs.iterdir() if f.is_dir()]
    fvoxels = [f for f in voxels.iterdir() if f.is_file()]
    g = [0, 1, 6, 7]

    #To remove the files which do not have corresponding images or are unreadable or have zero volume
    unreadable = 0
    zerovolume = 0
    i = -1
    while i < len(fvoxels):
        i += 1
        try:
            with open(str(fvoxels[i]), 'rb') as f:
                model = binvox_rw.read_as_3d_array(f)
        except:
            unreadable += 1
            print(str(fvoxels[i]), "Unreadable")
            fvoxels[i].unlink()
            if (i < len(fimgs)) and (fvoxels[i].stem == fimgs[i].stem):
                fvoxels.pop(i)
                fimgs.pop(i)
            else:
                fvoxels.pop(i)
            continue
        if np.sum(model.data) == 0:
            zerovolume += 1
            fvoxels[i].unlink()
            if (i < len(fimgs)) and (fvoxels[i].stem == fimgs[i].stem):
                fvoxels.pop(i)
                fimgs.pop(i)
            else:
                fvoxels.pop(i)
        else:
            if i < len(fimgs) and i < len(fvoxels):
                while not fvoxels[i].stem == fimgs[i].stem:
                    fvoxels[i].unlink()
                    fvoxels.pop(i)
            else:
                fvoxels[i].unlink()
                fvoxels.pop(i)

    print(f"Total unreadable:{unreadable}, Total 0volume:{zerovolume}")

    # To create 4 new folders, one for each view
    for ii in range(4):
        Path(f"models/models-screenshots/view{ii}").mkdir(exist_ok=True)
        Path(f"models/models-screenshots/view{ii}/data").mkdir(exist_ok=True)

    # To seperate each view of a model into it's corresponding image
    for j in range(len(fimgs)):
        img_files = [f for f in fimgs[j].iterdir() if f.is_file]
        if len(img_files)==15:
            for k in range(4):
                pieces = img_files[g[k]].parts
                img_files[g[k]].rename(Path(f"{pieces[0]}/{pieces[1]}/view{k}/data/{pieces[4]}"))

if __name__ == "__main__":
    preprocess()
