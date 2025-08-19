import streamlit as st
import plotly.express as ps
#pob = price of bitcoin(not accurate just random)
pob = [60000, 79000, 59000, 90000, 70900, 80000]#these are n0t accurate
year = [2020, 2021, 2022, 2023, 2024, 2025]
figure = ps.line( x=year, y=pob, title="The prices of bitcoin during the following years( its not accurate )" )
st.plotly_chart(figure)