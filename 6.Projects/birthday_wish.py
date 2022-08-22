# pip install pandas
# pip install xlrd
#pip install openpyxl
import datetime
import pandas as pd
def sendEmail(to,sub,msg):
    print(f'Email to {to} sent with Subject :{sub} and message {msg}')
    pass
if __name__ == '__main__':
    df=pd.read_excel("2.medium/data.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearnow=str(2021)
    # yearnow=datetime.datetime.now().strftime("%Y")
    writeInt=[]
    for index,item in df.iterrows():#function which give index and items
        # print(index,item['Birthday']
        bday=item['Birthday']
        if today==bday and yearnow not in str(item['Year']):
            sendEmail(item['Name'],"Happy Birthday",item['Message'])
            writeInt.append(index)
            print(writeInt)    
            for i in writeInt:
                yr=df.loc[i,'Year']
                # print(i,yr)
                df.loc[i,'Year']=str(yr)+','+str(yearnow)
                print(df)
                df.to_excel('data.xlsx')
                print('Finish...')



    
    