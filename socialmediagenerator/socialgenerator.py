import pandas as pd 
import streamlit as st 
from openai import OpenAI
import time

client = OpenAI(api_key=st.secrets["openai_api_key"])
authcode = st.secrets["authcode"]
system_prmpt = st.secrets["system_prmt"]

st.write('Social media tool')

sheet_url = st.secrets["sheet_one_url"] #reference sheet file
example_x_utm = 'x'
example_instagram_utm = 'x'
example_linkedin_utm = 'x'

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
        prompt = 'Generate one social post for the social media platform X ,for our clients event: ' + event_name + '\n\n use this other post we made as a reference when creating this new one only reference the style and tone. The events are otherwise unrelated: \n\n' + reference_list[i] + ' \n\n Consider the character limits for each platform.'

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_prmpt},
                   {"role": "user", "content": prompt}],
        temperature=0.7,
    )
        output = response.choices[0].message.content
        df.loc[i,'Generated X'] = output

        st.write(df)
        time.sleep(1)

        



#Do Next: Add UTM examples as variables. Adjust prompt accordingly and test 

        
      




