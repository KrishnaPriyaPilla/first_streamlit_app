import streamlit

streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 and blueberry oatmeal')
streamlit.text ('🥗 Kale, Spinach and Rocket smoothie')
streamlit.text ('🐔 Hard-Boiled free-range egg')
streamlit.text ('🥑🍞 Avaocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruits_list)
