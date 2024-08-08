 # import module
import streamlit as st
import pandas as pd
import numpy

df = pd.read_csv("CutGemEffects.csv").drop('Gem ID', axis=1)
 
# Title
st.title("Joe's Page For Testing Streamlit")

st.text("This page references the video game \"New World\" By Amazon Game Studios." )

# Header
st.header('Please Select a Gem with the Menu Below')

# checkbox
if st.checkbox("Show/Hide Gems Stat Sheet"): 
    st.text(df.to_string()) 

dfArray = df.values.tolist()

gemNames = []
for i in dfArray:
    gemNames.append(i[0])

# Selection box
gem = st.selectbox("Gem: ", gemNames)

# slider
tier = st.slider("Select the Tier", 1, 4)

gem_id = gemNames.index(gem)

xLineChart = []
columns = [True]*len(dfArray[0])
for i in range(3,7):
    columns[i]=False
for i in range(9,13):
    columns[i]=False
match tier:
    case 1:
        columns[3] = True
        columns[9] = True
        xLineChart = ["Effect 1 Tier 1","Effect 2 Tier 1"]
    case 2:
        columns[4] = True
        columns[10] = True
        xLineChart = ["Effect 1 Tier 2","Effect 2 Tier 2"]
    case 3:
        columns[5] = True
        columns[11] = True
        xLineChart = ["Effect 1 Tier 3","Effect 2 Tier 3"]
    case 4:
        columns[6] = True
        columns[12] = True
        xLineChart = ["Effect 1 Tier 4","Effect 2 Tier 4"]

# Header
st.header('-'*60)

# Subheader
st.subheader('You Have Selected a Tier {} {}'.format(tier,gem))
st.text(df.loc[gem_id,columns])

st.bar_chart(data=df, x='Gem',y=["Effect 1 Tier 1","Effect 1 Tier 2","Effect 1 Tier 3","Effect 1 Tier 4"])

st.bar_chart(data=df, x='Gem',y=["Effect 2 Tier 1","Effect 2 Tier 2","Effect 2 Tier 3","Effect 2 Tier 4"])