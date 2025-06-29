import streamlit as st
from datetime import date
import pandas as pd




st.title("Search Campaign Deployer")
st.write("Converts Google Search campaign data into a batch csv file for rapid campaign creation.")





campaign_name = st.text_input("Enter campaign name")
st.write("")

budgetstrat_options = ["Maximise conversions"]

selected_budgettype = st.selectbox(
    "Budget Strategy:",
    budgetstrat_options
)
st.write("")

dailybudget = st.text_input("Enter daily budget (GBP)")
st.write("")

#BEGIN Date input columns
startdate1, enddate2= st.columns([0.8, 0.8])
with startdate1: start_date = st.date_input(
    "Select your campaign start date:",
    value=date.today(),
    key='d1'
)

with enddate2: end_date = st.date_input(
    "Select your campaign end date:",
    value=date.today(),
    key='d2'
)   
    
formatted_start = start_date.strftime("%m/%d/%Y")
formatted_end = end_date.strftime("%m/%d/%Y")
#END Date input columns
st.write("")
st.write("")




#Columns for Ad group name input
Adgroup1, Adgroup2,Adgroup3,Adgroup4= st.columns([0.8, 0.8,0.8,0.8])
with Adgroup1:
    
    group1name = st.text_area(
        "Paste Ad group 1 Name:",
        height=70,
        key='groupname1'
    ) 

with Adgroup2:
    
    group2name = st.text_area(
        "Paste Ad group 2 Name:",
        height=70,
        key='groupname2'
    ) 

with Adgroup3:
    
    group3name = st.text_area(
        "Paste Ad group 3 Name:",
        height=70,
        key='groupname3'
    )

with Adgroup4:
    
    group4name = st.text_area(
        "Paste Ad group 4 Name:",
        height=70,
        key='groupname4'
    )
#END columns for Ad group name input



group1keywordcolumn, group2keywordcolumn,group3keywordcolumn,group4keywordcolumn= st.columns([0.8, 0.8,0.8,0.8])

with group1keywordcolumn:
    
    group1keywords = st.text_area(
        "Paste Adgroup1 keywords:",
        height=200,
        key='col1'
    ) 

with group2keywordcolumn:
    group2keywords = st.text_area(
        "Paste Adgroup2 keywords:",
        height=200,
        key='col2'
    )

with group3keywordcolumn:
    group3keywords = st.text_area(
        "Paste Adgroup3 keywords:",
        height=200,
        key='col3'
    )

with group4keywordcolumn:
    group4keywords = st.text_area(
        "Paste Adgroup4 keywords:",
        height=200,
        key='col4'
    )


    #BEGIN Processing w pandas

mainkeywordlist=group1keywords.splitlines()+group2keywords.splitlines()+group3keywords.splitlines()+group4keywords.splitlines()

#create a csv file
    
if 'uploadersheet' not in st.session_state:
    st.session_state.uploadersheet = pd.DataFrame({
        'Campaign Name': [''],
        'Ad Group Name': [''],
        'Keyword': [''],
        'Budget': [''],
        'Budget Type': [''],
        'Start Date': [''],
        'End Date': [''],
        'Status': [''],
        'Match Type': [''],
        'Bid Strategy Type': [''],
        # Ads stuff
        'Campaign': [''],
        'Ad Group': [''],
        'Ad status': [''],
        'Ad type': [''],
        'Ad Number': [''],
        'Headline 1': [''],
        'Headline 2': [''],
        'Headline 3': [''],
        'Headline 4': [''],
        'Headline 5': [''],
        'Headline 6': [''],
        'Headline 7': [''],
        'Headline 8': [''],
        'Headline 9': [''],
        'Headline 10': [''],
        'Headline 11': [''],
        'Headline 12': [''],
        'Headline 13': [''],
        'Headline 14': [''],
        'Headline 15': [''],
        'Description 1': [''],
        'Description 2': [''],
        'Description 3': [''],
        'Description 4': [''],
        'Final URL': [''],
    })

df = st.session_state.uploadersheet


#print campaign name





#Ads section ------------------------------------------- 1
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Ads")    

Adgroupnameoptions = [group1name,group2name,group3name,group4name]

selected_adgroup = st.selectbox(
    "Adding to Ad Group:",
    Adgroupnameoptions
)
st.write("")

Ad1headlines, Ad2headlines,Ad3headlines= st.columns([0.8, 0.8,0.8])

with Ad1headlines:
    
    headlines1 = st.text_area(
        "Ad 1 Headlines:",
        height=200,
        key='Adcol1'
    ) 

with Ad2headlines:
    headlines2 = st.text_area(
        "Ad 2 Headlines:",
        height=200,
        key='Adcol2'
    )

