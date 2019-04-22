import re
import os
from lxml import etree
import csv

citynames = []
def eachFile(path):
    documents = os.listdir(path)#遍历文件夹下所有文件夹及文件
    for document in documents:
        # subdocuments = os.listdir(path + document)#遍历子文件夹下所有文件夹及文件
        # for subdocument in subdocuments:
        #     print("*" * 30)
        #     print(subdocument)
        # print(document)
        citynameHtml = re.split("__", document)
        cityname = citynameHtml[0]
        citytimeHtml = citynameHtml[1]
        citytime = re.sub(".html",' ',citytimeHtml)
        # print(citytime)
        if  cityname not in citynames:
            citynames.append(cityname)
        readFile(document, cityname, citytime)
        # break


def readFile(document, cityname,citytime):#获取对应页面
        fopen = open( 'D:/test/PM2DT'+"/" + document, 'r',encoding='utf-8')  # r 代表read
        fileread = fopen.read()
        fopen.close()
        html = etree.HTML(fileread)
        csv_cityname = cityname
        csv_citytime = citytime
        parseFile(html,csv_cityname,csv_citytime)



def parseFile(html, csv_cityname, csv_citytime):#解析对应页面，并获得相应数据
    cityname = csv_cityname
    citytime = csv_citytime
    Value = [csv_citytime]
    Caption = ['Date']
    captions = html.xpath("(//div[@class='span1']//div[@class='caption']//text())")#获取名称
    for caption in captions:
        captionresult = re.sub("\n", ' ', caption)
        Caption.append(captionresult.strip())

    values = html.xpath("(//div[@class='span1']//div[@class='value']//text())")#得到的value值是一串的字符串，我们需要对字符串中的换行空白去掉
    #获取数据信息
    for value in values:
        valueresult = re.sub("\n", ' ', value)
            # print(valueresult.strip())
        Value.append(valueresult.strip())
    # print(Value)
    # else:
    #     print("the name of the city does't exit in the city list")
    writeCsv(Caption, Value, cityname)
    # print(Caption)
def writeCsv(Caption, Value, csv_cityname ):
    # print(Caption)
    if csv_cityname in citynames:
        # print(Caption)
        # if os.path.exists(csv_cityname + '.csv'):#基于上面的判断再进行，文件已经存在的操作
        if os.path.exists('D:/csv/' + csv_cityname + '.csv'):  # 基于上面的判断再进行，文件已经存在的操作
            with open('D:/csv/'+csv_cityname + '.csv', 'a', encoding = 'utf-8', newline='') as fp:#newline是用来控制空的行数的,将换行去掉
                writer = csv.writer(fp)
                writer.writerow( Value)

        if  not os.path.exists('D:/csv/' + csv_cityname + '.csv'):#判断是否存在该文件，如果不存在则新建一个
            # print(Caption)
            with open('D:/csv/'+csv_cityname + '.csv' , 'w+', encoding = 'utf-8', newline='') as fp:#newline是用来控制空的行数的,将换行去掉
                # 哪个值是你需要写入的字段
                #下面的Caption就是打印出来的内容，是需要写入的
                #没有写入表头，刚刚打开看了
                headers = Caption
                writer = csv.writer(fp)
                writer.writerow(headers)
                writer.writerow(Value)
                # print(Value)
                # line = Caption[0] + "," + Caption[1] + "," +  Caption[2] + "," +  Caption[3] + "," + \
                # Caption[4] + "," + Caption[5] + "," +  Caption[6] + "," +  Caption[7] + "," +  Caption[8]
                # fp.write(line)
                # fp.write('\n')

if __name__ == '__main__':
    path = 'D:\\test\\PM2DT' # refer root dir
    eachFile(path)






