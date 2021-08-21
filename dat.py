import streamlit as st

import pandas as pd


df = pd.read_csv('County_dis.csv')
print(df)

df1 = pd.read_csv('distribution_of_sunscreen_and_support_products_to_persons_with_albinism_pwas.csv')
print(df1)

st.write('''
# Data
top
''')

st.bar_chart(df[['AfterSun_Lotions', 'Caps']].sum())
st.line_chart(df1.Number_Of_Registered_Persons_With_Albinism)

