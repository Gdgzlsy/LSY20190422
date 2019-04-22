import csv
test = '122'
with open('D:/csv/'+test+'.csv','w') as fp:
    writer = csv.writer(fp)
    writer.writerow(['1','2','3'])
