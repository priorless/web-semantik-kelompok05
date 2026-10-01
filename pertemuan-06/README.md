# RDF Dasar: Triple dan Identifier

## Membaca Triple RDF

Setiap pernyataan RDF terdiri dari subject, predicate, dan object.

| Kalimat                                       | Subject          | Predicate    | Object           |
| --------------------------------------------- | ---------------- | ------------ | ---------------- |
| Ida Adi adalah dosen.                         | `ex:ida`         | `rdf:type`   | `ex:Lecturer`    |
| Ida Adi mengajar Web Semantik.                | `ex:ida`         | `ex:teaches` | `ex:WebSemantik` |
| Mata kuliah itu memiliki nama "Web Semantik". | `ex:WebSemantik` | `ex:name`    | `"Web Semantik"` |

Pada RDF, subject merupakan sesuatu yang dibahas, predicate adalah hubungan atau sifatnya, sedangkan object merupakan tujuan hubungan atau nilai yang dimiliki subject. Object berupa entitas menggunakan IRI, sedangkan nilai teks seperti nama mata kuliah menggunakan literal.
