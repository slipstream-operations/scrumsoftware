import pandas as pd
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["openai_api_key"])
authcode = st.secrets["authcode"]
system_prmt = st.secrets["system_prmt"]
user_prmt = st.secrets["user_prmt"]

st.image("Images/logo.jpeg", width=100)

st.subheader("MPG - Encoding Corrector")
st.markdown("Automatically detects and corrects encoding errors in a provided list.")
st.markdown("**Instructions:** Paste a list containing encoding errors below and click **Run**.")

user_data = st.text_area("Split by line",height = 200)
user_datalist = user_data.splitlines() #list of user entries
final_user_prmt = user_prmt + '\n\n' + '\n'.join(user_datalist)

if st.button('Run'):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":system_prmt },
                   {"role": "user", "content": final_user_prmt}],
        temperature=0.7,
    )
    output = response.choices[0].message.content
    st.session_state.outputlist = output.splitlines()

    sheet_file = {'Original':[''],
                'Corrected':['']}

    df = pd.DataFrame(sheet_file) #prep the dataframe

    for i, val in enumerate(user_datalist):
        df.loc[i,'Original'] = user_datalist[i]

    
    if "outputlist" in st.session_state:
        corrected_list = st.session_state.outputlist

    for c, val in enumerate(corrected_list):
        df.loc[c,'Corrected'] = corrected_list[c]

    st.write(df)

    corrected_data = df.to_csv(index=False)

    st.download_button(
    label="📥 Download CSV",
    data=corrected_data,
    file_name="corrected_data.csv",
    mime="text/csv"
)










   


