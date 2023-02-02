'''
on Terminal write below :
% pip install streamlit 
Then :
stremlit hello >> the IDE will open the browser with new host tab

To run a file from PC or web :
way 1) $ python -m streamlit run your_script.py (your scripts as file name not stander)
way 2) $ streamlit run your_script.py
way 3) $ streamlit run path.py

To display our first app :
import streamlist as st
# Create the Data Frame Or put the data frame details (path)
import pandas as pd
df= pd.Data_frame({'col1' : [1,2,3,4],
                   'col2' : [5,6,7,8]})
df

Then write :
streamlit run "path.py" like below
streamlit run "G:\My Drive\DataSciense\***\streamlit_app.py" >> Enter
'''
import streamlit as st
import pandas as pd
import numpy as np

# to set a title
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done...!')

# Create sub-header for the selected data row :
# Also we added a checkbox to allow user to explain the data once need
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)

# Create New sub-header for histogram visualization :
st.subheader('Number of pickup by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Crate New sub-header for Mapp visualization :
st.subheader('Mapp of all pickups')
st.map(data)

"""
Now we are filtering the date while hour == 17\n
So first created variable to filter the dataframe in hour == 17\n
And now it will be for Mapp visualization on 17 clock.
"""
st.subheader("New Mapp with scroll selection base on hours")
hour_to_filter = st.slider('hour', 0, 23, 17)
# min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
