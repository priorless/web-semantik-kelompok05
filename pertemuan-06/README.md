# Pertemuan 6 - RDF Dasar

## IRI dasar graf

Graf RDF ini menggunakan namespace berikut:

* `ex:` — `http://example.org/kampus/`
* `rdf:` — `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* `rdfs:` — `http://www.w3.org/2000/01/rdf-schema#`

## Ringkasan graf

* Jumlah triple: **3** (untuk contoh awal pada Langkah 1)
* Namespace yang digunakan: `ex:`, `rdf`
* Entitas: `ex:ida`, `ex:Lecturer`, `ex:WebSemantik`

## Contoh triple

1. `ex:ida` - `rdf:type` - `ex:Lecturer`
2. `ex:ida` - `ex:teaches` - `ex:WebSemantik`
3. `ex:WebSemantik` - `ex:name` - `"Web Semantik"`

## Perbandingan serialisasi

* Turtle: Menggunakan prefix agar IRI lebih singkat dan mudah dibaca.
* JSON-LD: Menggunakan format JSON dengan konteks untuk menjelaskan namespace dan hubungan antar-entitas.
* Pernyataan yang sama: Kedua format merepresentasikan informasi RDF yang sama, yaitu Ida Adi adalah dosen, mengajar Web Semantik, dan mata kuliah tersebut memiliki nama "Web Semantik".

## Refleksi

1. Object harus berupa IRI jika merujuk pada entitas atau sumber daya lain. Object berupa literal jika berisi nilai seperti teks, angka, atau tanggal.
2. Prefix membantu keterbacaan karena IRI panjang dapat ditulis dalam bentuk yang lebih singkat. Prefix tidak mengubah IRI sebenarnya.
3. Salah satu kesalahan pemodelan yang dihindari adalah menggunakan literal sebagai subject, padahal subject RDF harus berupa IRI atau blank node.




## Refleksi

**1. Kapan object harus berupa IRI dan kapan berupa literal?**

Object menggunakan IRI kalau merujuk pada entitas lain, misalnya mata kuliah Web Semantik. Kalau object berisi nilai seperti nama mata kuliah, maka digunakan literal, contohnya `"Web Semantik"`.

**2. Mengapa prefix membantu keterbacaan tanpa mengubah IRI?**

Prefix membuat penulisan IRI yang panjang menjadi lebih singkat dan mudah dibaca. Prefix hanya sebagai pengganti bagian awal IRI, jadi alamat IRI aslinya tetap sama.

**3. Sebutkan satu kesalahan pemodelan yang Anda hindari pada graf ini.**

Kesalahan yang saya hindari adalah menggunakan literal sebagai subject. Contohnya, `"Web Semantik"` digunakan sebagai nilai nama mata kuliah, bukan sebagai subject. Subject harus berupa IRI atau blank node.
