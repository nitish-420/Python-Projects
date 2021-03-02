# by Nitish Bhardwaj

import smtplib, ssl ,getpass
import pandas as pd
from datetime import datetime as dt

sender_email = "######@gmail.com"
# password = getpass.getpass(prompt='Password: ', stream=None)  #use this to get input which is hidden in console
password="########"

message = """\
Subject: Hi there

Here enter what you want to send in you own words."""


def sendEmail(receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__=='__main__':
    data=pd.read_excel("bday_data.xlsx")
    dm=dt.now().strftime("%d-%m")
    yr=dt.now().strftime("%Y")

    new=[]
    for index , item in data.iterrows():
        bday=item['Bday'].strftime("%d-%m") 
        if (dm == bday) and yr not in str(item['Year']):
            sendEmail(item['EmailId'])
            new.append(index)
            year=data.loc[index,'Year']
            data.loc[index,'Year']=str(year) + ',' + str(yr)            
    data.to_excel('bday_data.xlsx',index=False)