from pyshacl import validate
from rdflib import Graph

data_graph = Graph()
data_graph.parse("ttl/film_abox.ttl", format="turtle")

sg = Graph()
sg.parse("ttl/film_shacl_rules.ttl", format="turtle")

og = Graph()
og.parse("ttl/film_tbox.ttl", format="turtle")
og.parse("ttl/align_dbpedia.ttl", format="turtle")

r = validate(data_graph, shacl_graph=sg, ont_graph=og, inference='both', abort_on_first=False,
             allow_infos=False, allow_warnings=True, meta_shacl=False, advanced=True, js=False, debug=False, inplace=True)
conforms, results_graph, results_text = r

print(f"Results: \n{results_text}")

data_graph.serialize(destination="ttl/film_abox_inferred_with_shacl.ttl")
