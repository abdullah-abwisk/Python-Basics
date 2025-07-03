''' os module '''

import os

# get current working directory
print(os.getcwd())
# change directory
#os.chdir(path in string)
print(os.getcwd())
# list files in directory
print(os.listdir())
# make directory if not exists
if not os.path.exists('OSCreateDirectory'):
    os.mkdir('OSCreateDirectory')
    
# remove directory
if os.path.exists('OSCreateDirectory'):
    os.rmdir('OSCreateDirectory')
    
# create a directory and 100 python files in it
if not os.path.exists('OSCreateDirectory'):
    os.mkdir('OSCreateDirectory')
    for i in range(100):
        with open(f'OSCreateDirectory/file_{i}.py', 'w') as f:
            f.write('print("Hello World")')
            
# remove all files in directory
for i in range(100):
    os.remove(f'OSCreateDirectory/file_{i}.py')
    
# remove directory
if os.path.exists('OSCreateDirectory'):
    os.rmdir('OSCreateDirectory')

# rename file
if not os.path.exists('OSCreateDirectory'):
    os.mkdir('OSCreateDirectory')
    with open('OSCreateDirectory/file.py', 'w') as f:
        f.write('print("Hello World")')
    os.rename('OSCreateDirectory/file.py', 'OSCreateDirectory/newfile.py')
    
# remove file
if os.path.exists('OSCreateDirectory/newfile.py'):
    os.remove('OSCreateDirectory/newfile.py')
    
# remove directory
if os.path.exists('OSCreateDirectory'):
    os.rmdir('OSCreateDirectory')
    
# get file size
print(os.path.getsize('024_OSModule.py'))
# get file last modified time
print(os.path.getmtime('024_OSModule.py'))
# get file last accessed time
print(os.path.getatime('024_OSModule.py'))
# get file last created time
print(os.path.getctime('024_OSModule.py'))

# get file stats
print(os.stat('024_OSModule.py'))
# get file stats as a dictionary
print(os.stat('024_OSModule.py').st_size)
print(os.stat('024_OSModule.py').st_mtime)
print(os.stat('024_OSModule.py').st_atime)
print(os.stat('024_OSModule.py').st_ctime)
print(os.stat('024_OSModule.py').st_mode)
print(os.stat('024_OSModule.py').st_uid)
print(os.stat('024_OSModule.py').st_gid)
print(os.stat('024_OSModule.py').st_ino)
print(os.stat('024_OSModule.py').st_dev)
print(os.stat('024_OSModule.py').st_nlink)
print(os.stat('024_OSModule.py').st_blocks)
print(os.stat('024_OSModule.py').st_blksize)
print(os.stat('024_OSModule.py').st_blocks)
print(os.stat('024_OSModule.py').st_blksize)
print(os.stat('024_OSModule.py').st_rdev)
print(os.stat('024_OSModule.py').st_flags)
print(os.stat('024_OSModule.py').st_gen)
print(os.stat('024_OSModule.py').st_birthtime)

# get environment variables
print(os.environ)
print(os.environ.get('HOME'))
print(os.environ.get('PATH'))
print(os.environ.get('USER'))
print(os.environ.get('SHELL'))

# join paths
print(os.path.join(os.getcwd(), '024_OSModule.py'))
print(os.path.join(os.getcwd(), 'OSCreateDirectory', 'newfile.py'))
print(os.path.join(os.getcwd(), 'OSCreateDirectory', 'newfile.py', 'newfile.py'))

# get basename
print(os.path.basename('024_OSModule.py'))
print(os.path.basename('OSCreateDirectory'))
print(os.path.basename('OSCreateDirectory/newfile.py'))

# get directory name
print(os.path.dirname('024_OSModule.py'))
print(os.path.dirname('OSCreateDirectory'))

# get both directory name and basename
print(os.path.split('024_OSModule.py'))
print(os.path.split('OSCreateDirectory'))

# get file extension
print(os.path.splitext('024_OSModule.py'))

# walk through directory
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
    
# check if path exists
print(os.path.exists('024_OSModule.py'))

# check if path is a file
print(os.path.isfile('024_OSModule.py'))

# check if path is a directory
print(os.path.isdir('024_OSModule.py'))

# split path
print(os.path.split('024_OSModule.py'))

# create folder with 100 subfolders
if not os.path.exists('OSCreateDirectory'):
    os.mkdir('OSCreateDirectory')
    for i in range(100):
        os.mkdir(f'OSCreateDirectory/folder_{i}')
        
# remove folder with 100 subfolders
if os.path.exists('OSCreateDirectory'):
    for i in range(100):
        os.rmdir(f'OSCreateDirectory/folder_{i}')
    os.rmdir('OSCreateDirectory')