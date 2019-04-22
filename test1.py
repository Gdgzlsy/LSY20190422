import os
path ="D:\\"
documents = os.listdir(path)[1:2]
for document in documents:
    # print(document)
    subdocuments = os.listdir(path+document)
    # print(subdocuments)
    for subdocument in subdocuments:
        fopen = open('D:\AppServ'+'\\' + subdocument, 'r')  # r 代表read
        fileread = fopen.read()
        fopen.close()
        print(fileread)
        # print(subdocument)