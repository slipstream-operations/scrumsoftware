import streamlit as st 
import pandas as pd 


#functions

#headline character limit enforcer

def charlimit(variable,max_length):
    headline = variable
    length_string = str(max_length)

    if len(headline)> max_length:
        warning =st.warning("Headline exceeds max character limit of " + length_string + " characters")

        return warning
    



#end functions


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
    
    "Final mobile URL": [''],
    "Location": [''],
    "Reach": [''],
    "Radius": [''],
    "Ad type": [''],
    "Ad Name": [''],
    "Image": [''],
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
    "Final URL": [''],
    "Business name": [''],
    "Call to action": [''],
    "Allow flexible color": [''],
    "Use asset enhancements": [''],
    "Use auto generated video": [''],
    "Ad formats": [''],
    "Campaign Status": [''],
    "Ad Group Status": [''],
    "Logo 1":[''],
    "Logo 2":[''],
    "Logo 3":[''],
    "Logo 4":[''],
    "Logo 5":[''],
    "Image 1":[''],
    "Image 2":[''],
    "Image 3":[''],
    "Image 4":[''],
    "Image 5":[''],

}

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(ad_campaign_template)
    st.session_state.df=pd.concat([st.session_state.df]*120,ignore_index=True)
    

#if st.button("check sessions"):

   # if "df" in st.session_state:
  #      st.write('df in session state')


#program code
#Adding campaign data to the df
st.title    ("MPG - Display Campaign Creator")
network_box_options = ['Dispay Network','None']
bid_strategy_options = ['Maximize conversions']
audience_target_options = ['Audience segments']

campaign_name=st.text_input("Enter the campaign name")
network=st.selectbox("Select Network... *Recommended to use a network for display campaigns*",network_box_options)
bid_strategy=st.selectbox("Select Bid Strategy", bid_strategy_options)
audience_targeting_selection = st.selectbox("Audience Targeting Options:",audience_target_options)

start_date=st.date_input("Select Start Date:")
end_date=st.date_input("Select End Date:")

daily_budget = st.text_input("Enter Daily Budget")

business_name = st.text_input("Enter Business Name:")

#location targeting

major_cities = [
    # United States
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
    "San Francisco", "Columbus", "Fort Worth", "Indianapolis", "Charlotte",
    "Seattle", "Denver", "Washington", "Boston", "Nashville", "Detroit",
    "Portland", "Las Vegas", "Miami", "Atlanta",
    
    # Europe
    "London", "Paris", "Berlin", "Madrid", "Rome", "Milan", "Barcelona",
    "Amsterdam", "Brussels", "Vienna", "Warsaw", "Budapest", "Prague",
    "Stockholm", "Copenhagen", "Dublin", "Athens", "Lisbon", "Zurich",
    "Oslo", "Frankfurt", "Munich", "Hamburg",
    
    # Asia
    "Tokyo", "Osaka", "Seoul", "Beijing", "Shanghai", "Hong Kong", "Singapore",
    "Bangkok", "Kuala Lumpur", "Jakarta", "Manila", "Mumbai", "Delhi",
    "Bangalore", "Hyderabad", "Chennai", "Ho Chi Minh City", "Hanoi", "Taipei",
    "Dubai", "Abu Dhabi", "Riyadh", "Jeddah"
]


location_list = [
    "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", 
    "Antigua and Barbuda", "Argentina", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", 
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", 
    "Bosnia and Herzegovina", "Botswana", "Brazil", "British Virgin Islands", "Brunei Darussalam", 
    "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", 
    "Central African Republic", "Chad", "Chile", "China", "Hong Kong", "Taiwan", "Christmas Island", 
    "Cocos Islands", "Colombia", "Comoros", "Congo-Brazzaville", "Congo-Kinshasa", "Cook Islands", 
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", 
    "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", 
    "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", 
    "Federated States of Micronesia", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", 
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Grenada", 
    "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Honduras", 
    "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", 
    "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", 
    "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Martinique", 
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", 
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", 
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Norway", "Oman", 
    "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", 
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
    "Saint Lucia", "Samoa", "San Marino", "São Tomé and Príncipe", "Saudi Arabia", "Senegal", "Serbia", 
    "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", 
    "South Africa", "South Georgia and the South Sandwich Islands", "South Korea", "Sudan", "Spain", 
    "Sri Lanka", "St. Vincent and the Grenadines", "Suriname", "Svalbard and Jan Mayen", "Swaziland", 
    "Sweden", "Switzerland", "Tajikistan", "Tanzania", "Thailand", "UAE", "Togo", "Tonga", 
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", 
    "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", 
    "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"
] + major_cities




selected_locations = st.multiselect("Location Targeting * (City targeting included major metropolitan cities only)", location_list)
eu_countries = st.checkbox("Add all EU Countries (*Feature available in next update*)")

