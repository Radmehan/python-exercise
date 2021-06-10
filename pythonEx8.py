import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(file) as f:
        fileList=f.read().split("\n")

    for file in files:
        if file not in fileList:
            os.rename(file,file.capitalize())

    if os.path.splitext(file)[1]==format:
        os.rename(file,f"{i}{format}")
        i+=1
soldier(r"C:\Users\MD RAFSAN\Desktop\testing",r"C:\Users\MD RAFSAN\Desktop\others\Python Exercise\exe.txt",".png")
