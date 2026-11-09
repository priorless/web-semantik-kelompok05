
import sys
from rdflib import Graph

if len(sys.argv) != 3:
    print("Cara pakai: python jalankan.py data.ttl query.rq")
    sys.exit(1)

data_file = sys.argv[1]
query_file = sys.argv[2]

g = Graph()
g.parse(data_file, format="turtle")

with open(query_file, "r", encoding="utf-8") as f:
    query = f.read()

hasil = g.query(query)

if hasil.type == "CONSTRUCT":
    print("Jumlah triple hasil:", len(hasil.graph))
    print(hasil.serialize(format="turtle"))
else:
    for row in hasil:
        print(row)
    print("Jumlah baris:", len(hasil))
