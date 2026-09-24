# Semantik Web Layer Cake

| Lapis | Peran | Contoh Anda |
| --- | --- | --- |
| URI dan Unicode | Identitas global dan representasi karakter | URI sumber belajar pada file `metadata-sumber.ttl` |
| XML | Sintaks pertukaran data | XML pada file `profil_saya.xml` |
| RDF dan RDFS | Pernyataan graph dan kosakata dasar | RDF pada file `metadata-sumber.ttl` |
| Ontology / OWL | Makna domain dan penalaran lebih kaya | OWL pada file `ontology-kampus.owl` |
| SPARQL | Query graph RDF | Belum ada artefak terkait pada Pertemuan 1–4 |
| Rules, Proof, Trust | Belum ada artefak terkait pada Pertemuan 1–4 |

## Mengapa ontology berada di atas RDF/RDFS dan di bawah SPARQL?

Ontology berada di atas RDF/RDFS karena RDF/RDFS menyediakan dasar untuk merepresentasikan data dan hubungan, sedangkan ontology seperti OWL memberikan makna dan aturan yang lebih lengkap terhadap data.

Ontology berada di bawah SPARQL karena SPARQL digunakan untuk melakukan query atau mengambil informasi dari graph RDF yang menggunakan konsep dan hubungan yang didefinisikan oleh ontology.

Secara sederhana:

**RDF/RDFS → Ontology/OWL → SPARQL**