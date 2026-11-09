# Tugas Mandiri Pertemuan 11 — Web Semantik

## A. CONSTRUCT Wikidata dan Pengujian LIMIT

### 1. Pengujian CONSTRUCT LIMIT 10

Query CONSTRUCT dijalankan menggunakan Wikidata Query Service dengan batas `LIMIT 10`. Hasil yang diperoleh adalah **30 triple**.

Setiap data kota menghasilkan tiga pola triple, yaitu:

- `?kota a ex:Kota` untuk menyatakan bahwa data tersebut merupakan kota.
- `?kota rdfs:label ?namaKota` untuk menyimpan nama kota.
- `?kota ex:populasi ?populasi` untuk menyimpan jumlah populasi kota.

Karena terdapat 10 data kota dan setiap data menghasilkan tiga triple, jumlah keseluruhan adalah 30 triple.

### 2. Pengujian CONSTRUCT LIMIT 30

Setelah batas query diubah menjadi `LIMIT 30`, hasil yang diperoleh adalah **90 triple**.

Jumlah tersebut meningkat karena query memproses hingga 30 data kota. Setiap data menghasilkan tiga triple sehingga perhitungannya adalah 30 × 3 = 90 triple.

### 3. Pengujian SELECT LIMIT 10

Query kemudian diubah dari CONSTRUCT menjadi SELECT dengan variabel `?kota`, `?namaKota`, dan `?populasi`, serta menggunakan `LIMIT 10`.

Hasil pengujian menunjukkan **10 baris data**. Berdasarkan hasil yang diperoleh, terdapat 10 kota berbeda.

### 4. Analisis Hasil

Dari ketiga pengujian tersebut, dapat diketahui bahwa CONSTRUCT digunakan untuk membentuk graf RDF baru berdasarkan pola triple yang ditentukan pada bagian template. Sementara itu, SELECT digunakan untuk menampilkan data dalam bentuk tabel hasil query.

Perubahan LIMIT dari 10 menjadi 30 menyebabkan jumlah hasil CONSTRUCT meningkat dari 30 menjadi 90 triple. Hal ini terjadi karena setiap solusi menghasilkan tiga pola triple.

Dalam RDF, triple yang identik tidak disimpan berulang kali karena graf RDF merupakan himpunan triple. Oleh karena itu, jika terdapat triple yang sama, triple tersebut hanya dihitung satu kali dalam graf hasil.

## B. Mengambil Data Film dari DBpedia

### 1. Menjalankan Query CONSTRUCT

Pada bagian ini, query `q_demo_b.rq` digunakan untuk mengambil data film yang disutradarai oleh Christopher Nolan dari endpoint SPARQL DBpedia.

Query menggunakan pola CONSTRUCT untuk membentuk graf RDF baru dengan kosakata Schema.org. Data yang diambil mencakup identitas film, nama film, sutradara, dan tanggal rilis jika tersedia.

### 2. Menyimpan Hasil ke Turtle

Query dijalankan menggunakan program `demo_c.py`. Hasil dari endpoint kemudian dimasukkan ke dalam graf RDF menggunakan RDFLib dan disimpan ke file `film_nolan.ttl`.

Berdasarkan hasil pengujian, graf yang berhasil diperoleh berisi **48 triple**.

### 3. Mengolah Data Secara Lokal

Setelah graf disimpan, file `film_nolan.ttl` dibaca kembali menggunakan RDFLib. Selanjutnya, query SELECT dijalankan untuk menghitung jumlah film yang tidak memiliki tanggal publikasi.

Hasil pengujian menunjukkan terdapat **16 film tanpa tanggal publikasi**.

### 4. Analisis Hasil

Penggunaan `OPTIONAL` pada query memungkinkan data film tetap diambil meskipun informasi tanggal rilis tidak tersedia. Dengan demikian, film yang tidak memiliki tanggal rilis tetap dapat masuk ke dalam hasil query.

Penyimpanan hasil ke dalam format Turtle juga memudahkan pengolahan data secara lokal tanpa harus mengakses endpoint DBpedia berulang kali. Hal ini membuat proses pengujian lebih efisien dan mengurangi permintaan ke endpoint publik.

## C. Materialisasi dan Inferensi RDF

### 1. Pengujian Materialisasi pada Graf Kampus

