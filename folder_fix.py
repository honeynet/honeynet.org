import os

# directory/folder path
dir_path = r'./content/projects'

for c in os.listdir(dir_path):
    print(c)
    parts = c.split("-")
    post_name = "-".join(parts[3:])
    path = os.path.join(dir_path, parts[0])
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path, parts[1])
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path, parts[2])
    if not os.path.exists(path):
        os.mkdir(path)
    os.rename(os.path.join(dir_path, c), os.path.join(path, post_name)) 

# Iterate directory
# for year_path in os.listdir(dir_path):
#     # check if current file_path is a file
#     if not os.path.isfile(os.path.join(dir_path, year_path)):
#         for month_path in os.listdir(dir_path+"/"+year_path):
#             if not os.path.isfile(os.path.join(dir_path, year_path, month_path)):
#                 if not len(month_path) == 2:
#                     parts = month_path.split("-")
#                     post_name = "-".join(parts[3:])
#                     path = os.path.join(dir_path, year_path, parts[1])
#                     if not os.path.exists(path):
#                         os.mkdir(path)
#                     if not os.path.exists(os.path.join(path, parts[2])):
#                         os.mkdir(os.path.join(path, parts[2]))
#                     os.rename(os.path.join(dir_path,year_path,month_path), os.path.join(path, parts[2], post_name))          
