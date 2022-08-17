import os
import shutil
from  extensions import ExtensionList

sourceDirPath = "C:/Users/Hussain/Downloads/"
destinationDirPath = "D:/Organiser/"
 
files = os.listdir(sourceDirPath)
for file in files:
    SplittedFile = file.split(".")
    for x,y in ExtensionList.items():
        if(y.__contains__(SplittedFile[len(SplittedFile)-1].lower())):
            if(os.path.isdir(destinationDirPath+x)):
                shutil.move(sourceDirPath+file,destinationDirPath+x+"/")
            else:
                os.mkdir(destinationDirPath+x)
                shutil.move(sourceDirPath+file,destinationDirPath+x+"/")
