from rdflib import Graph

g = Graph()
g.parse("../pertemuan-06/kampus_usu.ttl", format="turtle")

g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)
g.serialize("kampus_usu.nt", format="nt")

print(f"Jumlah triple: {len(g)}")
print(g.serialize(format="turtle"))