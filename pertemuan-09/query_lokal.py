from pathlib import Path
from rdflib import Graph

g = Graph()
g.parse(Path("../pertemuan-06/kampus_usu.ttl"), format="turtle")
print("Jumlah triple awal:", len(g))

PREFIX = """
PREFIX ex:   <https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
"""

# 1. SELECT: siapa mengajar apa
q_select = PREFIX + """
SELECT ?namaDosen ?namaMK WHERE {
  ?dosen ex:mengajar ?mk ;
         foaf:name   ?namaDosen .
  ?mk    foaf:name   ?namaMK .
}
ORDER BY ?namaDosen
"""

for row in g.query(q_select):
    print(row.namaDosen, "-", row.namaMK)

# 2. ASK: fakta yang belum tercatat
q_ask = PREFIX + """
ASK { ex:isa_dadi ex:mengajar ex:mk_baru_pertemuan09 }
"""

print("Sebelum INSERT:", g.query(q_ask).askAnswer)

# 3. TELL lewat SPARQL Update
g.update(PREFIX + """
INSERT DATA {
  ex:isa_dadi ex:mengajar ex:mk_baru_pertemuan09 .
  ex:mk_baru_pertemuan09 foaf:name "Pemrograman Web Lanjut"@id .
}
""")

print("Sesudah INSERT:", g.query(q_ask).askAnswer)
print("Jumlah triple akhir:", len(g))

g.serialize("kampus_usu_v2.ttl", format="turtle")
