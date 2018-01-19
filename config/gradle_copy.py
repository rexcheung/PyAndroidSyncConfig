import shutil
import os


def copy(path):
    source = "files/gradle"
    target = os.path.join(path, 'gradle')
    if os.path.isdir(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)


'''
复制
gradle-wrapper.jar
gradle-wrapper.properties
两个文件
'''
