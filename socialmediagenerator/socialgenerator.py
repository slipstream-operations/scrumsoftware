import pandas as pd 
import streamlit as st 
from openai import OpenAI
import time


authcode = st.secrets["authcode"]
system_prmpt = st.secrets["system_prmt"]

st.write('Social media tool - Testing')

sheet_url = st.secrets["sheet_one_url"] #reference sheet file
example_utm = '?utm_source=instagram&utm_medium=social&utm_campaign=event&utm_content=&utm_term=agenda'


api_key= st.text_input("Org. API Key:")
client = OpenAI(api_key=api_key)

st.markdown('Social media file preview: [Update here](https://docs.google.com/spreadsheets/d/1POZkt9Xboo3YlIjBmYL0HliURqAO4w-U2gehEX1o60A/edit?gid=0#gid=0')

df = pd.read_csv(sheet_url)

st.write(df)

event_name=st.text_input("Enter the event name:")
key_details=st.text_area("Enter key details and info about the event (to be used in the social posts):")
event_urls=st.text_area("Enter key urls to be used in the social posts:")

#end UI
reference_list = df['Reference Post'].tolist()

if st.button("Generate Social Media Campaign"):
    
    #for X.com posts
    for i, val in enumerate(reference_list):
        prompt = 'Generate one social post for the social media platform X ,for our clients event: ' + event_name + '\n\n use this other post we made as a reference when creating this new one,but only reference the style and tone. The events are otherwise unrelated: \n\n' + reference_list[i] + ' \n\n Consider the character limits for the platform. \n\n . apply the event urls given to you based on the post (1 url per post). Here are the event urls: ' + event_urls + ' \n\n and here are is an example utm structure to follow: ' + example_utm + ' \n\n Format the utm according to platform and campaign, but keep the same structure'

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_prmpt},
                   {"role": "user", "content": prompt}],
        temperature=0.7,
    )
        output = response.choices[0].message.content
        df.loc[i,'Generated X'] = output

        time.sleep(0.5)


    #for instagram posts
    for i, val in enumerate(reference_list):
        prompt = 'Generate one social post for the social media platform: Instagram ,for our clients event: ' + event_name + '\n\n use this other post we made as a reference when creating this new one,but only reference the style and tone. The events are otherwise unrelated: \n\n' + reference_list[i] + ' \n\n Consider the character limits for the platform. \n\n . apply the event urls given to you based on the post (1 url per post). Here are the event urls: ' + event_urls + ' \n\n and here are is an example utm structure to follow: ' + example_utm + ' \n\n Format the utm according to platform and campaign, but keep the same structure'

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_prmpt},
                   {"role": "user", "content": prompt}],
        temperature=0.7,
    )
        output = response.choices[0].message.content
        df.loc[i,'Generated Instagram'] = output

        
        time.sleep(0.5)

    st.dataframe(df, height=600, use_container_width=True)




        
      




