import os

def subdir(path, ext):
    list_sub = []
    if os.path.isdir(path) == True:
        for root, dirs, files in os.walk(path):
            for name_sd in dirs:
                list_sub.append(name_sd)
            for file in files:
                if ext in file:
                    list_sub.append(file)
            break
    return list_sub

def return_files(path, ext, flag):
    list_names = []
    ext = '.' + ext
    dir_tr = os.path.isdir(path)
    if not dir_tr:
        return False
    for root, dirs, files in os.walk(path):
        for name_d in dirs:
            list_names.append(name_d)
        for name_file in files:
            if ext in name_file:
                list_names.append(name_file)
        if flag:
            for i in list_names:
                subd_name = root + '\\' + i
                for k in subdir(subd_name, ext):
                    list_names.append(k)
        break

    return list_names


