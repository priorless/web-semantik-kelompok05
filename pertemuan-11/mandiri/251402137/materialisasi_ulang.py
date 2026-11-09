
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, FOAF

g = Graph().parse("kampus.ttl", format="turtle")
turunan = Graph()

EX = Namespace("http://contoh.id/kampus/")

def hitung_person(graph):
    return len(set(graph.subjects(RDF.type, FOAF.Person)))

def materialisasi(graph, hasil):
    sebelum = len(hasil)

    aturan = graph.query("""
        CONSTRUCT {
            ?x a ?super
        }
        WHERE {
            ?x a/rdfs:subClassOf+ ?super
        }
    """)

    for triple in aturan:
        if triple not in graph:
            graph.add(triple)
            hasil.add(triple)

    return len(hasil) - sebelum

# Putaran pertama
baru = materialisasi(g, turunan)
print(f"Putaran 1: {baru} triple baru | Person:{hitung_person(g)}")

# Menambahkan individu Rina
g.add((EX.rina, RDF.type, EX.DosenTetap))

print(f"Rina masuk | Person:{hitung_person(g)}")

# Putaran kedua
baru = materialisasi(g, turunan)
print(f"Putaran 2: {baru} triple baru | Person:{hitung_person(g)}")

# Menyimpan hasil
g.serialize("kampus_v4.ttl", format="turtle")
turunan.serialize("kampus_turunan.ttl", format="turtle")

print(f"Triple turunan disimpan terpisah: {len(turunan)}")
