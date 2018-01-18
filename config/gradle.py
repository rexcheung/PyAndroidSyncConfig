import os
from config import constant
from os import path

'''
接收到gradle文件路径
读取文件内容
判断有没需要修改的
1. 若有修改，则删除旧文件，创建新文件
2. 没有则什么都不需要做了。
'''


def test(new_content):
    for i in range(len(new_content)):
        print(new_content[i])


def sync_gradle(filepath):
    # 文件不存在则退出
    if not path.isfile(filepath):
        print('文件不存在')
        return

    source_file = open(filepath)
    lines = source_file.readlines()
    source_file.close()

    modify = False

    new_content = []
    for i in range(len(lines)):
        line = lines[i]
        if '//' in line:
            # 忽略注释的行
            new_content.append(line)
            continue

        if "com.android.tools.build:gradle" in line:
            line = '\t\t' + constant.GRADLE_TOOLS + "\n"
            modify = True
        elif 'buildToolsVersion' in line:
            line = '\t' + constant.BUILD_TOOLS + '\n'
            modify = True
        elif 'compileSdkVersion' in line:
            line = '\t' + constant.COMPILE_SDK + '\n'
            modify = True
        elif 'minSdkVersion' in line:
            line = '\t' + constant.MIN_SDK + '\n'
            modify = True
        elif 'targetSdkVersion' in line:
            line = '\t' + constant.TARGET_SDK + '\n'
            modify = True

        new_content.append(line)

    # 没有修改则什么都不用做了。
    if not modify:
        return

    # test(new_content)
    update(filepath, new_content)


def update(filepath, content):
    if os.path.isfile(filepath):
        os.remove(filepath)

    new_file = open(filepath, 'w')
    new_file.writelines(content)
    new_file.close()