Pada bagian ini dilakukan pengujian materialisasi menggunakan data pada file `kampus.ttl`. Materialisasi digunakan untuk menambahkan triple hasil inferensi berdasarkan hubungan hierarki kelas dalam graf RDF.

Pada pengujian menggunakan `demo_d.py`, hasil awal menunjukkan **0 triple**. Setelah proses materialisasi dilakukan, diperoleh **3 triple**. Ketika Rina ditambahkan, jumlah individu yang termasuk kategori Person tetap 3 pada hasil pengujian tersebut.

Hasil ini menunjukkan bahwa materialisasi dapat menambahkan informasi hasil inferensi ke dalam graf berdasarkan aturan yang digunakan.

### 2. Materialisasi Ulang dengan Graf Terpisah

Selanjutnya, pengujian dilakukan menggunakan `materialisasi_ulang.py`. Pada pendekatan ini, triple hasil inferensi disimpan secara terpisah dalam graf `turunan`, kemudian hasil akhirnya disimpan ke file `kampus_turunan.ttl`.

Hasil pengujian menunjukkan:

- Putaran 1 menghasilkan 4 triple baru dengan jumlah Person sebanyak 3.
- Setelah Rina ditambahkan, jumlah Person masih 3 sebelum materialisasi ulang.
- Putaran 2 menghasilkan 2 triple baru dengan jumlah Person menjadi 4.
- Total triple turunan yang tersimpan secara terpisah adalah **6 triple**.

Hasil tersebut menunjukkan bahwa penambahan data baru dapat menghasilkan kesimpulan tambahan ketika materialisasi dilakukan kembali.

### 3. Analisis Hasil

Dari kedua pengujian tersebut, dapat diketahui bahwa materialisasi menyimpan hasil inferensi sebagai triple nyata di dalam graf RDF.

Pada pengujian pertama, hasil materialisasi disimpan bersama graf utama dan menghasilkan file `kampus_v4.ttl`. Pada pengujian kedua, hasil inferensi dipisahkan ke dalam `kampus_turunan.ttl`.

Pemisahan graf turunan memudahkan proses pemeriksaan dan pembaruan hasil inferensi. Apabila terdapat perubahan pada data atau hierarki kelas, materialisasi perlu dilakukan kembali agar kesimpulan yang tersimpan tetap sesuai dengan kondisi terbaru.

## D. Debugging Query SPARQL

Pada bagian ini dilakukan pengujian terhadap tiga query SPARQL yang sengaja dibuat memiliki kesalahan. Setiap query dijalankan menggunakan `jalankan.py`, kemudian diperbaiki dan diuji kembali.

### Kasus A — Kesalahan Variabel

Query `rusak_a.rq` menghasilkan 0 triple karena variabel `?film` pada bagian CONSTRUCT tidak terikat dengan variabel `?f` pada bagian WHERE. Setelah diperbaiki dengan menggunakan variabel yang konsisten, `perbaikan_a.rq` berhasil menghasilkan 4 triple film.

### Kasus B — Pemilihan Nama

Query `rusak_b.rq` menghasilkan 4 triple karena Christopher Nolan memiliki dua sumber nama, yaitu `foaf:name` dan `rdfs:label`. Hal ini menyebabkan nama yang sama muncul dalam dua bentuk literal berbeda.

Setelah diperbaiki menggunakan UNION dan FILTER NOT EXISTS, query hanya memilih satu sumber nama untuk setiap orang. Hasilnya adalah 3 triple untuk Christopher Nolan, Joko Anwar, dan Mira Lesmana.

### Kasus C — Property Path

Query `rusak_c.rq` menghasilkan 0 triple karena hanya mencari individu yang secara langsung memiliki tipe `ex:Permukiman`.

Perbaikannya menggunakan property path `a/rdfs:subClassOf*` untuk menelusuri hubungan kelas dan seluruh kelas turunannya. Hasilnya adalah 3 triple, yaitu Medan, Surabaya, dan Tomok.

### Kesimpulan

Ketiga pengujian menunjukkan bahwa kesalahan kecil dalam penulisan variabel, pemilihan properti, dan penelusuran hierarki kelas dapat memengaruhi hasil query SPARQL. Pengujian sebelum dan sesudah perbaikan membantu memastikan query menghasilkan data sesuai tujuan.

## E. Etika Endpoint dan Diskusi Tertulis

## E1. Etika Endpoint

