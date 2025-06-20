try:
    file1=open("sample.txt","r")
    read_file=file1.read()
    print(read_file)
    file1.close()
except FileNotFoundError:
    print("Error: File sample.txt was not Found")
