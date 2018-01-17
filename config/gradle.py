from config import CommonConfig
from os import path
import os

FILE = "build.gradle"

"""
同步两个文件的配置
"""

KEY = "gradle:"


def get_file_path(dir_path):
    return dir_path + "/" + FILE


def backup(dir_path):
    full_path = get_file_path(dir_path)
    backup_path = backup_file_path(dir_path)
    remove_backup(backup_path)
    os.rename(full_path, backup_path)
    pass


def backup_file_path(dir_path):
    return get_file_path(dir_path) + ".backup"


def remove_backup(file_path):
    if path.isfile(file_path):
        os.remove(file_path)


def modify(dir_path):
    print("modify")
    file = open(backup_file_path(dir_path))
    lines = file.readlines()
    file.close()
    # print(lines)

    new_path = get_file_path(dir_path)
    new_file = open(new_path, "w")
    for i in range(len(lines)):
        line = lines[i]
        # 忽略注释的行
        if "classpath" in line and "//" not in line:
            # 找到目标行并整行替换
            print("将要替换的内容：" + line)
            line = CommonConfig.GRADLE_TOOLS + "\n"
            print("替换后: " + line)

        # 写入文件
        new_file.write(line)

    new_file.close()
    print("modify end")
    pass


def sync(target_dir):
    print(CommonConfig.BUILD_TOOLS)
    full_path = get_file_path(target_dir)
    print(full_path)
    is_exist = path.isfile(full_path)
    if is_exist:
        print("开始修改" + full_path)
        backup(target_dir)
        modify(target_dir)
        remove_backup(target_dir)
        print("修改完成" + full_path)
    else:
        print("文件不存在")
