import glob

source_path='../source/*'
postfix=[1,2,3]
source_object=glob.glob(source_path)

source_object[0]=source_object[0].replace(chr(92),'/')
object_path=source_object[0]

object_name=object_path.split('/')[-1].split('.')

prefix=object_name[0]
postfix2='.'+object_name[1]

for item in postfix:
    i=0
    file=open(object_path,'r')
    filename=prefix+'_'+str(item)+postfix2
    for line in file:
        if i==item*10:
            break
        else:
            file2=open(filename,'a')
            file2.write(line)
            i+=1
            file2.close()
    file.close()

