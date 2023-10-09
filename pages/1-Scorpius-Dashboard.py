import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import plotly.figure_factory as ff
from collections import Counter
import streamlit as st  # 🎈 data web app development
import plotly.graph_objects as go 
import random
import warnings
warnings.filterwarnings('ignore')

# System User Input
df = pd.read_csv("Scorpius-Users.csv")

# System Inventory Input
inventory_df = pd.read_csv("Scorpius-Inventory.csv")

# Security Events
causes = pd.read_csv('event-cause.csv')

# Repair Costs
impact_df = pd.read_csv('failure_impact.csv')

st.set_page_config(
    page_title = 'Scorpius CyberSecurity Dashboard"',
    page_icon = 'Scorpion',
    layout = 'wide',
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
st.markdown("<h1 style='text-align: center; color: white;'>Scorpius II CyberSecurity Dashboard</h1>", unsafe_allow_html=True)

# top-level filters
          
st.header('Location')
location_filter = st.selectbox("",pd.unique(df['City']))  

impact = pd.DataFrame(columns=['Asset','Failure','Repair Time', 'Repair Cost'])
table_df = pd.DataFrame()
failure_df = pd.DataFrame()
new_event = pd.DataFrame(columns=['Event'])
#fig = go.Figure() 

def sample(causes,df,number,filter):

    e_cause = causes.sample(number, random_state=None, replace=True)
    events = np.array([])
    events = e_cause[['Events']].values

    new_df = df[df["City"] == filter]
    temp_df = new_df.sample(number, random_state=None)
    next_df = temp_df[['Full Name', 'Job Title','Department', 'City']]
    next_df.insert(4, 'Event', ' ')
    next_df.iloc[:,4] = events
    table_df = next_df[['Full Name', 'Event', 'Job Title']]
    return table_df

def plotly_bar_chart(
        df: pd.DataFrame,
        x_axis_label: str = 'Violations',
        y_axis_label: str = 'Number of Events'
) -> go.Figure:
    this_chart = go.Figure(
        data=[go.Bar(x=df['user-e'], y=df['user-v'], text = df['user-v'],textposition = 'auto')])
    this_chart.update_yaxes(title_text=y_axis_label)
    this_chart.update_xaxes(title_text=x_axis_label)

    return this_chart

new_table = pd.DataFrame()
i = 0

  
placeholder = st.empty()

inv_df = inventory_df[inventory_df["City"] == location_filter]
hardware = inv_df[['Asset', 'Failure', 'Risk']]


for seconds in range(1,200):
    
# Process rows for Left Column
    fourth = seconds % 3

    if i == 0:
        new_table = sample(causes,df,5,location_filter)
        users = new_table

    if fourth == 0 & i:
        sub_table = sample(causes,df,2,location_filter)
#        new_table = new_table.append(sub_table)
        new_table = pd.concat([new_table, sub_table], axis=0)
        users = new_table
    i = 1
    users = new_table.reset_index()
    
# Process rows for Right Column

    inventory_rows = random.randint(1, len(hardware)) 
    fifth = seconds % 5
    if seconds == 1:
        failure_df = hardware.iloc[inventory_rows:inventory_rows+1]
        impact = hardware.iloc[inventory_rows:inventory_rows+1]
        impact.drop(['Risk'], axis=1, inplace=True)

    if fifth == 0:
        failure_df = pd.concat([failure_df, hardware.iloc[inventory_rows:inventory_rows+1]], axis=0)
        impact = pd.concat([impact, hardware.iloc[inventory_rows:inventory_rows+1]], axis=0)
        impact.drop(['Risk'], axis=1, inplace=True)
    failure = failure_df.reset_index()

    
    if seconds == 1:
        impact.insert(2, 'Hours', ' ')
        impact.insert(3, 'Cost', ' ')
    for fails in range(len(impact)):
        fail = impact.iloc[fails][1]

    for impacts in range(len(impact_df)):
        repair = impact_df.iloc[impacts][0]

        if fail == repair:
            timeto = impact_df.iloc[impacts][1]
            costto = impact_df.iloc[impacts][2] 

            impact.iloc[fails, 2] =  timeto
            impact.iloc[fails, 3] = costto

    repair_impact = impact[['Asset', 'Failure', 'Hours', 'Cost']]
    repair_impact = impact.reset_index()

#   user_v has number of times an event occurred
    user_temp = Counter(new_table['Event'])
    vio_value = user_temp.values()
    user_v = pd.DataFrame.from_dict(vio_value) 

#   user_e has list of violation types
    user_violations = new_table.groupby(['Event']).size()
    user_e = user_violations.index.values
    sec_events = pd.DataFrame(columns = ['user-e', 'user-v'])
    sec_events['user-e'] = user_e
    sec_events['user-v'] = user_v


    with placeholder.container():
        left_column, middle_column, right_column = st.columns(3, gap = 'medium')
        with left_column:
            st.subheader("Employee Security Events")
            users = users.style.set_properties(**{'background-color': 'blue', 'color': 'white'})
            st.dataframe(users, hide_index=True)
            
        with middle_column:
            st.subheader("Failure Impact")
            repair_impact = repair_impact.style.set_properties(**{'background-color': 'blue', 'color': 'white'})
            st.dataframe(repair_impact, hide_index=True)  

        with right_column:
            st.subheader("System Failures")
            failure = failure.style.set_properties(**{'background-color': 'blue', 'color': 'white'})
            st.dataframe(failure, hide_index=True) 

        st.write('User Security Violations')
        chart = plotly_bar_chart(df = sec_events)
        st.plotly_chart(chart, use_container_width=True)            


        

    time.sleep(3)
