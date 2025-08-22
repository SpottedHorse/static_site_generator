import os
import shutil

def copy_files(source, dest):
  if os.path.exists(dest):
    shutil.rmtree(dest)
  shutil.copytree(source, dest)
  # os.mkdir(dest)

  # files = os.listdir(source)

  # for file in files:
  #   if not os.path.isfile(file):
  #     folder = os.path.join(source, file)


