# Pertemuan 7 - Serialisasi RDF

## Artefak
- Graf asal: 32 triple (39 triple setelah reifikasi)
- Format ekspor: Turtle, JSON-LD, N-Triples
- Named graph: `<https://priorless.github.io/web-semantik-kelompok05/graph/kampus>` dan `<https://priorless.github.io/web-semantik-kelompok05/graph/fakultas>`

## Reifikasi dan provenance

* **Triple yang dianotasi:** `ex:isa_dadi ex:mengajar ex:web_semantik`
* **Creator:** Kelompok 05
* **Date:** 2026-10-08
* **Source:** Graf `kampus_usu.ttl` dari Pertemuan 6.

Triple tersebut menyatakan bahwa Isa Dadi mengajar mata kuliah Web Semantik. Reifikasi klasik digunakan untuk merepresentasikan triple tersebut sebagai resource dengan `rdf:Statement`, `rdf:subject`, `rdf:predicate`, dan `rdf:object`. Informasi provenance ditambahkan untuk mencatat pembuat, tanggal, dan sumber data.

## Perbandingan Serialisasi RDF

| Format    | Kekuatan utama                           | Skenario tepat |
| :-------- | :--------------------------------------- | :------------- |
| Turtle    | Ringkas dan mudah dibaca manusia         | Cocok untuk membuat dan membaca data RDF secara manual, terutama saat mengembangkan ontology atau mengecek isi graf. |
| JSON-LD   | Cocok web/API dan HTML                   | Cocok digunakan untuk aplikasi web dan API karena bentuk datanya mirip dengan JSON yang sudah umum digunakan dalam pengembangan web. |
| RDF/XML   | Kompatibilitas data lama                 | Cocok untuk sistem atau aplikasi lama yang sudah menggunakan RDF/XML dan membutuhkan kompatibilitas dengan format tersebut.|
| N-Triples | Satu triple per baris; stabil untuk diff | Cocok untuk penyimpanan data RDF sederhana dan pengecekan perubahan data menggunakan Git karena setiap triple berada di satu baris.|
| N-Quads   | Menambahkan konteks graf                 | Cocok digunakan ketika data berasal dari beberapa graf atau sumber yang berbeda dan kita perlu mengetahui triple tersebut berasal dari graf yang mana. |

## Perbandingan
- Format paling mudah dibaca manusia: `Turtle`, karena sintaksnya ringkas dan bentuk triple RDF-nya mudah dipahami saat dibaca atau diedit secara manual.
- Format untuk HTML/API: `JSON-LD`, karena menggunakan struktur JSON yang umum digunakan pada aplikasi web dan lebih mudah diproses oleh JavaScript.
- Perbedaan reifikasi klasik dan RDF-star: `Reifikasi klasik` membutuhkan beberapa triple tambahan untuk menjelaskan sebuah triple, sehingga lebih panjang dan verbose. Sedangkan `RDF-star` dapat menambahkan informasi seperti creator atau sumber langsung pada triple yang ingin diberi keterangan, sehingga penulisannya lebih ringkas.


## Refleksi
Mengapa named graph berguna saat menggabungkan data dari sumber berbeda?
Named graph berguna untuk memisahkan kumpulan triple berdasarkan sumber atau kelompok datanya. Dengan begitu, data dari sumber berbeda dapat digabungkan tanpa kehilangan informasi mengenai graf asalnya. Hal ini juga memudahkan pengelolaan dan pemeriksaan data.
Mengapa provenance penting untuk sebuah triple?
Provenance penting untuk mengetahui asal informasi, siapa yang membuat atau mencatatnya, dan kapan informasi tersebut dibuat. Dengan provenance, data lebih mudah ditelusuri dan keandalannya dapat dievaluasi.
Format apa yang Anda pilih untuk git diff, dan mengapa?
Saya memilih N-Triples karena setiap triple ditulis dalam satu baris dengan format yang konsisten. Hal ini memudahkan Git untuk menampilkan baris yang ditambahkan, dihapus, atau diubah ketika terjadi perubahan pada graf RDF.
