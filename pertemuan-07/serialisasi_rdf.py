
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, DCTERMS, XSD

# Membaca graf dari Pertemuan 6
g = Graph()
g.parse("../pertemuan-06/kampus_usu.ttl", format="turtle")

# Namespace sesuai dengan graf kelompok
EX = Namespace(
    "https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#"
)

# Catat jumlah triple sebelum reifikasi
jumlah_awal = len(g)
print(f"Jumlah triple awal: {jumlah_awal}")

# Triple asli yang akan diberi provenance:
# isa_dadi mengajar web_semantik
stmt = EX["stmt-01"]

# Reifikasi klasik
g.add((stmt, RDF.type, RDF.Statement))
g.add((stmt, RDF.subject, EX.isa_dadi))
g.add((stmt, RDF.predicate, EX.mengajar))
g.add((stmt, RDF.object, EX.web_semantik))

# Informasi provenance
g.add((stmt, DCTERMS.creator, Literal("Kelompok 05")))
g.add((
    stmt,
    DCTERMS.date,
    Literal("2026-10-08", datatype=XSD.date)
))
g.add((
    stmt,
    DCTERMS.source,
    Literal("Graf kampus_usu.ttl Pertemuan 6")
))

# Ekspor graf setelah ditambahkan reifikasi
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)
g.serialize("kampus_usu.nt", format="nt")

print(f"Jumlah triple setelah reifikasi: {len(g)}")
print(g.serialize(format="turtle"))