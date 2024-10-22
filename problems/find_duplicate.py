import os

duplicateList = []
allStuff = []
def compare_files(file1,  file2):
    with open(file1, 'r', errors="replace") as f1, open(file2, 'r', errors="replace") as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        if file1 != file2:
            if file1 not in duplicateList:
                duplicateList.append(file1)
            if file2 not in duplicateList:
                duplicateList.append(file2)

def search_all_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            allStuff.append(os.path.join(dirpath, filename))

    for fileOriginal in allStuff:
        for fileDuplicate in allStuff:
            compare_files(fileOriginal, fileDuplicate)

# Example usage
search_all_files("C:/Users/radu0/OneDrive/Desktop/find_duplicate/")

print(allStuff)

print("duplicates:")
print(duplicateList)
