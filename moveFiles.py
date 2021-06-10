import os
import shutil

source = input("Enter the source")
destination = input("Enter the destination")
source = source+'/'
destination = destination+'/'
list = os.listdir(source)

for file in list:
    shutil.move((source+file),destination)