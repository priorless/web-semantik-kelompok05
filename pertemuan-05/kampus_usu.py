from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()

EX = Namespace("https://priorless.github.io/web-semantik-kelompok05/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)


g.add((EX.isa_dadi, RDF.type, EX.Lecturer))
g.add((EX.isa_dadi, FOAF.name, Literal("Isa Dadi", lang="id")))
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.isa_dadi, EX.mengajar, EX.web_semantik))


print(g.serialize(format="turtle"))
g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)