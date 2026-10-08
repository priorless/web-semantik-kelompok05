# Pertemuan 7 - Serialisasi RDF


## Reifikasi dan provenance

* **Triple yang dianotasi:** `ex:isa_dadi ex:mengajar ex:web_semantik`
* **Creator:** Kelompok 05
* **Date:** 2026-10-08
* **Source:** Graf `kampus_usu.ttl` dari Pertemuan 6.

Triple tersebut menyatakan bahwa Isa Dadi mengajar mata kuliah Web Semantik. Reifikasi klasik digunakan untuk merepresentasikan triple tersebut sebagai resource dengan `rdf:Statement`, `rdf:subject`, `rdf:predicate`, dan `rdf:object`. Informasi provenance ditambahkan untuk mencatat pembuat, tanggal, dan sumber data.

## Refleksi
Mengapa named graph berguna saat menggabungkan data dari sumber berbeda?
Named graph berguna untuk memisahkan kumpulan triple berdasarkan sumber atau kelompok datanya. Dengan begitu, data dari sumber berbeda dapat digabungkan tanpa kehilangan informasi mengenai graf asalnya. Hal ini juga memudahkan pengelolaan dan pemeriksaan data.
Mengapa provenance penting untuk sebuah triple?
Provenance penting untuk mengetahui asal informasi, siapa yang membuat atau mencatatnya, dan kapan informasi tersebut dibuat. Dengan provenance, data lebih mudah ditelusuri dan keandalannya dapat dievaluasi.
Format apa yang Anda pilih untuk git diff, dan mengapa?
Saya memilih N-Triples karena setiap triple ditulis dalam satu baris dengan format yang konsisten. Hal ini memudahkan Git untuk menampilkan baris yang ditambahkan, dihapus, atau diubah ketika terjadi perubahan pada graf RDF.
