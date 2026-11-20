
import csv
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics

# IRI dasar graf kampus kelompok 05
BASE = "https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#"

ERR = Namespace(
    "http://www.daml.org/2002/03/agents/agent-ont#"
)

# Lokasi folder pertemuan-12
FOLDER = Path(__file__).resolve().parent
SUMBER = FOLDER / "kampus_usu_v5.ttl"

# 1. Memuat graf asserted
if not SUMBER.exists():
    raise FileNotFoundError(
        f"File tidak ditemukan: {SUMBER}"
    )

asserted = Graph().parse(SUMBER, format="turtle")

print("Sumber:", SUMBER)
print("Jumlah triple awal:", len(asserted))

# 2. Menambahkan aksioma dan triple yang sengaja terbalik
asserted.update(f"""
PREFIX ex: <{BASE}>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT DATA {{
    ex:Pegawai owl:disjointWith ex:Course .

    
}}
""")

# Kelas yang diperiksa
KELAS = ["Lecturer", "Pegawai", "Course"]


def anggota(g, kelas):
    return len(
        set(
            g.subjects(
                RDF.type,
                URIRef(BASE + kelas)
            )
        )
    )


# 3. Menjalankan reasoner RDFS dan OWL RL
hasil = {}

for nama, semantik in [
    ("RDFS", RDFS_Semantics),
    ("OWL RL", OWLRL_Semantics)
]:
    g = Graph() + asserted

    DeductiveClosure(semantik).expand(g)

    # Mencari pesan inkonsistensi
    pesan = [
        str(e)
        for m in g.subjects(RDF.type, ERR.ErrorMessage)
        for e in g.objects(m, ERR.error)
    ]

    hasil[nama] = {
        k: anggota(g, k)
        for k in KELAS
    }

    print("\nProfil:", nama)
    print("Jumlah triple:", len(g))
    print("Jumlah pesan galat:", len(pesan))

    for p in pesan:
        print("  ", p)


# 4. Membuat laporan CSV
with open(
    FOLDER / "laporan_kelas.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    w = csv.writer(f)

    w.writerow([
        "kelas",
        "asserted",
        "rdfs",
        "owl_rl"
    ])

    for k in KELAS:
        w.writerow([
            k,
            anggota(asserted, k),
            hasil["RDFS"][k],
            hasil["OWL RL"][k]
        ])

print("\nCSV tersimpan: laporan_kelas.csv")
