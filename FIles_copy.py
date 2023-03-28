import os
import shutil

k=0
for root, dirs, files in os.walk(r'D:/Kavach/Dataset'):
    for file in files:
        # check the extension of files
        if file.endswith('.jpg'):
            # print whole path of files
            path=os.path.join(root, file)


           shutil.copy(path, 'Train/Images/')

            k+=1
            print(k, "files done")
            
