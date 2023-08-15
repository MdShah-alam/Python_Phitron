import glob
from zipfile import ZipFile
import shutil
import os


source_path='../source/*'
source_path_2='../source'
destination_path = '../destination'
postfix=[1,2,3]
source_object=glob.glob(source_path)

source_object[0]=source_object[0].replace(chr(92),'/')
object_path=source_object[0]
# print(object_path)

object_name=object_path.split('/')[-1].split('.')

prefix=object_name[0]
postfix2='.'+object_name[1]
main_file_path=f'{source_path_2}/{prefix+postfix2}'

# main_file=open(main_file_path,'r')
# lines=main_file.readlines()
# main_file.close()

lines=[]
filenames=[]
with open(main_file_path,'r') as file:
    lines=file.readlines()

# print(lines)
cont=0
zpf = ZipFile("../destination/.zip",'w')
for item in range(1,len(postfix)+1):
    filename=prefix+'_'+str(item)+postfix2
    file_path=f"{source_path_2}/{filename}"
    destion=f"{destination_path}/{filename}"
    file=open(destion ,'w')
    filenames.append(filename)

    for i in range(0,(item)*10):
        file.write(lines[i])
        print(filename)
        zpf.write(filename)
    file.close()



# with zipfile.ZipFile(f"{destination_path}/data.zip",'w') as file:
#     print(file)
    

# shutil.make_archive(object_path,"zip",c)

# with zipfile.ZipFile(f"{source_path_2}/sample.zip","w") as archive:
#     for file in filenames:
#         archive.write(f"{source_path_2}/{file}")
#         # os.remove(file)
#     print(f"{source_path_2}/sample.zip",f"{destination_path}/{archive}")
#     shutil.copy(object_path,f"{destination_path}/sample.zip")
#     print(f"{destination_path}/sample.zip")
#     archive.extractall('..\destination')
# archive.close()

    # for line in file:
    #     if i==item*10:
    #         break
    #     else:
    #         file2=open(filename,'a')
    #         file2.write(line)
    #         i+=1SSS
    #         file2.close()
    # file.close()
#     with zipfile.ZipFile("sample.zip", mode="a") as archive:
#         archive.write(filename)
#     archive.close()

# with zipfile.ZipFile("sample.zip", mode="r") as archive:
#     for filename in archive.namelist():
#         print(filename)
#         shutil.copy(object_path,f"{destination_path}/{filename}")

# with ZipFile(zfile_name,'w') as zip:
#                     for file in file_names:
#                         zip.write(file)
#                         os.remove(file) 
#                     shutil.copy(object_path, f'{destination_path}/{zfile_name}')
#                     zip.extractall('..\destination')
