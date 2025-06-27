import streamlit as st
import pandas as pd
from sparql_processor import run_sparql_query

st.title("Film finder")
film_name = st.text_input("Enter the name of a film")

if (st.button("Search") or film_name):

    var = run_sparql_query(sparql_param=film_name,
                           sparql_file="./sparql_queries/ask_query.sparql")
    if var["boolean"]:
        results = run_sparql_query(sparql_param=film_name,
                                   sparql_file="./sparql_queries/film_details_with_number.sparql")
        if results["results"]["bindings"]:
            # definimos las columnas
            columns = ["title", "runtime", "directorLabel", "countryLabel"]

            table_data = []
            for result in results["results"]["bindings"]:
                row_data = {}
                for column in columns:
                    # al  iterar si existe la columna se da el valor
                    if result.get(column):
                        row_data[column] = result[column]["value"]
                    else:  # de lo contrario se pone el guion
                        row_data[column] = "-"
                table_data.append(row_data)
            # se crea el df de pandas, en automatico se agregan los titulos
            table_data = pd.DataFrame(table_data)
            # se añade al panel
            st.dataframe(table_data)

            # se agrega etiqueta que nos da el numero de peliculas distintas (nuevo query)
            film_number = results["results"]["bindings"][0]["filmNumber"]["value"]
            st.write("Number of film results: "+film_number)
    else:
        st.write("No results found for the entered film name.")
