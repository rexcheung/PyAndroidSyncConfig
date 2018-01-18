from os import path
import os

'''
根据文件名，搜索指定文件，执行递归操作，
把匹配文件的列表完整路径返回。

@:param url 根目录，从哪个目录开始搜索
@:param fullname，文件名全称，包括文件名和扩展名，若参数为''，空字符串，则匹配所有文件。
@:return type=list
'''


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
