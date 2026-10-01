from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()

EX = Namespace("https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

# DOSEN
g.add((EX.isa_dadi, RDF.type, EX.Lecturer))
g.add((EX.isa_dadi, FOAF.name, Literal("Isa Dadi", lang="id")))

g.add((EX.umaya, RDF.type, EX.Lecturer))
g.add((EX.umaya, FOAF.name, Literal("Umayya", lang="id")))

g.add((EX.opim_salim, RDF.type, EX.Lecturer))
g.add((EX.opim_salim, FOAF.name, Literal("Opim Salim", lang="id")))

# MATA KULIAH
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))

g.add((EX.basis_data, RDF.type, EX.Course))
g.add((EX.basis_data, FOAF.name, Literal("Basis Data", lang="id")))

g.add((EX.dasar_pemrograman, RDF.type, EX.Course))
g.add((EX.dasar_pemrograman, FOAF.name, Literal("Dasar Pemrograman", lang="id")))

# MAHASISWA
g.add((EX.indah, RDF.type, EX.Student))
g.add((EX.indah, FOAF.name, Literal("Indah Ayu Gemilang", lang="id")))

g.add((EX.keizya, RDF.type, EX.Student))
g.add((EX.keizya, FOAF.name, Literal("Keizya Azalea Azka", lang="id")))

# UNIVERSITAS
g.add((EX.usu, RDF.type, EX.University))
g.add((EX.usu, FOAF.name, Literal("Universitas Sumatera Utara", lang="id")))

# RELASI DOSEN DENGAN MATA KULIAH
g.add((EX.isa_dadi, EX.mengajar, EX.web_semantik))
g.add((EX.umaya, EX.mengajar, EX.basis_data))
g.add((EX.opim_salim, EX.mengajar, EX.dasar_pemrograman))

# RELASI MAHASISWA DENGAN MATA KULIAH
g.add((EX.indah, EX.mengambil, EX.web_semantik))
g.add((EX.keizya, EX.mengambil, EX.basis_data))

# RELASI DOSEN DENGAN UNIVERSITAS
g.add((EX.isa_dadi, EX.bekerjaDi, EX.usu))
g.add((EX.umaya, EX.bekerjaDi, EX.usu))
g.add((EX.opim_salim, EX.bekerjaDi, EX.usu))

# JUMLAH KREDIT MATA KULIAH
g.add((EX.web_semantik, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))
g.add((EX.basis_data, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))
g.add((EX.dasar_pemrograman, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))

# HARI KULIAH
g.add((EX.web_semantik, EX.hariKuliah, Literal("Senin", lang="id")))
g.add((EX.basis_data, EX.hariKuliah, Literal("Selasa", lang="id")))
g.add((EX.dasar_pemrograman, EX.hariKuliah, Literal("Rabu", lang="id")))

print(g.serialize(format="turtle"))
g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)


print("\nOutput Turtle:\n" + "="*40)
print(g.serialize(format="turtle"))

print("\nDaftar dosen:\n" + "="*40)
for subject, predicate, obj in g.triples((None, RDF.type, EX.Lecturer)):
    print(subject)