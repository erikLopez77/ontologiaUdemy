import streamlit as st
import pandas as pd
from sparql_processor import run_sparql_query

st.title("Film finder")
film_name = st.text_input("Enter the name of a film")
st.button("Search")
