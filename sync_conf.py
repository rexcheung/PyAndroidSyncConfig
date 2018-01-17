from config import local
from config import gradle
from config import rootgradle

SOURCE_PATH = ""
SOURCE_APP_MODULE_NAME = ""
TARGET_PATH = ""
TARGET_APP_MODULE_NAME = ""


def main():
    print("main() begin")
    local.copy_not_exist("files", "targetFiles")
    gradle.sync("files")
    rootgradle.sync("a", "b")
    print("main() end")

    print("test")
    str="classpath 'com.android.tools.build:gradle:XXX'"
    result=str.replace("[0-9]?", "w")
    print(result)
    print("test")


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
