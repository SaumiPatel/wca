import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration for better mobile view
st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide", initial_sidebar_state="expanded")

# Main page title
st.title("WhatsApp Chat Analyzer")

# Instructions for extracting WhatsApp chat files
with st.expander("How to extract WhatsApp chat for analysis", expanded=True):
    st.markdown("""
    ### For Android:
    1. Open WhatsApp > Go to the chat you want to analyze
    2. Click three dots on top right of the chat
    3. Press 'More' > 'Export chat'
    4. Choose 'Without Media'
    5. Extract the ZIP file if needed
    
    ### For iPhone:
    1. Open WhatsApp > Go to the chat you want to analyze
    2. Tap on the contact/group name at the top
    3. Scroll down and tap 'Export Chat'
    4. Choose 'Without Media'
    5. Extract the ZIP file if needed
    """)

# Sidebar configuration
st.sidebar.title("WhatsApp Chat Analyzer")

Phone_type = st.sidebar.radio(
        "Select your phone type",
        ('Android', 'Iphone'))
st.sidebar.title(Phone_type)




# Add file upload instructions in main area for mobile users
st.markdown("### Upload your WhatsApp chat file (.txt) in the sidebar")
st.markdown("If you're on mobile, tap the '>' icon at the top left to open the sidebar")

# Add a prominent button for mobile users
if st.button("Open Sidebar"):
    st.markdown("<style>div.row-widget.stButton > button {display: none;}</style>", unsafe_allow_html=True)
    st.sidebar.markdown("### 👈 Please upload your file here")

# File uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Choose a WhatsApp chat file (.txt)")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data,Phone_type)
   

    #fatch unique user
    user_list=df['user'].unique().tolist()
    if user_list=='group_notification':
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'overall')
    selected_user=st.sidebar.selectbox('show analysis',user_list)
    
    if st.sidebar.button("show Analysis"):

        num_messages,num_words,num_media,num_links=helper.fetch_stats(selected_user,df)

        #Stats Area
        st.title('Top Statistics')

        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header('Total Messages')
            st.title(num_messages)
        
        with col2:
            st.header('Total Words')
            st.title(num_words)

        with col3:
            st.header('Total Media Shared')
            st.title(num_media)
        
        with col4:
            st.header('Total Links Shared')
            st.title(num_links)

        #Timeline
        st.title('Monthly Timeline')
        timeline=helper.timeline(selected_user,df)
        fig,axis=plt.subplots()
        axis.plot(timeline['time'],timeline['message'],color='purple')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #Activity map
        st.title('Activity Map')
        col1,col2=st.columns(2)
       

        with col1:
            st.header("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user,df)
            fig,axis=plt.subplots()
            axis.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month=helper.month_activity_map(selected_user,df)
            fig,axis=plt.subplots()
            axis.bar(busy_month.index,busy_month.values,color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        
        #Weekly Activity Map
        st.title('Weekly Activity Map')
        user_heatmap=helper.activity_heatmap(selected_user,df)
        fig,axis=plt.subplots()
        axis=sns.heatmap(user_heatmap)
        plt.yticks(rotation='horizontal')
        st.pyplot(fig)




        #Finding thr busiest users in the group(Group)
        if selected_user=='overall':
            st.title('Most Busiest User')
            x,percentage=helper.most_busy_users(df)
            
            fig,axis=plt.subplots()
            col1,col2=st.columns(2)

            with col1:
                axis.bar(x.index,x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(percentage)

        
         

        #Most common words
        most_common_df=helper.most_common_words(selected_user,df)
        fig,axis=plt.subplots()
        axis.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title('Most Common Words')
        st.pyplot(fig)
        
        #Emoji Analysis
        emoji_df=helper.emoji_helper(selected_user,df).head()
        st.title('Emoji Analysis')
        col1,col2=st.columns(2)

        with col1:
            fig,axis=plt.subplots()
            axis.pie(emoji_df[1],labels=emoji_df[0],autopct='%0.2f')
            st.pyplot(fig)
        with col2:
            st.dataframe(emoji_df)
        
        #word Cloud
        df_wc=helper.creat_wordcloud(selected_user,df)
        fig,axis=plt.subplots()
        axis.imshow(df_wc)
        st.header('Word Cloud')
        st.pyplot(fig)

       