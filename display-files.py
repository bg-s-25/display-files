import glob

files = glob.glob('*.*')

num_files = len(files)
print('Found {} files:'.format(num_files))

for file in files:
    print(file)