if st.button("Add Campaign Data"):
    
    free_row=st.session_state.df[st.session_state.df['Campaign'] == ''].index[0]
    df = st.session_state.df

    df.loc[free_row,'Campaign'] = campaign_name
    df.loc[free_row,'Campaign Type'] = 'Display'
    df.loc[free_row,'Networks'] = network
    df.loc[free_row,'Bid Strategy Type'] = bid_strategy
    df.loc[free_row,'Start Date'] = start_date
    df.loc[free_row,'End Date']= end_date
    df.loc[free_row,'Standard conversion goals'] = 'Account-level'
    df.loc[free_row,'Targeting method'] = 'Location of presence'
    df.loc[free_row,'Audience targeting'] = audience_targeting_selection
    df.loc[free_row,'Campaign Status'] = 'Paused'
    df.loc[free_row,'Budget'] = daily_budget
    df.loc[free_row,'Budget type'] = "Daily"
    df.loc[free_row,'Business name'] = business_name


    ##enumerate to add location data

    for i, country in enumerate(selected_locations):
        df.loc[free_row+i+1,'Campaign'] = campaign_name
        df.loc[free_row+i+1,'Location'] = country



    ##end location data enumeration

    st.session_state.df =df
    st.success("Campaign Data Added")
    

#Adding Ad groups and custom audience segments to the df
st.write("")
st.write("")
st.write("")    
st.write("")    
st.write("") 
filt=st.session_state.df['Campaign'] != ''
current_campaigns = list(set(st.session_state.df.loc[filt,'Campaign'].tolist()))
st.write("**Ad Groups and Custom Audience Segments**")

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

    st.success("Ad Group Data Added")


#store a list of all current ad groups to a variable 
filt =  st.session_state.df['Ad Group'] != ''
adgroup_list = st.session_state.df.loc[filt,'Ad Group'].tolist()
cta_options = ['Learn more','Book now', 'Download']




#Adding responsive ads to the df
st.write("")
st.write("")
st.write("")    
st.write("")    
st.write("") 
st.write("**Add Responsive Display Ads**")
selected_adgroup = st.selectbox("Adding to which ad group:", adgroup_list)
responsive_headline1 = st.text_input("Ad Headline 1:", key="r1")
charlimit(responsive_headline1,30)
responsive_headline2 = st.text_input("Ad Headline 2:", key ="r2")
charlimit(responsive_headline2,30)
responsive_headline3 = st.text_input("Ad Headline 3:", key ='r3')
charlimit(responsive_headline3,30)
responsive_headline4 = st.text_input("Ad Headline 4:", key = 'r4')
charlimit(responsive_headline4,30)
responsive_headline5 = st.text_input("Ad Headline 5:", key ='r5')
charlimit(responsive_headline5,30)
long_headline = st.text_input("Long Headline:",key='l1')
charlimit(long_headline,90)
ad_type = 'Responsive display ad'
ad_format = 'All formats'

description1 = st.text_input("Desc. 1:", key = 'd1')
charlimit(description1,90)
description2 = st.text_input("Desc. 2:", key = 'd2')
charlimit(description2,90)
description3 = st.text_input("Desc. 3:", key = 'd3')
charlimit(description3,90)
description4 = st.text_input("Desc. 4:", key = 'd4')
charlimit(description4,90)
description5 = st.text_input("Desc. 5:", key = 'd5')
charlimit(description5,90)


final_url = st.text_input("Final URL:", key= 'u1')
cta_selection = st.selectbox("CTA:",cta_options)



if st.button("Add Responsive Ad Data"):
    
    free_row=st.session_state.df[st.session_state.df['Campaign'] == ''].index[0]
    df = st.session_state.df
    df.loc[free_row,'Campaign'] = campaign_name
    df.loc[free_row,'Ad Group'] = selected_adgroup
    df.loc[free_row,'Ad type'] = ad_type
    df.loc[free_row,'Headline 1',] = responsive_headline1
    df.loc[free_row,'Headline 2'] = responsive_headline2
    df.loc[free_row,'Headline 3'] = responsive_headline3
    df.loc[free_row,'Headline 4'] = responsive_headline4
    df.loc[free_row,'Headline 5'] = responsive_headline5
    df.loc[free_row,'Long headline'] = long_headline
    df.loc[free_row,'Call to action'] = cta_selection

    df.loc[free_row,'Description 1'] = description1
    df.loc[free_row,'Description 2'] = description2
    df.loc[free_row,'Description 3'] = description3
    df.loc[free_row,'Description 4'] = description4
    df.loc[free_row,'Description 5'] = description5
    df.loc[free_row,'Logo 1'] = 'images/logo1.jpg'
    df.loc[free_row,'Image 1'] = 'images/landscape1.jpg'
    df.loc[free_row,'Final URL'] = final_url

    df.loc[free_row,'Ad formats'] = ad_format
    st.success("Ad Data Added")

def clear_text():
    st.session_state["r1"] = ""
    st.session_state["r2"] = ""
    st.session_state["r3"] = ""
    st.session_state["r4"] = ""
    st.session_state["r5"] = ""
    st.session_state["l1"] = ""
    st.session_state["d1"] = ""
    st.session_state["d2"] = ""
    st.session_state["d3"] = ""
    st.session_state["d4"] = ""
    st.session_state["d5"] = ""
    st.session_state["u1"] = ""
    
st.button("Clear Text Input", on_click=clear_text)
st.write("")
st.write("")
st.write("")
st.write("")




st.write("File Output:")
st.write(st.session_state.df)
#chuck blank rows 
cleaned_df = st.session_state.df[st.session_state.df["Campaign"].str.strip() != ""]

csv = cleaned_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label='Download Export File',
    data=csv,
    file_name="CampaignData.csv",
    mime="text/csv"
)



#evening task - Finalise the character limit warning functions and checks