with Ad3headlines:
    headlines3 = st.text_area(
        "Ad 3 Headlines:",
        height=200,
        key='Adcol3'
    )

st.write("") 
st.write("Desc. (Max 4 - Seperate each with a Fullstop)") 

#Desc i
Ad1Desccolumn1, Ad1Desccolumn2,Ad1Desccolumn3= st.columns([0.8, 0.8,0.8])

with Ad1Desccolumn1:
    
    Ad1desc = st.text_area(
        "Ad 1 Descriptions:",
        height=90,
        key='Desccol1'
    ) 

with Ad1Desccolumn2:
    Ad2desc = st.text_area(
        "Ad 2 Descriptions:",
        height=90,
        key='Desccol2'
    )

with Ad1Desccolumn3:
    Ad3desc = st.text_area(
        "Ad 3 Descriptions:",
        height=90,
        key='Desccol3'
    )


#URL Columns

st.write("Final URL")

Ad1URL, Ad2URL,Ad3URL= st.columns([0.8, 0.8,0.8])

with Ad1URL:
    
    url1 = st.text_area(
        "",
        height=68,
        key='url1'
    ) 

with Ad2URL:
    url2 = st.text_area(
        "",
        height=68,
        key='url2'
    )

with Ad3URL:
    url3 = st.text_area(
        "",
        height=68,
        key='url3'
    )    

#list variables for ads and descriptions
ad1headlinelist = headlines1.splitlines()
ad2headlinelist = headlines2.splitlines()
ad3headlinelist = headlines3.splitlines()
ad1descriptionlist = [s.strip() for s in Ad1desc.split('.') if s.strip()]
ad2descriptionlist = [s.strip() for s in Ad2desc.split('.') if s.strip()]
ad3descriptionlist = [s.strip() for s in Ad3desc.split('.') if s.strip()]










#Geenrate Campaign File button
if st.button("Generate Campaign File"):
    df = df.iloc[0:0]
    for i in range(len(mainkeywordlist)):
     df.loc[i,'Campaign Name'] = campaign_name

    #print Adgrp1 name
    #for i in range(len(group1keywords.split())):
    #   df.loc[i,'Ad Group Name'] = group1name

    #Keyords gen group 1 ---------------------
    keywords = group1keywords.splitlines()

    # Find the first empty row in 'Ad Group Name' column
    existing_rows = df['Ad Group Name'].notna().sum()
    start_index = existing_rows 

    for i, keyword in enumerate(keywords):
        df.loc[start_index + i, 'Ad Group Name'] = group1name
        df.loc[start_index + i, 'Keyword'] = keyword  # optional
    #Keyords gen group 1 Close ---------------------
        

    #Keyords gen group 2 ---------------------
    keywords = group2keywords.splitlines()

    # Find the first empty row in 'Ad Group Name' column
    existing_rows = df['Ad Group Name'].notna().sum()
    start_index = existing_rows

    for i, keyword in enumerate(keywords):
        df.loc[start_index + i, 'Ad Group Name'] = group2name
        df.loc[start_index + i, 'Keyword'] = keyword  # optional
    #Keyords gen group 2 Close ---------------------
        
    #Keyords gen group 3 ---------------------
    keywords = group3keywords.splitlines()

    # Find the first empty row in 'Ad Group Name' column
    existing_rows = df['Ad Group Name'].notna().sum()
    start_index = existing_rows

    for i, keyword in enumerate(keywords):
        df.loc[start_index + i, 'Ad Group Name'] = group3name
        df.loc[start_index + i, 'Keyword'] = keyword  # optional
    #Keyords gen group 3 Close ---------------------
        
    #Keyords gen group 4 ---------------------
    keywords = group4keywords.splitlines()

    # Find the first empty row in 'Ad Group Name' column
    existing_rows = df['Ad Group Name'].notna().sum()
    start_index = existing_rows

    for i, keyword in enumerate(keywords):
        df.loc[start_index + i, 'Ad Group Name'] = group4name
        df.loc[start_index + i, 'Keyword'] = keyword  # optional
    #Keyords gen group 4 Close ---------------------




    #Budget Column
    for i in range(len(mainkeywordlist)):
        df.loc[i,'Budget'] = dailybudget

    #Budget Type
    for i in range(len(mainkeywordlist)):
        df.loc[i,'Budget Type'] = 'Avg. Daily'

    #Start Date
    for i in range(len(mainkeywordlist)):
        df.loc[i,'Start Date'] = formatted_start

    #End Date
    for i in range(len(mainkeywordlist)):
        df.loc[i,'End Date'] = formatted_end

    #Status
    for i in range(len(mainkeywordlist)):
        df.loc[i,'Status'] = 'Enabled'

    #Match Type
    for i in range(len(mainkeywordlist)):
        df.loc[i,'Match Type'] = 'Phrase'

    #Bid Strategy Type
    for i in range(len(mainkeywordlist)):
        df.loc[i,'Bid Strategy Type'] = selected_budgettype 


    
    st.session_state.df = df
    st.write(st.session_state.df)

