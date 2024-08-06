import os
import re

# 文件夹路径，当前目录
folder_path = '.'  # 设置为当前目录

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    # 去掉文件名两端的空白字符
    filename = filename.strip()
    
    # 匹配文件名的模式，考虑可能的空格
    match = re.match(r'freecompress-罗马书2章第(\d+)讲\s*\.mp3', filename)
    if match:
        # 提取讲的编号
        lecture_number = match.group(1)
        # 生成新的文件名
        new_filename = f'{lecture_number}.mp3'
        # 旧文件的完整路径
        old_file_path = os.path.join(folder_path, filename)
        # 新文件的完整路径
        new_file_path = os.path.join(folder_path, new_filename)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f'Renamed {filename} to {new_filename}')
    else:
        print(f'Filename does not match pattern: {filename}')

print('重命名完成')
