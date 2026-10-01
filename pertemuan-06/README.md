# Pertemuan 6 - RDF Dasar

## IRI dasar graf

Graf RDF menggunakan namespace berikut:

* `ex:` — `http://example.org/kampus/`
* `rdf:` — `http://www.w3.org/1999/02/22-rdf-syntax-ns#`

## Contoh triple

Berikut contoh pemodelan kalimat menjadi triple RDF.

| Kalimat                                       | Subject          | Predicate    | Object           |
| --------------------------------------------- | ---------------- | ------------ | ---------------- |
| Ida Adi adalah dosen.                         | `ex:ida`         | `rdf:type`   | `ex:Lecturer`    |
| Ida Adi mengajar Web Semantik.                | `ex:ida`         | `ex:teaches` | `ex:WebSemantik` |
| Mata kuliah itu memiliki nama "Web Semantik". | `ex:WebSemantik` | `ex:name`    | `"Web Semantik"` |

Subject merupakan entitas yang dibahas, predicate menunjukkan hubungan atau sifatnya, sedangkan object merupakan entitas lain atau nilai yang berkaitan dengan subject.


## Refleksi

**1. Kapan object harus berupa IRI dan kapan berupa literal?**

Object menggunakan IRI kalau merujuk pada entitas lain, misalnya mata kuliah Web Semantik. Kalau object berisi nilai seperti nama mata kuliah, maka digunakan literal, contohnya `"Web Semantik"`.

**2. Mengapa prefix membantu keterbacaan tanpa mengubah IRI?**

Prefix membuat penulisan IRI yang panjang menjadi lebih singkat dan mudah dibaca. Prefix hanya sebagai pengganti bagian awal IRI, jadi alamat IRI aslinya tetap sama.

**3. Sebutkan satu kesalahan pemodelan yang Anda hindari pada graf ini.**

Kesalahan yang saya hindari adalah menggunakan literal sebagai subject. Contohnya, `"Web Semantik"` digunakan sebagai nilai nama mata kuliah, bukan sebagai subject. Subject harus berupa IRI atau blank node.
