from config import local
from config import gradle
from config import rootgradle
import search

SOURCE_PATH = ""
SOURCE_APP_MODULE_NAME = ""
TARGET_PATH = ""
TARGET_APP_MODULE_NAME = ""


def main():
    print("=========main() begin==========")
    # local.copy_not_exist("files", "targetFiles")
    # gradle.sync("files")
    # rootgradle.sync("a", "b")
    files = search.find_by_fullname('/Users/xmyy-26/apps/android/workspace', 'build.gradle')
    for i in range(len(files)):
        print(files[i])

    localpro = search.find_by_fullname('/Users/xmyy-26/apps/android/workspace/OPenHAB_app_andorid', 'local.properties')
    print(localpro)
    print("==========main() end==========")



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
