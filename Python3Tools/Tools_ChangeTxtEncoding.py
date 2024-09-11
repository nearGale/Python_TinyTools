import Python3Tools.Handler_File as handler_file
import codecs

'''
将 txt 文件的编码 从 gb2312 转为 utf-8
'''
if __name__ == "__main__":
    # lst_txt_files = handler_file.get_files_in_directory(r'D:\内库\电子书', 'txt')
    lst_txt_files = handler_file.get_files_in_directory(r'D:\内库\电子书', 'txt')

    failed_lst = []

    for file_directory, file_name in lst_txt_files:
        full_path = file_directory + '\\' + file_name

        encoding = handler_file.get_txt_file_encoding(full_path)
        if encoding != 'GB2312':
            continue

        # 打开 GB2312 文件
        # gb2312收录的中文字符集不够全面，在遇到如繁体字的时候会出现解码错误。
        # 汉字字符集范围 gb2312 < gbk < gb18030
        # 将 gbk2312 替换为中文字符集更全面的 gb18030

        # 打开话要修改编码的大件，并得定原始编码
        try:
            with codecs.open(full_path, 'r', encoding='gb18030')as f:
                content = f.read()

            # 将内容重新编码为UTF-8格式
            with codecs.open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
                print(full_path, '替换为 utf-8 格式')
        except:
            failed_lst.append(full_path)
            print(full_path, '替换失败')

    if len(failed_lst) == 0:
            print("全部替换成功！")
    else:
        print('替换失败：')
        for path in failed_lst:
            print(path)



