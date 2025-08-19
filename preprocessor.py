import re
import pandas as pd


def preprocess(data,phone_type):
   
    
    
    if phone_type=='Android':
        pattern=r"\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s(?:AM|PM)\s-\s"
    if phone_type=='Iphone':
        pattern=r"\[\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}:\d{2}\s(?:AM|PM)\]\s"
    message=re.split(pattern,data)[2:]
    dates=re.findall(pattern,data)[1:]

    if phone_type=='Android':
        Format='%m/%d/%y, %I:%M %p -'
    if phone_type=='Iphone':
        Format='[%d/%m/%y, %I:%M:%S %p]'

    df=pd.DataFrame({'user_message':message,'message_date':dates})
    df['message_date']=pd.to_datetime(df['message_date'],format=Format,exact=False)
    df.rename(columns={'message_date':'dates'},inplace=True)
    users=[]
    message=[]
    for message1 in df['user_message']:
        entry=re.split(r'([\w\W]+?):\s', message1)
        if entry[1:]:
            users.append(entry[1])
            message.append(entry[2])
        else:
         users.append('group_notification')
         message.append(entry[0])
    df['user']=users
    df['message']=message
    df.drop(columns=['user_message'],inplace=True)

    df['year']=df['dates'].dt.year
    df['month']=df['dates'].dt.month_name()
    df['day']=df['dates'].dt.day
    df['day_name']=df['dates'].dt.day_name()
    df['hour']=df['dates'].dt.hour
    df['minutes']=df['dates'].dt.minute

    period=[]
    for hour in df[['day_name','hour']]['hour']:
        if hour==23:
            period.append(str(hour)+'-'+str('00'))
        elif hour==0:
            period.append(str('00')+'-'+str(hour+1))
        else:
            period.append(str(hour)+'-'+str(hour+1))
    df['period']=period
    return df
