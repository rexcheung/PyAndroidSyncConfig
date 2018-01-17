import shutil
from os import path
import time

FILE = "local.properties"


def copy_not_exist(source_dir, target_dir):
    full_path = source_dir + "/" + FILE
    source_exist = path.isfile(full_path)
    target_exist = path.isfile(target_dir + "/" + FILE)
    if source_exist and target_exist is False:
        start = time.time()
        print("开始复制")
        shutil.copy(full_path, target_dir)
        print("复制完成" + FILE)
        end=time.time()
        print(start - end)
    else:
        print("源文件不存在或目标目录已存在" + FILE)


def read_file(full_path, is_exist):
    if is_exist:
        file = open(full_path)
        lines = file.readlines()
        for i in range(len(lines)):
            print(lines[i])