Empat aturan etika endpoint diperiksa berdasarkan file `a_kota_limit.rq` dan `demo_c.py`.

### 1. User-Agent Bermakna

Aturan ini diterapkan pada `demo_c.py`:

- Pernyataan `UA = "KelasWebSemantik/1.0 (quinshailmi@students.usu.ac.id)"` mendefinisikan identitas aplikasi dan alamat email sebagai kontak.
- Pemanggilan `SPARQLWrapper("https://dbpedia.org/sparql", agent=UA)` mengirimkan identitas tersebut ketika mengakses endpoint DBpedia.

Dengan demikian, endpoint dapat mengenali aplikasi yang mengirimkan permintaan melalui identitas User-Agent yang digunakan.

### 2. LIMIT Saat Eksplorasi

Aturan ini diterapkan pada `a_kota_limit.rq`:

- Bagian `LIMIT 10` membatasi jumlah solution yang diproses oleh query.
- Berdasarkan pengujian Bagian A, 10 solution menghasilkan 30 triple karena setiap solution dapat mengisi tiga pola pada template CONSTRUCT.

LIMIT membatasi solution, bukan secara langsung jumlah triple yang dihasilkan.

### 3. Simpan, Jangan Ulangi

Aturan ini diterapkan pada `demo_c.py`:

- `sp.queryAndConvert()` mengambil hasil query dari endpoint DBpedia.
- `g.serialize("film_nolan.ttl", format="turtle")` menyimpan hasil ke file Turtle.
- `lokal = Graph().parse("film_nolan.ttl")` membaca kembali file tersebut menjadi graf lokal.
- `lokal.query(Q_TANPA_TANGGAL)` menjalankan query SELECT pada graf lokal tanpa mengakses endpoint kembali.

Dengan cara ini, hasil dari endpoint cukup diambil dan disimpan satu kali, kemudian dapat diolah kembali tanpa mengirim permintaan berulang.

### 4. Jangkar Jalur

Aturan ini diterapkan pada `a_kota_limit.rq`:

- Pola `wdt:P31/wdt:P279* wd:Q515` menggunakan IRI tetap `wd:Q515` sebagai tujuan jalur. Dengan demikian, pencarian diarahkan pada kelas kota, bukan menelusuri semua kemungkinan pasangan kelas.

### Contoh Query yang Melanggar Aturan 4

