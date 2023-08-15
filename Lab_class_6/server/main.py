
import glob
import shutil
import os

source_path='../source/*'
destination_path='../destination'
postfix=[1,2,3]
while True:
    source_object=glob.glob(source_path)
    # print(source_object)
    if len(source_object)>0:
        
        # source_path=source_object[0].split("\\")
        # print(source_path)
        source_object[0]=source_object[0].replace(chr(92),'/')
        objert_path=source_object[0]

        # print(objert_path)

        # shutil.copy(objert_path,'.')
        object_name=objert_path.split('/')[-1].split('.')
        print(object_name)
        # print(object_name)
        prefix=object_name[0]
        postfix2='.'+object_name[1]

        # print(object_name)
        # print(type(object_name))

        for item in postfix:
            filename=prefix+'_'+str(item)+postfix2       
            shutil.copy(objert_path,f'{destination_path}/{filename}')
            
        os.remove(objert_path)