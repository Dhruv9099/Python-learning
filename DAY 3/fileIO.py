# creating file
f = open("Myfile.txt", "w")
print(f"The file is {f.name}")

# writing a file and creating
a = "Dhruv MAisuria"
with open("file.txt", "w") as f:
    f.write(a)

fp = open("file.txt", "w")
fp.write(a)
fp.close()

# Reading To a File
f = open('file.txt', 'r')
content = f.read()


with open("file.txt", "r") as f:
    s = f.read()
    print(a)

# append to add txt  in the existing file
    with open("file.txt", "w")as f:
        f.write("DHRUV MAISURIA WELCOME")
        f.write(a)


#close Files
        f = open('myfile.txt',"r")
        f.close()

# Delete a File
# Need to import os module
import os
os.remove("myfile.txt")
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
# The file does not exist
# Delete Folder
os.rmdir("myfolder") # You can only remove empty folders.