Berikut contoh query yang sengaja dibuat tanpa jangkar IRI. Query ini hanya untuk dianalisis dan **tidak dijalankan**.

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?x ?y
WHERE {
  ?x rdfs:subClassOf* ?y .
}
```

Query tersebut melanggar aturan jangkar jalur karena menggunakan dua variabel, yaitu `?x` dan `?y`, sebagai awal dan akhir penelusuran. Endpoint harus mempertimbangkan banyak kemungkinan pasangan kelas dalam graf. Operator `*` juga memungkinkan jalur dengan panjang nol, sehingga node dapat berpasangan dengan dirinya sendiri.

Akibatnya, ruang pencarian menjadi jauh lebih luas dan dapat membutuhkan lebih banyak waktu serta sumber daya endpoint. Sebaiknya jalur dibatasi menggunakan IRI tertentu agar pencarian lebih terarah dan efisien.

### E2. Diskusi

#### 1. Perubahan Taksonomi dan Materialisasi

Jika taksonomi berubah setelah hasil materialisasi disimpan ke graf produksi, triple hasil inferensi yang bergantung pada hubungan kelas lama berpotensi menjadi tidak valid. Contohnya, ketika suatu kelas tidak lagi menjadi turunan dari kelas induknya, triple tipe yang sebelumnya disimpulkan melalui hubungan tersebut harus diperiksa kembali. Triple yang perlu diperiksa adalah triple hasil inferensi yang jalur hierarki kelasnya sudah tidak berlaku. Nama triple yang benar-benar salah belum dapat ditentukan tanpa mengetahui perubahan taksonomi yang terjadi.

Hal ini terlihat dari perbandingan `kampus_v4.ttl` dan `kampus_turunan.ttl`. Pada pengujian C1, hasil materialisasi dimasukkan ke graf utama. Sementara itu, pada C2, hasil inferensi disimpan terpisah dalam `kampus_turunan.ttl`. Pengujian menghasilkan 4 triple baru pada putaran pertama dan 2 triple baru setelah Rina ditambahkan, sehingga total terdapat 6 triple turunan. Pemisahan ini memudahkan pemeriksaan karena kesimpulan hasil inferensi tidak bercampur dengan data awal.

Untuk menemukan triple yang sudah tidak sesuai, saya akan menjalankan materialisasi ulang menggunakan taksonomi terbaru, kemudian membandingkan hasilnya dengan `kampus_turunan.ttl` lama. Triple yang hanya ada pada hasil lama perlu diperiksa dan dihapus jika tidak lagi didukung oleh aturan terbaru. Dengan demikian, materialisasi perlu dihitung ulang ketika taksonomi berubah.

#### 2. SELECT atau CONSTRUCT untuk Dashboard dan Integrasi Data?

Untuk dashboard populasi kota, saya akan menggunakan SELECT karena dashboard membutuhkan data berbentuk baris yang mudah ditampilkan, difilter, dan diolah menjadi tabel atau grafik. Pada Bagian A, pengujian SELECT dengan LIMIT 10 menghasilkan 10 baris dari 10 kota berbeda. Namun, data Medan memiliki dua nilai populasi, yaitu 2.435.252 dan 2.097.610. Hal ini menunjukkan bahwa satu kota dapat memiliki lebih dari satu nilai populasi sehingga sumber dan waktu pembaruan data perlu diperhatikan sebelum menentukan angka yang ditampilkan.

Sementara itu, untuk menggabungkan data kota dari tiga sumber, saya lebih memilih CONSTRUCT. Query ini dapat membentuk graf baru dengan struktur dan kosakata yang diseragamkan sehingga data dari sumber berbeda lebih mudah digabungkan. Akan tetapi, hasilnya tetap perlu diperiksa agar perbedaan nilai tidak dianggap sebagai duplikasi yang boleh dihapus begitu saja.

Temuan `rusak_b.rq` juga menunjukkan pentingnya pemeriksaan saat menggabungkan data. Query tersebut menghasilkan 4 triple karena Christopher Nolan memiliki dua bentuk nama, yaitu literal biasa dan literal berbahasa Inggris. Setelah diperbaiki, hasilnya menjadi 3 triple, masing-masing satu nama untuk setiap orang. Jadi, SELECT lebih sesuai untuk kebutuhan tampilan dashboard, sedangkan CONSTRUCT lebih sesuai untuk membentuk graf hasil integrasi.

## Cek Diri Berdasarkan Hasil Praktikum

1. **CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar.**  
   Bukti: Bagian A, CONSTRUCT dengan LIMIT 10 menghasilkan 30 triple, sedangkan LIMIT 30 menghasilkan 90 triple. Graf RDF menyimpan triple sebagai himpunan sehingga triple yang benar-benar identik tidak dihitung berulang.

2. **Triple dengan variabel tak terikat tidak dicetak, tanpa error.**  
   Bukti: Bagian D, `rusak_a.rq` menghasilkan 0 triple karena variabel `?film` pada CONSTRUCT tidak terikat oleh pola WHERE yang menggunakan `?f`.

3. **UNION, jalur `|`, dan VALUES menyatukan predikat berbeda.**  
   Bukti: Bagian D, `rusak_b.rq` menggunakan VALUES untuk memilih tiga orang dan jalur alternatif `foaf:name|rdfs:label|schema:name` untuk mengambil nama dari beberapa predikat. Query perbaikannya menggunakan UNION untuk memilih sumber nama secara terkontrol.

4. **Jalur `+` dan `*` menelusuri hierarki tanpa menyebut perantara.**  
   Bukti: Bagian C, query materialisasi menggunakan `rdfs:subClassOf+` untuk memperoleh tipe kelas induk. Bagian D, `perbaikan_c.rq` menggunakan `rdfs:subClassOf*` dan menghasilkan 3 triple untuk Medan, Surabaya, dan Tomok.

5. **Materialisasi menyimpan kesimpulan, tetapi harus dihitung ulang.**  
   Bukti: Bagian C, materialisasi menghasilkan 4 triple pada putaran pertama dan 2 triple pada putaran kedua, sehingga total 6 triple turunan disimpan dalam `kampus_turunan.ttl`. Jika taksonomi berubah, hasil inferensi perlu dihitung ulang agar kesimpulan lama yang tidak lagi sesuai dapat diperbarui.