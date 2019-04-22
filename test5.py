import os
path = "D:\\test\\PM2DT"
documents = os.listdir(path)
for document in documents:
    if os.path.exists(path + "\\"+document):
        if os.path.getsize(path +"\\"+document):
            print("hello world")

