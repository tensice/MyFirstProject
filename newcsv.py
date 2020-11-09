import os
cwd = os.getcwd()
print(cwd)
home_dir = '/Users/ragu/tmp'
os.chdir(home_dir)
print(os.getcwd())
#os.rmdir('d1')

for i in range(5):
    new_dir = f"d{i}"
    print(new_dir)
    os.mkdir(new_dir)
#     my_dir = new_dir
#     os.chdir(my_dir)

os.chdir(home_dir)
