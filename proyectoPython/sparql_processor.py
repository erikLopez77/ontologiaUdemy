from SPARQLWrapper import SPARQLWrapper, JSON
# creamos un cliente concectado al endpoint de DBpedia
sparql_wrapper = SPARQLWrapper("http://dbpedia.org/sparql")
sparql_wrapper.setReturnFormat(JSON)

# funcion que se le pasa el valor de consulta y la ruta al archivo .sparql


def run_sparql_query(sparql_param, sparql_file):
    # abre y lee el archivo sparql
    with open(sparql_file, "r") as file:
        query = file.read().replace("{sparql_param}", sparql_param)

    sparql_wrapper.setQuery(query)

    try:
        # ejecuta la consulta y la convierte a JSON
        ret = sparql_wrapper.queryAndConvert()
        # se itera sobre los resultados y se retornan los datos obtenidos
        for r in ret["results"]["bindings"]:
            print(r)
        return ret
    except Exception as e:
        print(e)


# se ejecuta si el script es llamado directamente (no como modulo)
if __name__ == "__main__":
    file_name = input("Enter the file name:")
    run_sparql_query(file_name, "./sparql_queries/film_details.sparql")
