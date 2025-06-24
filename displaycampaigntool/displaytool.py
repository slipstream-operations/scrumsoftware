import streamlit as st 
import pandas as pd 

#campaign template keys
ad_campaign_template = {
    "Campaign": [''],
    "Campaign Type": [''],
    "Networks": [''],
    "Budget": [''],
    "Budget type": [''],
    "Standard conversion goals": [''],
    "Languages": [''],
    "Bid Strategy Type": [''],
    "Bid Strategy Name": [''],
    "Start Date": [''],
    "End Date": [''],
    "Ad rotation": [''],
    "Targeting method": [''],
    "Exclusion method": [''],
    "Audience targeting": [''],
    "Flexible Reach": [''],
    "Ad Group": [''],
    "Max CPC": [''],
    "Max CPM": [''],
    "Target CPV": [''],
    "Percent CPC": [''],
    "Target CPM": [''],
    "Display Network Custom Bid Type": [''],
    "Optimized targeting": [''],
    "Strict age and gender targeting": [''],
    "Ad Group Type": [''],
    "Custom audience segments": [''],
    "ID": [''],
    "Audience segment": [''],
    "Bid Modifier": [''],
    "Final URL": [''],
    "Final mobile URL": [''],
    "Location": [''],
    "Reach": [''],
    "Radius": [''],
    "Ad type": [''],
    "Ad Name": [''],
    "Image Size": [''],
    "Display URL": [''],
    "Device Preference": [''],
    "Headline 1": [''],
    "Headline 2": [''],
    "Headline 3": [''],
    "Headline 4": [''],
    "Headline 5": [''],
    "Long headline": [''],
    "Description 1": [''],
    "Description 2": [''],
    "Description 3": [''],
    "Description 4": [''],
    "Description 5": [''],
    "Business name": [''],
    "Call to action": [''],
    "Allow flexible color": [''],
    "Use asset enhancements": [''],
    "Use auto generated video": [''],
    "Ad formats": [''],
    "Campaign Status": [''],
    "Ad Group Status": ['']
}

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(ad_campaign_template)
    st.session_state.df=pd.concat([st.session_state.df]*120,ignore_index=True)
    st.write('Firs time')

if st.button("check sessions"):

    if "df" in st.session_state:
        st.write('df in session state')


#program code
#Adding campaign data to the df
st.write("Testing")
network_box_options = ['Dispay Network','None']
bid_strategy_options = ['Maximize conversions']
audience_target_options = ['Audience segments']

campaign_name=st.text_input("Enter the campaign name")
network=st.selectbox("Select Network",network_box_options)
bid_strategy=st.selectbox("Select Bid Strategy", bid_strategy_options)
audience_targeting_selection = st.selectbox("Audience Targeting Options:",audience_target_options)

start_date=st.date_input("Select Start Date:")
end_date=st.date_input("Select End Date:")

if st.button("Add Campaign Data"):
    
    free_row=st.session_state.df[st.session_state.df['Campaign'] == ''].index[0]
    df = st.session_state.df

    df.loc[free_row,'Campaign'] = campaign_name
    df.loc[free_row,'Networks'] = network
    df.loc[free_row,'Bid Strategy Type'] = bid_strategy
    df.loc[free_row,'Start Date'] = start_date
    df.loc[free_row,'End Date']= end_date
    df.loc[free_row,'Standard conversion goals'] = 'Account-level'
    df.loc[free_row,'Targeting method'] = 'Location of presence'
    df.loc[free_row,'Audience targeting'] = audience_targeting_selection
    df.loc[free_row,'Campaign Status'] = 'Paused'

    st.session_state.df =df
    

#Adding Ad groups and custom audience segments to the df
st.write("")
st.write("")
st.write("")    
st.write("")    
st.write("") 
filt=st.session_state.df['Campaign'] != ''
current_campaigns = list(set(st.session_state.df.loc[filt,'Campaign'].tolist()))
st.write("Ad Groups and Custom Audience Segments")

adgroupname=st.text_input("Ad Group Name")
audience_segment = st.text_input("Custom Audience Segment Name*")
selected_campaign=st.selectbox("Add to campaign:",current_campaigns)


if st.button('Add Ad Group and Audience Segment'):
    free_row = st.session_state.df[st.session_state.df['Campaign']==''].index[0]
    df = st.session_state.df
    df.loc[free_row,'Campaign'] = selected_campaign
    df.loc[free_row,'Ad Group'] = adgroupname
    df.loc[free_row,'Audience segment'] = audience_segment
    st.write(free_row)
    st.session_state.df =df


#store a list of all current ad groups to a variable 
filt =  st.session_state.df['Ad Group'] != ''
adgroup_list = st.session_state.df.loc[filt,'Ad Group'].tolist()
cta_options = ['Learn more']




#Adding responsive ads to the df
st.write("")
st.write("")
st.write("")    
st.write("")    
st.write("") 
st.write("Add Responsive Display Ads")
selected_adgroup = st.selectbox("Adding to which ad group:", adgroup_list)
responsive_headline1 = st.text_input("Ad Headline 1:", key = 'r1')
responsive_headline2 = st.text_input("Ad Headline 2:", key ='r2')
responsive_headline3 = st.text_input("Ad Headline 3:", key ='r3')
responsive_headline4 = st.text_input("Ad Headline 4:", key = 'r4')
responsive_headline5 = st.text_input("Ad Headline 5:", key ='r5')
long_headline = st.text_input("Long Headline:",key='l1')
ad_type = 'Responsive display ad'
ad_format = 'All formats'

description1 = st.text_input("Desc. 1:", key = 'd1')
description2 = st.text_input("Desc. 2:", key = 'd2')
description3 = st.text_input("Desc. 3:", key = 'd3')
description4 = st.text_input("Desc. 4:", key = 'd4')
description5 = st.text_input("Desc. 5:", key = 'd5')


final_url = st.text_input("Final URL:")
cta_selection = st.selectbox("CTA:",cta_options)



if st.button("Add Responsive Ad Data"):
    
    free_row=st.session_state.df[st.session_state.df['Campaign'] == ''].index[0]
    df = st.session_state.df
    df.loc[free_row,'Campaign'] = campaign_name
    df.loc[free_row,'Ad type'] = ad_type
    df.loc[free_row,'Headline 1'] = responsive_headline1
    df.loc[free_row,'Headline 2'] = responsive_headline2
    df.loc[free_row,'Headline 3'] = responsive_headline3
    df.loc[free_row,'Headline 4'] = responsive_headline4
    df.loc[free_row,'Headline 5'] = responsive_headline5
    df.loc[long_headline,'Long headline'] = long_headline
    df.loc[long_headline,'Call to Action'] = cta_selection

    df.loc[free_row,'Description 1'] = description1
    df.loc[free_row,'Description 2'] = description2
    df.loc[free_row,'Description 3'] = description3
    df.loc[free_row,'Description 4'] = description4
    df.loc[free_row,'Description 5'] = description5

    df.loc[free_row,'Ad formats'] = ad_format


if st.button('Test'):
    
    st.write(adgroup_list)





st.write(st.session_state.df)

#ad group selection for the responsive display ads

#left 
#Add description fields for the ads 
#Add image uploads 