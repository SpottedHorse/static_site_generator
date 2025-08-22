import os
import shutil

def copy_files(source, dest):
  if os.path.exists(dest):
    print('path exists, removing folder')
    shutil.rmtree(dest)
    print('folder removed')
  shutil.copytree(source, dest)

def copy_files_recursive(source_dir_path, dest_dir_path):
  if not os.path.exists(dest_dir_path):
    os.mkdir(dest_dir_path)

  for filename in os.listdir(source_dir_path):
    from_path = os.path.join(source_dir_path, filename)
    dest_path = os.path.join(dest_dir_path, filename)
    print(f" * {from_path} -> {dest_path}")
    if os.path.isfile(from_path):
      shutil.copy(from_path, dest_path)
    else:
      copy_files_recursive(from_path, dest_path)