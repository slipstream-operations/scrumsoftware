from openai import OpenAI
import pandas as pd 
import streamlit as st

hide_github_style = """
    <style>
        [data-testid="stToolbar"] { visibility: hidden; height: 0; position: fixed; }
    </style>
"""

st.markdown(hide_github_style, unsafe_allow_html=True)
#------------------------------------------------------

client = OpenAI(api_key=st.secrets["openai_api_key"])
authcode = st.secrets["authcode"]

st.image("Images/logo.jpeg", width=100)
st.subheader("MPG - Email Helper")
st.markdown("Generate new email copy using previous reference material.")
st.markdown("**Instructions:** State an objective (context) - Set the tone - Select a reference - Generate.")

sheet_url = st.secrets["sheet_one_url"] #reference sheet file
platformlist = ['Adestra','Hubspot','Pardot','Sailthru']

df = pd.read_csv(sheet_url)
st.markdown('Email Bank Preview: [Update the email bank here.](https://docs.google.com/spreadsheets/d/1Ojp-0Gm-8-CKC2QdqbWOMjkCFIqhppx3nxQBeMSGYTQ/edit?gid=0#gid=0)')
st.dataframe(df, height=150)

reference_list = df['Email_Number'].tolist()

#User Input areas
st.subheader("Generate a new email:")

objective=st.text_input("Describe the emails objective:")

tone=st.text_input("Enter the general tone (Optional):")
default_tone = 'Match Refererence'

reference_emailselection = st.selectbox(
    "Reference Email Number / Identifier:",
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
    st.session_state.email_output_stored = output #saved the output in session state

if 'email_output_stored' in st.session_state:
     st.text_area("Result:", st.session_state.email_output_stored, height=500)
     st.session_state.output_state = 1 #to signal an output by the AI/LLM has been generated at least once


#Area loaded only after initial email is generated
if 'output_state' in st.session_state and int(st.session_state.output_state)>0:
   st.write('')
   st.write('Construct HTML version (Optional):')
   selected_platform = st.selectbox("Select Platform:",
                platformlist)
   
   html_prompt = 'Generate a html version of the provided email: \n\n' + st.session_state.email_output_stored + '\n\n to set it up in this email platform: ' + selected_platform

   if st.button("Generate HTML Version"):
      response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an event marketer and are given email copy to setup in a mentioned email platform. To do this you need to convert the email to a html version, compatible with the email platform provided to you."},
                   {"role": "user", "content": html_prompt}],
        temperature=0.7,
    )
      st.session_state.html_output = response.choices[0].message.content
   

if 'html_output' in st.session_state:
     st.text_area("Result:", st.session_state.html_output, height=500)
   




