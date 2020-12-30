import os
from datetime import datetime
cwd = os.getcwd()
home_dir = '/Users/ragu/tmp'
os.chdir(home_dir)
#os.rmdir('d1')

#for i in range(5):
#    new_dir = f"d{i}"
#    print(new_dir)
#    os.mkdir(new_dir)
#     my_dir = new_dir
#     os.chdir(my_dir)

os.chdir(home_dir)
print(os.listdir())
#os.rename('abc.txt','xyz')
"""
for file in os.listdir():
    if os.path.isdir(file):
        print(f'{file} is a directory')
    if os.path.isfile(file):
        print(f'{file} is a file')
    mod_time = os.stat(file).st_mtime
    print(datetime.fromtimestamp(mod_time))
    print(os.stat(file).st_size)
"""
def five_files():
    for i in range(1,6):
        file_name = f'abc{i}'
        with open(file_name,'w') as f:
            pass

#five_files()
def rename_abc():
    for file in os.listdir():
        if file.startswith('abc'):
            if os.path.isfile(file):
                print(file)
                new_file_name = file.replace('abc','xyz')
                print(new_file_name)
                os.rename(file,new_file_name)

#rename_abc()

def rename2_pqr():
    for file in os.listdir():
        if file.startswith('xyz') and os.stat(file).st_size > 0 and os.path.isfile(file):
            new_file_name = file.replace('xyz','pqr')
            print(new_file_name)
            #os.rename(file,new_file_name)

rename2_pqr()

