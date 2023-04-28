import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("Data/final.csv")
data["Date"] = pd.to_datetime(data['Date'])
event_date = pd.read_csv("Data/MajorEvents.csv")
event_date['Date'] = pd.to_datetime(event_date['Date']) # convert Date column to datetime format


# Create a sidebar with a dropdown menu
# Create a sidebar with a dropdown menu
options1 = ['Metal', 'Energy', 'Microchips', "Transport", "Food"]
all_option1 = 'All of Them'
if st.sidebar.checkbox('Select all industries', False):
    option1 = [all_option1]
else:
    option1 = st.sidebar.multiselect('Which industries do you want to visualize?', options1)

# Filter data based on selected options
if all_option1 in option1:
    data_filtered = data.copy()
else:
    data_filtered = data.loc[:, ['Date'] + option1]
    
# Create plot
sns.set_style('darkgrid')
fig, ax = plt.subplots()
if all_option1 in option1:
    for col in data_filtered.columns[2:]:
        sns.lineplot(x='Date', y=col, data=data_filtered, label=col, ax=ax)
else:
    for col in option1:
        sns.lineplot(x='Date', y=col, data=data_filtered, label=col, ax=ax)
    
# Highlight event date
option2 = st.sidebar.selectbox(
    'Which event do you want to visualize?',
     event_date['Event'].unique())

date = event_date.loc[event_date['Event'] == option2, 'Date'].iloc[0]

plt.axvline(date, color='red', linestyle='--', label='Event Date')

plt.xlim(date - pd.Timedelta(days=20), date + pd.Timedelta(days=20))

# set x-axis ticks
xticks = [date - pd.Timedelta(days=20), date, date + pd.Timedelta(days=20)]
xticklabels = ['t-20', date.strftime('%Y-%m-%d'), 't+20']
plt.xticks(xticks, xticklabels)
plt.xticks(rotation=45)

# add title and axis labels
plt.title('Cumulative Returns by Industry')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')

# move the legend to the bottom right corner
plt.legend(loc='lower right')

# show the plot
st.pyplot(fig)
