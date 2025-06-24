from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

sparql.setReturnFormat(JSON)


def run_sparql_query(sparql_param, sparql_file):
    with open(sparql_file, "r") as file:
        query = file.read().replace("{sparql_param}", sparql_param)

    sparql_wrapper.setQuery(query)

    try:
        ret = sparql.queryAndConvert()
        for r in ret["results"]["bindings"]:
            print(r)
        return ret
    except Exception as e:
        print(e)


if __name__ == "__main__":
    file_name = input("Enter the file name:")
    run_sparql_query(file_name, "./sparql_queries/film_details.sparql")
