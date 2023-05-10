file_size = int(input("File size: "))
no = int(input("File number: "))
total_file_size = file_size * no
memory = int(input("Memory size: "))

if total_file_size <= memory:
    print("Storage available!")
else:
    print("Required more storage")