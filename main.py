import streamlit as st
import plotly.express as px
import pandas as pd

# Reading the data frame
df = pd.read_csv("happy.csv")

# Converting data frame to a list
columns = list(df.columns)

# Contains lists of the cleaned up column name and the original column name for later comparison
matched_list = []

# Creating a clean list of column names
for i in range(len(columns)):
    matched_list.append([columns[i].replace("_", " ").title(), columns[i]])
    columns[i] = columns[i].replace("_", " ").title()

# Display title, selection boxes and subheader for scattor plot
st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis", columns[1:])
y_axis = st.selectbox("Select the data for the Y-axis", columns[1:])
st.subheader(f"{x_axis} and {y_axis}")

# Returns the correct column data
def get_data(column):
    return list(df[column])

# Iterates through matched_list and returns the original column name
def match_column(column):
    for i in range(len(matched_list)):
        if matched_list[i][0] == column:
            return matched_list[i][1]

# Retriving the data
x_axis_data = get_data(match_column(x_axis))
y_axis_data = get_data(match_column(y_axis))

# Creating the figure and plotting the data
figure = px.scatter(x=x_axis_data, y=y_axis_data, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
