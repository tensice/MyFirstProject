import os
os_home = os.environ.get('HOME')
home_dir = os_home + '/tmp'
print(home_dir)
os.chdir(home_dir)
file = 'my_file.txt'
#file_name = home_dir + '/' +'d1' + file
file_name = os.path.join(home_dir,'d1',file)
with open(file,'w') as f:
    f.write('hello world')
current_dir = os.getcwd()
print(current_dir)
print(file_name)
f_path,f_name = os.path.split(file_name)
print(os.path.splitext(f_path))
print(os.path.isdir(file_name))
cwd = os.getcwd()
#for current_path,dirs,files in os.walk(home_dir):
    #print(current_path,dirs,files)
#for i in os.listdir():
    #print(os.stat(i))
    #print(os.path.split(i))
    #print(i)
#for i in d1:
    #print(i,d1.get(i))

#print(os_home)
