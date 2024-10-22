import os

duplicate_list = []
all_stuff = []
def compare_files(file1,  file2):
    with open(file1, 'r', errors="replace") as f1, open(file2, 'r', errors="replace") as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        if file1 != file2:
            if file1 not in duplicate_list:
                duplicate_list.append(file1)
            if file2 not in duplicate_list:
                duplicate_list.append(file2)

def search_all_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            all_stuff.append(os.path.join(dirpath, filename))

    for file_original in all_stuff:
        for file_duplicate in all_stuff:
            compare_files(file_original, file_duplicate)

# Example usage
search_all_files("C:/Users/radu0/OneDrive/Desktop/find_duplicate/")

print(all_stuff)

print(f"duplicates:")
print(duplicate_list)
