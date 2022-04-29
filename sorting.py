import os 
import shutil
from os import walk
path1=r"C:\Users\prade\Desktop\project\models-binvox-solid\models-binvox-solid"
path2=r'C:\Users\prade\Desktop\project\models-screenshots\screenshots'
f = next(os.walk(path1))[2]
lst1 = []
for x in f:
    lst1.append(os.path.splitext(x)[0])
dir_list2 = os.listdir(path2)
diff=list(set(lst1)-set(dir_list2))
vox=[i for i in lst1 if i not in diff]
k=".binvox"
vox1=[x+k for x in vox]
target1=r'C:\Users\prade\Desktop\project\data2'
for i,j in enumerate(vox1):
    path=os.path.join(target1, str(i))
    os.makedirs(path)
    from1=r"C:\Users\prade\Desktop\project\models-binvox-solid\models-binvox-solid"+'\\'+ j
    to=r'C:\Users\prade\Desktop\project\data2'+'\\'+str(i)
    shutil.copy(from1,to)
for i,j in enumerate(vox):
    dir_list = os.listdir(path2+'\\'+j)
    from1=path2+'\\'+j+'\\'+dir_list[0]
    to1=r'C:\Users\prade\Desktop\project\data2'+'\\'+str(i)
    shutil.copy(from1,to1)
    from2=path2+'\\'+j+'\\'+dir_list[6]
    to2=r'C:\Users\prade\Desktop\project\data2'+'\\'+str(i)
    shutil.copy(from2,to2)
    from3=path2+'\\'+j+'\\'+dir_list[7]
    to3=r'C:\Users\prade\Desktop\project\data2'+'\\'+str(i)
    shutil.copy(from3,to3)
    from4=path2+'\\'+j+'\\'+dir_list[8]
    to4=r'C:\Users\prade\Desktop\project\data2'+'\\'+str(i)
    shutil.copy(from4,to4)