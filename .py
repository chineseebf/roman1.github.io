import os

# 设置文件夹路径
folder_path = r'D:\克隆\roman1'

# 确保路径存在
if not os.path.exists(folder_path):
    print(f"Path not found: {folder_path}")
else:
    # 切换到目标目录
    os.chdir(folder_path)

    # 获取文件列表并按文件名排序
    files = [f for f in os.listdir(folder_path) if f.startswith('freecompress-罗马书2章第') and f.endswith('.mp3')]
    files.sort()

    # 重命名文件
    for index, file in enumerate(files, start=1):
        old_name = file
        new_name = f"{index}.mp3"
        
        if old_name != new_name:
            os.rename(old_name, new_name)
            print(f"Renamed '{old_name}' to '{new_name}'")
        else:
            print(f"Skipping '{old_name}' as it is already named correctly")

    print("Renaming complete.")
