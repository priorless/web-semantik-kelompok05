# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30 triple
- Triple dengan LIMIT 30: 90 triple
- Baris SELECT LIMIT 10 / kota berbeda: 10 baris / 10 kota berbeda
- Mengapa tidak (atau mengapa tepat) 30 triple: Hasilnya tepat mencapai 30 triple karena `CONSTRUCT` memiliki 3 pola (`?kota a ex:Kota`, `?kota rdfs:label ?namaKota`, dan `?kota ex:populasi ?populasi`), dan dengan `LIMIT 10`, sebanyak 10 solution yang dihasilkan masing-masing mencetak 3 triple secara konsisten tanpa adanya duplikat atau data ganda yang disatukan.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia 
- Triple yang tetap tercetak untuk film tanpa tanggal: Triple `schema:name` dan `schema:director` serta `a schema:Movie` tetap tercetak karena bagian `dbo:releaseDate` dibungkus dalam blok `OPTIONAL`, sehingga jika data tanggalnya tidak ada, baris tersebut diabaikan tanpa membuat seluruh solusi gagal. Tidak ada pesan error karena sifat `OPTIONAL` di SPARQL bersifat toleran terhadap data yang kosong.
- Query lokal tanpa internet: Berhasil dijalankan pada berkas `film_nolan.ttl`, karena graf tersebut sudah disimpan secara fisik di penyimpanan lokal sehingga rdflib tidak membutuhkan koneksi jaringan. Namun, jika seluruh skrip `demo_c.py` dijalankan ulang tanpa internet, program akan mengalami error saat mengeksekusi `sp.queryAndConvert()` karena gagal menghubungi endpoint DBpedia secara daring.
- Mengapa dbo:Film memberi 0 pada `film_nolan.ttl`: Karena query Demo B mengubah tipe film menjadi `schema:Movie`, bukan `dbo:Film`. Oleh karena itu, pencarian dengan tipe `dbo:Film` tidak menemukan data yang sesuai.

## Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0, Sesudah: 3, Ada Rina: 3
- Mengapa Ada Rina bernilai 3: Karena entitas `ex:rina` ditambahkan ke dalam graf setelah blok kode materialisasi (CONSTRUCT) selesai dieksekusi. Aturan inferensi subkelas tidak berjalan secara otomatis saat ada data baru masuk, sehingga triple turunan `ex:rina a foaf:Person` belum terbentuk di dalam graf.
- Output materialisasi_ulang.py: 
    Putaran 1: 4 triple baru | Person: 3
    Rina masuk | Person: 3
    Putaran 2 | Person: 4
    Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: `ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, dan `ex:andi a ex:Mahasiswa`. Ketiganya sudah ada di graf awal, sehingga tidak dihitung sebagai triple baru.
- Kegunaan `kampus_turunan.ttl` dan langkah manual yang tersisa: File terpisah ini sangat berguna karena memisahkan *data fakta* dari *data inferensi*. Jika suatu hari ontologi berubah (misal: `ex:Dosen` tidak lagi subkelas dari `foaf:Person`), kita cukup menghapus `kampus_turunan.ttl` dan menjalankan ulang skrip tanpa risiko merusak data asli. Namun, langkah manual yang tetap harus dilakukan adalah memperbarui file sumber (`kampus.ttl`) agar mencerminkan taksonomi yang baru sebelum materialisasi dijalankan.


## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Tidak ada triple yang dihasilkan. | variabel `?film` pada CONSTRUCT tidak terikat karena WHERE menggunakan `?f`. | 3 triple: Following, Insomnia, dan Memento. |
| rusak_b | 4 triple | `Christopher Nolan` memiliki dua nama yang berbeda tag bahasanya. | Query mengambil semua nama tanpa memilih satu bahasa untuk setiap orang. | 3 triple, satu nama untuk setiap orang menggunakan VALUES dan FILTER. |
| rusak_c | 0 triple | Tidak ada individu yang ditemukan sebagai `ex:Permukiman`. | Query hanya mencari tipe langsung `ex:Permukiman`, sedangkan data menggunakan kelas turunannya. | 3 triple: Medan, Surabaya, dan Tomok, menggunakan property path `a/rdfs:subClassOf*`. |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan secara langsung karena file ini hanya berisi query, bukan kode untuk mengirim HTTP request. | Terpenuhi karena program mendefinisikan User-Agent melalui variabel UA, kemudian mengirimkannya menggunakan parameter `agent=UA` pada SPARQLWrapper. |
| 2 LIMIT | Menggunakan LIMIT 10 untuk membatasi jumlah solution yang dihasilkan. Hasilnya adalah 30 triple karena setiap solution menghasilkan 3 triple. | Tidak menggunakan LIMIT pada query `q_demo_b.rq`. Query dibatasi berdasarkan film yang disutradarai Christopher Nolan, tetapi tidak memiliki batas jumlah solution. |
| 3 Simpan, jangan ulangi | Tidak menyimpan hasil graf secara otomatis karena file ini hanya berisi query untuk endpoint. | Memenuhi aturan dengan mengambil data satu kali, menyimpannya ke `film_nolan.ttl`, kemudian membaca dan mengolah file tersebut secara lokal. |
| 4 Jangkar jalur | Memenuhi aturan karena menggunakan `wdt:P31/wdt:P279* wd:Q515`. Jalur berakhir pada IRI tetap `wd:Q515` yang mewakili kelas kota. | Tidak menggunakan property path * atau +, sehingga aturan ini tidak diterapkan secara langsung pada query Demo B. |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: 
    Query : 
    ```sparql
        PREFIX ex:  <http://contoh.id/>
        PREFIX wd:  <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>

        CONSTRUCT {
            ?kota a ex:Kota .
        }
        WHERE {
            ?kota wdt:P31/wdt:P279* ?kelas ;
            wdt:P17 wd:Q252 ;
            wdt:P1082 ?populasi .
        }
        LIMIT 10
    ```
    Alasan : Jalur `wdt:P31/wdt:P279*` tidak memiliki IRI tetap sebagai tujuan karena menggunakan variabel `?kelas`. Akibatnya, mesin harus mencari berbagai kemungkinan kelas yang terhubung melalui hierarki subclass. Walaupun `?kota` sudah dibatasi oleh negara dan populasi, jalur yang tidak memiliki tujuan spesifik tetap berpotensi menghasilkan banyak pencocokan dan membebani endpoint. Penggunaan LIMIT 10 tidak selalu membatasi pekerjaan yang harus dilakukan mesin saat mengevaluasi pola tersebut..

### Diskusi 1 - Taksonomi berubah
Berdasarkan hasil Bagian C, terdapat perbedaan antara `kampus_v4.ttl` dari C1 dan `kampus_turunan.ttl` dari C2. File `kampus_v4.ttl` menyimpan data awal bersama hasil materialisasi pertama, sedangkan `kampus_turunan.ttl` menyimpan triple hasil inferensi secara terpisah, termasuk hasil materialisasi ulang setelah Rina ditambahkan.

Misalnya, setahun kemudian hubungan `ex:DosenTetap rdfs:subClassOf ex:Dosen` dihapus dari taksonomi. Triple inferensi seperti `ex:budi a ex:Dosen` dan `ex:budi a foaf:Person` menjadi tidak valid karena Budi tidak lagi dapat ditelusuri melalui hubungan tersebut. Kesimpulan serupa untuk Rina juga perlu diperiksa karena Rina ditambahkan pada C2 sebagai `ex:DosenTetap`.

Pada `kampus_v4.ttl`, triple lama bercampur dengan data fakta sehingga lebih sulit dibedakan. Sebaliknya, `kampus_turunan.ttl` memudahkan pemeriksaan karena hanya berisi hasil inferensi. Cara menemukannya adalah memperbarui taksonomi pada `kampus.ttl`, menjalankan kembali materialisasi, lalu membandingkan hasil baru dengan triple turunan lama. Triple lama yang tidak lagi dihasilkan menjadi kandidat kesimpulan yang sudah tidak valid. Jadi, pemisahan graf turunan membantu proses pembaruan dan menjaga agar data produksi tidak menyimpan kesimpulan yang sudah usang.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota, saya memilih *SELECT* karena hasilnya dapat ditampilkan dalam bentuk tabel dan lebih mudah diperiksa sebelum digunakan untuk perhitungan. Pada Bagian A, data populasi Medan memiliki dua nilai, yaitu *2.435.252* dan *2.097.610*. Kondisi ini perlu diperhatikan agar dashboard tidak langsung menganggap kedua angka tersebut sebagai dua populasi yang harus dijumlahkan. Dengan *SELECT*, setiap baris dan nilai populasi dapat diperiksa terlebih dahulu, kemudian dipilih berdasarkan sumber atau aturan yang sesuai. SELECT tidak otomatis menghilangkan data ganda, tetapi memudahkan pemeriksaan dan pengolahan hasil.

Untuk menggabungkan data kota dari tiga sumber berbeda, saya memilih *CONSTRUCT*. Alasannya, CONSTRUCT dapat mengubah data dari beberapa kosakata menjadi struktur graf dengan kosakata target yang seragam. Hal ini memudahkan penggabungan dan penggunaan data dari berbagai sumber.

Namun, penggabungan tetap membutuhkan pemeriksaan nilai dan literal. Pada `rusak_b.rq`, hasil awalnya adalah 4 triple untuk 3 orang karena Christopher Nolan memiliki dua literal nama, yaitu "Christopher Nolan" dan "Christopher Nolan"@en. Keduanya dianggap berbeda karena tag bahasanya berbeda. Setelah diperbaiki menggunakan VALUES dan FILTER, hasilnya menjadi 3 triple. Jadi, *SELECT* lebih sesuai untuk memeriksa data dashboard, sedangkan *CONSTRUCT* lebih sesuai untuk menyelaraskan struktur graf dari beberapa sumber.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: LIMIT 10 menghasilkan 30 triple dari 10 solution dengan 3 pola triple. Bagian D-C: Medan hanya muncul satu kali meskipun dapat ditemukan melalui lebih dari satu jalur subclass. |
| 2 | Bagian D-A: `rusak_a.rq` menghasilkan 0 triple karena `?film` tidak terikat di WHERE. Setelah diperbaiki menjadi `?f`, hasilnya 3 triple. |
| 3 | Bagian D-B: `rusak_b.rq` menggunakan property path `foaf:name`|`rdfs:label`|`schema:name` untuk mengambil nama dari beberapa predikat. `perbaikan_b.rq` menggunakan VALUES dan FILTER untuk memilih bahasa nama setiap orang. UNION tidak digunakan secara langsung dalam query yang diuji. |
| 4 | Bagian A dan C: Query menggunakan `wdt:P31/wdt:P279*` dan `a/rdfs:subClassOf*` untuk menelusuri hubungan kelas tanpa menuliskan setiap kelas perantara. Dalam praktikum ini, jalur * digunakan, sedangkan jalur + tidak diuji secara langsung.|
| 5 | Bagian C: Jumlah Person tetap 3 setelah Rina ditambahkan. Setelah materialisasi ulang pada Putaran 2, jumlah Person menjadi 4. |
