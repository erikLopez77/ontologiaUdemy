import streamlit as st
import pandas as pd
from sparql_processor import run_sparql_query

st.title("Film finder")
film_name = st.text_input("Enter the name of a film")
st.button("Search")

if st.button("search") or film_name:
    results = run_sparql_query(sparql_param=film_name,
                                sparq_file="./sparql_queries/film_details.sparql")
    if results["results"] ["bindings"]:
        columns=["title", "runtime", "directorLabel","countryLabel"]

        table_data=[]
        for result in results["results"]["bindings"]:
            row_data={}
            for column in columns:
                if result.get(column):
                    row_data(column)=result[column][]

    else:
        st.write("No results found for the entered film name.")
