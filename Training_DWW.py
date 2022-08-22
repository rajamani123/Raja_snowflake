import streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega3 & Blueberry Oatmeal')
streamlit.text('Kale,Spinach and Rocket smoothie')
streamlit.text('Hard boiled free range egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