Adgroupstore = ['']















if st.button("Add Ad"):  # Adds or overwrites 3 rows for the Ad Group

    df = st.session_state.df

    # Find existing rows for this Ad Group
    existing_indices = df[df['Ad Group'] == selected_adgroup].index.tolist()

    if len(existing_indices) >= 3:
        # Overwrite the first 3 rows for that Ad Group
        for i in range(3):
            df.loc[existing_indices[i], 'Ad Group'] = selected_adgroup
            df.loc[existing_indices[i], 'Ad Number'] = i + 1

            #TEST - Adding Ad1 to the columns
            for idx in df[df['Ad Number'] == 1].index:
             for i, text in enumerate(ad1headlinelist):
              col = f'Headline {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Adding Ads to columns

            #TEST - Adding Ad2 to the columns
            for idx in df[df['Ad Number'] == 2].index:
             for i, text in enumerate(ad2headlinelist):
              col = f'Headline {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Adding Ads to columns
            
            #TEST - Adding Ad3 to the columns
            for idx in df[df['Ad Number'] == 3].index:
             for i, text in enumerate(ad3headlinelist):
              col = f'Headline {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Adding Ads to columns

            #Description Ad 1 
            for idx in df[df['Ad Number'] == 1].index:
             for i, text in enumerate(ad1descriptionlist):
              col = f'Description {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Desc

            #Description Ad 2 
            for idx in df[df['Ad Number'] == 2].index:
             for i, text in enumerate(ad2descriptionlist):
              col = f'Description {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Desc

            #Description Ad 3
            for idx in df[df['Ad Number'] == 3].index:
             for i, text in enumerate(ad3descriptionlist):
              col = f'Description {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Desc


            #URL Adding
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 1), 'Final URL'] = url1
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 2), 'Final URL'] = url2
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 3), 'Final URL'] = url3

        st.success(f"'{selected_adgroup}' already existed — rows overwritten.")

    else:
        # Append new rows
        existing_rows = df['Ad Group'].notna().sum()
        start_index = existing_rows

        for i in range(3):
            df.loc[start_index + i, 'Ad Group'] = selected_adgroup
            df.loc[start_index + i, 'Ad Number'] = i + 1

             #TEST - Adding Ad 1 to  columns
            for idx in df[df['Ad Number'] == 1].index:
             for i, text in enumerate(ad1headlinelist):
              col = f'Headline {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Adding Ads to columns

            #TEST - Adding Ad2 to the columns
            for idx in df[df['Ad Number'] == 2].index:
             for i, text in enumerate(ad2headlinelist):
              col = f'Headline {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Adding Ads to columns


            #TEST - Adding Ad3 to the columns
            for idx in df[df['Ad Number'] == 3].index:
             for i, text in enumerate(ad3headlinelist):
              col = f'Headline {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Adding Ads to columns

            #Description Ad 1 
            for idx in df[df['Ad Number'] == 1].index:
             for i, text in enumerate(ad1descriptionlist):
              col = f'Description {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Desc

            #Description Ad 2 
            for idx in df[df['Ad Number'] == 2].index:
             for i, text in enumerate(ad2descriptionlist):
              col = f'Description {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Desc

            #Description Ad 3
            
            for idx in df[df['Ad Number'] == 3].index:
             for i, text in enumerate(ad3descriptionlist):
              col = f'Description {i + 1}'
              if col in df.columns:
                df.at[idx, col] = text  #End Desc

            #URL Adding
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 1), 'Final URL'] = url1
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 2), 'Final URL'] = url2
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 3), 'Final URL'] = url3
            
            #Ad Status
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 1), 'Ad status'] = 'Enabled'
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 2), 'Ad status'] = 'Enabled'
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 3), 'Ad status'] = 'Enabled'

            #Ad Type
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 1), 'Ad type'] = 'Responsive Search Ad'
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 2), 'Ad type'] = 'Responsive Search Ad'
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 3), 'Ad type'] = 'Responsive Search Ad'

            #Ad Campaign
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 1), 'Campaign'] = campaign_name
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 2), 'Campaign'] = campaign_name
            df.loc[(df['Ad Group'] == selected_adgroup) & (df['Ad Number'] == 3), 'Campaign'] = campaign_name

            

        st.success(f"'{selected_adgroup}' added successfully.")

    # Update Adgroupstore
    if selected_adgroup not in Adgroupstore:
        Adgroupstore.append(selected_adgroup)

    # Show updated DataFrame
    st.write(df)



#AI Module
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')



if st.button("Test"):
   print 