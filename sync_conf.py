from config import local
from config import gradle
from config import gradle_copy
from config import gradle
import search
import os

SOURCE_PATH = ""
SOURCE_APP_MODULE_NAME = ""
TARGET_PATH = ""
TARGET_APP_MODULE_NAME = ""

WORKSPACE = '/Users/xmyy-26/apps/android/workspace'


def main():
    path = input('请输入完整路径：')
    print(path)
    print("=========main() begin==========")
    # path = '/Users/xmyy-26/Downloads/test/androidWheelView-master'
    # local.properties
    local.copy_not_exist("files", path)
    # build.gradle
    gradle_config(path)

    # gradle/wrapper 删除并复制过去
    gradle_copy.copy(path)


    print("==========main() end==========")


def gradle_config(path):
    gradle_files_path = search.find_by_fullname(path, 'build.gradle')
    for i in range(len(gradle_files_path)):
        file = gradle_files_path[i]
        gradle.sync_gradle(file)


def test():
    f = open("files/local.properties", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        # 检查是否包含特定字符串
        if "sdk" in line:
            print(line)
    f.close()


main()
