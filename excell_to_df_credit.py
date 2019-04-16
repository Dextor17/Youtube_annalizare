import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('/home/prachi/Downloads/credit_youtube.xlsx', sheet_name='Sheet1')

print("Column headings:")
print(df.columns)
print(df)

Total1 = df['xoTyrdT9SZI'].sum()
print(Total1)
rate1=(Total1/50)*5
print(rate1)


Total2 = df['oylHRgBDfNc'].sum()
print(Total2)
rate2 = (Total2/50)*5
print(rate2)

Total3 = df['wRoABkgPocI'].sum()
print(Total3)
rate3 = (Total3/50)*5
print(rate3)

Total4 = df['5GDTIUVlHB8'].sum()
print(Total4)
rate4 = (Total4/50)*5
print(rate4)


Total5 = df['qTR8QnYXHvQ'].sum()
print(Total5)
rate5 = (Total5/50)*5
print(rate5)

list=[rate1,rate2,rate3,rate4,rate5]
print(list)

for i in list :
    if (i<=1 and i>=0):
        print("\033[1;32;40m Bright Green  \n")
    if (i>1 and i<=1.5):
        print("\033[1;37;40m theek thak  \n")
    if(i>1.5 and i<=2):
        print("\033[1;30;41m thoda theek hai hai  \n")
    if(i>2 and i<=2.5):
        print("\033[1;30;42m chalo dekhlo  \n")
    if(i>2.5 and i<=3):
        print("\033[1;30;43m good  \n")
    if(i>3 and i<=3.5):
        print("\033[1;30;44m nice  \n")
    if(i>3.5 and i<=4):
        print("\033[1;30;43m very good  \n")
    if (i>4 and i<=4.5):
        print("\033[1;30;43m excellent  \n")
    if(i>4.5 and i<=5):
        print("\033[1;30;43m mindblowing  \n")







