import os
import chardet


def get_txt_file_encoding(file_path):
    '''
    :param file_path: 文件完整路径，包括文件名
    :return: 编码格式
    示例：
        get_txt_file_encoding()
    '''
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def get_files_in_directory(directory, file_type):
    '''
    递归的找出目表路径下的所有文件
    directory: 目录
    file_type: 文件类型
    示例：
        get_files_in_directory(r'D:\内库\电子书', 'txt')
    '''
    lst = []
    for file_directory, dirnames, filenames in os.walk(directory):
        for file_name in filenames:
            if file_name.endswith(file_type):
                lst.append((file_directory, file_name))
    return lst


