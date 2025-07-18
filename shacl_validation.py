from pyshacl import validate
from rdflib import Graph

data_graph = Graph()
data_graph.parse("ttl/film_abox.ttl", format="turtle")

sg = Graph()
sg.parse("ttl/film_shacl.ttl", format="turtle")

og = Graph()
og.parse("ttl/film_tbox.ttl", format="turtle")
og.parse("ttl/align_dbpedia.ttl", format="turtle")

r = validate(data_graph, shacl_graph=sg, ont_graph=og, inference='both', abort_on_first=False,
             allow_infos=True, allow_warning=False, meta_shacl=False, advanced=False, js=False, debug=False)
conforms, results_graph, results_text = r

print(f"Results: \n{results_text}")
