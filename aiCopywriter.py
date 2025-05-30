from openai import OpenAI
import pandas as pd 
import streamlit as st

client = OpenAI(api_key=st.secrets["openai_api_key"])
authcode = st.secrets["authcode"]

st.subheader("MPG - Email Helper")
st.markdown("Instructions: Select an email reference from the bank - Provide context (objective) - Set the tone - Generate")

sheet_url = st.secrets["sheet_one_url"] #reference sheet file

df = pd.read_csv(sheet_url)
st.markdown('Email Bank Preview: [Update](https://docs.google.com/spreadsheets/d/1Ojp-0Gm-8-CKC2QdqbWOMjkCFIqhppx3nxQBeMSGYTQ/edit?gid=0#gid=0)')
st.dataframe(df, height=150)

reference_list = df['Email_Number'].tolist()

#User Input areas
st.subheader("Generate a new email:")

objective=st.text_input("Describe the emails objective:")

tone=st.text_input("Enter the general tone (Optional):")
default_tone = 'Match Refererence'

reference_emailselection = st.selectbox(
    "Reference Email Number",
    reference_list
    )

#end user input areas
reference_content = df.loc[df['Email_Number'] == reference_emailselection, 'Body']
reference_content = reference_content.iloc[0]

if tone == '':
  prompt = 'Here is the objective: ' + objective + ' \n \n .And here is the reference email content: \n \n ' + reference_content

else:
   prompt = 'Here is the objective: ' + objective + ' \n \n .And here is the reference email content: \n \n ' + reference_content + ' \n\n and here is the tone: ' + tone


if st.button("Generate Email"):

   if(objective==''):
    st.write("Error: Objective is blank")

   else: 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an expert event marketing email copywriter. Working for a marketing agency. You are given a reference email with an objective, and need to create a new one using similar tone and structure."},
                   {"role": "user", "content": prompt}],
        temperature=0.7,
    )
    output = response.choices[0].message.content
    st.text_area("Output", output, height=500)