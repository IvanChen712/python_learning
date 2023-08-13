import os


def find_files_with_string(root_path, target_string):
    for foldername, subfolders, filenames in os.walk(root_path):
        for filename in filenames:
            if target_string in filename:
                relative_path = os.path.relpath(os.path.join(foldername, filename), root_path)
                print("Found:", relative_path)


if __name__ == "__main__":
    search_root = r"C:\Users\Chen Yi Fan\Desktop\codes\Yifan"
    # search_root = os.getcwd()  # 当前目录作为搜索的根目录
    find_files_with_string(search_root, "md")
