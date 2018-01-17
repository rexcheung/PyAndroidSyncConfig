from os import path
import os


def find_by_fullname(url, fullname):
    matchfiles = []
    filelist = os.listdir(url)
    for i in range(len(filelist)):
        file = filelist[i]
        fullpath = path.join(url, file)
        if path.isfile(fullpath):
            if fullpath.endswith(fullname):
                matchfiles.append(fullpath)
                # print(fullpath)
        else:
            list = find_by_fullname(fullpath, fullname)
            for j in range(len(list)):
                matchfiles.append(list[j])

    return matchfiles
