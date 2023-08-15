""" Hi I am Shah_alam """

import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'

postfix = [1,2,3]

source_object = glob.glob(source_path)
#print(source_object)

object_path = source_object[0]

shutil.copy(object_path , '.')

#print(object_path.split('\\')[-1])

object_name = object_path.split('\\')[-1].split('.')
prefix = object_name[0]
postfix2 = object_name[1]

for item in range(len(postfix)):
    filename = prefix + '_' + str(item + 1) + '.' + postfix2
#    print(filename)
    shutil.copy(object_path,f"{destination_path}/{filename}")

os.remove(object_path)
os.remove(object_path.split('\\')[-1])
