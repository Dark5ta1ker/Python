import filecmp

def compare_folders(folder1, folder2):
    comparison = filecmp.dircmp(folder1, folder2)
    print("Файлы, отличающиеся:", comparison.diff_files)
    print("Файлы только в папке 1:", comparison.left_only)
    print("Файлы только в папке 2:", comparison.right_only)

compare_folders(r'F:\\', r'E:\\Мама')