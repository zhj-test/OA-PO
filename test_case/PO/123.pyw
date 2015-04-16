import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

print BASE_DIR

file_path = os.path.join(BASE_DIR,"data\\Upload\\upfile.exe")

print file_path







os.system(file_path)
print '123456'
