from urlextract import URLExtract
from wordcloud import WordCloud
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import emoji


def fetch_stats(selected_user,df):
    if selected_user!='overall':
        df=df[df['user']==selected_user]
    
    number_message=df.shape[0]
    number_words=[]
    for message in df['message']:
        number_words.extend(message.split())
    number_media=df[df['message']=='<Media omitted>\n'].shape[0]
    extract=URLExtract()
    link=[]
    for message in df['message']:
        link.extend(extract.find_urls(message))
    return number_message,len(number_words),number_media,len(link)

def most_busy_users(df):
    activity=df['user'].value_counts().head()
    user_percentage=round((df['user'].value_counts()/df.shape[0])*100).reset_index().rename(columns={'index':'User','user':'Percentage'})
    return activity,user_percentage

def creat_wordcloud(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    
    temp= df[df['message']!='<Media omitted>\n']
    temp=temp[temp['user']!='group_notification']
    temp  
    def remove_stopwords(message):
        words=[]
        for message in temp['message']:
            for word in message.lower().split():
                if word  not in stopwords.words('english'):
                    words.append(word)  
        return ' '.join(words)
    
    
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message']=temp['message'].apply(remove_stopwords)
    df_wc=wc.generate(temp['message'].str.cat(sep=' '))
   
    return df_wc

def most_common_words(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    words=[]
    temp= df[df['message']!='<Media omitted>\n']
    temp=temp[temp['user']!='group_notification']
    temp    
    for message in temp['message']:
        for word in message.lower().split():
            if word  not in stopwords.words('english'):
                words.append(word)
    return_df=pd.DataFrame(Counter(words).most_common(20))
    return return_df

def emoji_helper(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    emojies=[]
    for message in df['message']:
        emojies.extend([c for c in message if c in emoji.EMOJI_DATA])
    return_df=pd.DataFrame(Counter(emojies).most_common(20))
    return return_df

def timeline(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    df['num_month']=df['dates'].dt.month
    timeline=df.groupby(['year','num_month','month']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] +'-'+ str(timeline['year'][i]))
    timeline['time']=time
    return timeline

def week_activity_map(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    
    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    
    return df['month'].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]
    user_heatmap=df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)
    return user_heatmap



    