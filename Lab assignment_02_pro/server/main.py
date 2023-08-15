import glob
import shutil
import zipfile
import os
import subprocess
import time
source_path = '../sources/*'  # dataa base directory

while True:  # Start Event All Updated Check and Process by sources directory
    # source directory fetced path of list
    source_object = glob.glob(source_path)
    if len(source_object) > 0:  # check path of list not less than zero if zero skip this command
        # create a .zip file under disination directory
        zip_file = zipfile.ZipFile('../destination/.zip', 'w')
        for object_path in source_object:  # traverse list of path all
            if object_path.endswith('.py'):  # check python file
                # python file execute time 1 sec late again and again
                time.sleep(1)
                # execite python file sources filder comand
                print(f'{"-"*100}\n')
                subprocess.run(f'py {object_path}', shell=True)
                print(f'{"-"*100}\n')
                print()
                print()
            else:  # checkking txt file else
                # extract object_path to object name exm: some.txt
                object_name = object_path.split('\\')[-1].split('.')[0]
                # obejct name split first word exmple: some
                prefix = object_path.split('\\')[-1].split('.')[0]
                # obejct name split last word exmple: .txt
                postfix = object_path.split('\\')[-1].split('.')[1]
                # open file read and write mode
                with open(object_path, 'r+', encoding="utf8") as file:
                    data = file.readlines()  # store the all content in the file
                    for i in range(3):  # 3 times of loop start
                        # filename making fist and last word
                        filename = f'{prefix}_{i+1}.{postfix}'
                        # copy object_path with filename
                        current_file = shutil.copy(object_path, filename)
                        # open only write mode file
                        with open(current_file, 'w', encoding='utf8') as file_2:
                            for j in range(0, (i+1)*10):  # start traverse some tecnique
                                # content add depend on iteration
                                file_2.write(data[j])
                        # making ziped file and append to zip file
                        zip_file.write(filename)
                        # remove this directory all sources file copyed
                        os.remove(filename)
        zip_file.extractall('../destination')  # extract the ziped file
        zip_file.close()  # closed the zip file