import os

# current directory
current_workding_dir = os.getcwd()
print(current_workding_dir)


# display all files and folder in current directory
files_and_folders_in_dir = os.listdir(current_workding_dir)
for f in files_and_folders_in_dir:
  print("f", f)
  
  
# display all files and folder of parent directory
current_workding_dir = os.getcwd()
print("current_workding_dir", current_workding_dir)
path = os.path.join(current_workding_dir, "..")
print("path", path)
abs_path = os.path.abspath(path)
print("abs_path", abs_path)

files_and_folders_in_dir = os.listdir(abs_path)
for f in files_and_folders_in_dir:
  print("f", f)
