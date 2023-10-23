import numpy as np  
import pandas as pd  
import plotly_express as px  
import plotly.figure_factory as ff
import streamlit as st 
from supabase import create_client
from st_supabase_connection import SupabaseConnection
import json
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title = 'Scorpius II Employee and System Information"',
    page_icon = 'Scorpion',
    layout = 'wide',
)

supabase = st.experimental_connection("supabase",type=SupabaseConnection)

st.markdown("<h1 style='text-align: center; color: white;'>Scorpius II Employee and System Information</h1>", unsafe_allow_html=True)

employees = supabase.table('Employees').select('*').execute().data # fetching documents with filtering
df = pd.DataFrame(employees)

inventory = supabase.table('Scorpius-Inventory').select('*').execute().data # fetching documents with filtering
inventory_df = pd.DataFrame(inventory)

st.header('Location')
location_filter = st.selectbox("♏",pd.unique(df['City']))  

placeholder = st.empty()

#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#local_css("style.css")

df = df[df["City"] == location_filter]
next_df = df[['EEID', 'Full Name', 'Email', 'Job Title','Department', 'Business Unit', 'City', 'Hire Date', 'Access']]
p_access = len(next_df[next_df['Access']== 'Privileged'])
s_access = len(next_df[next_df['Access']== 'Standard'])

inventory_df = inventory_df[inventory_df['City'] == location_filter]
inv_df = inventory_df[['Asset', 'Type', 'Risk', 'City']]
unpatched = len(inventory_df[inventory_df['Failure']== 'Improper Patch'])
total_equip = len(inventory_df)

with placeholder.container():
    kpi1, kpi2 = st.columns(2)

        # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Priviledged User Access",
        value=p_access,
        )
        
    kpi2.metric(
        label="Standard User Access",
        value=s_access,
        )
   
    
    st.subheader("Scorpius II Employee Accounts")
    next_df = next_df.style.set_properties(**{'background-color': 'blue', 'color': 'white'})
    st.dataframe(next_df, hide_index=True)

    kpi3, kpi4= st.columns(2)
    kpi3.metric(
        label="Total System Components",
        value= total_equip,
        )
        
    kpi4.metric(
        label="Unpatched Equipment",
        value =f"{round((unpatched / total_equip) * 100)} % ",
        )    
 
    st.subheader("Scorpius II Equipment Inventory")
    inv_df = inv_df.style.set_properties(**{'background-color': 'blue', 'color': 'white'})
    st.dataframe(inv_df, hide_index=True)

