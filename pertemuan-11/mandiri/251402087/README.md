# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30 triple
- Triple dengan LIMIT 30: 90 triple
- Baris SELECT LIMIT 10 / kota berbeda: 10 baris / 10 kota berbeda
- Mengapa tidak (atau mengapa tepat) 30 triple: Hasil saya tepat mencapai 30 triple. Hal ini terjadi karena 10 solusi (kota) yang dikembalikan oleh LIMIT 10 semuanya memiliki data yang lengkap untuk ketiga pola dalam template CONSTRUCT (yaitu: `rdf:type`, `rdfs:label`, dan `ex:populasi`). Tidak ada kota yang kehilangan salah satu properti, sehingga tidak ada selisih atau triple yang "hilang".

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia
- Triple yang tetap tercetak untuk film tanpa tanggal: Triple `a schema:Movie`, `schema:name`, dan `schema:director` tetap tercetak. Triple `schema:datePublished` tidak tercetak. Tidak ada pesan error karena klausa `OPTIONAL` dalam SPARQL memang dirancang untuk tetap mengembalikan solusi (sukses) meskipun pola di dalamnya tidak ditemukan, hanya saja variabel `?rilis` akan bernilai kosong (unbound).
- Query lokal tanpa internet: Berhasil karena `demo_c.py` menyimpan hasil query pertama ke berkas lokal `film_nolan.ttl`. Query kedua (`Q_TANPA_TANGGAL`) dijalankan pada objek `Graph` yang di-parse dari berkas lokal tersebut, sehingga tidak membutuhkan koneksi internet. Jika menjalankan ulang *seluruh* `demo_c.py` tanpa internet, akan muncul error koneksi pada baris `sp.queryAndConvert()` karena gagal menghubungi endpoint DBpedia.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Karena query `CONSTRUCT` di `q_demo_b.rq` secara eksplisit mendefinisikan outputnya sebagai `?film a schema:Movie`. Tidak ada perintah untuk menyimpan `?film a dbo:Film` ke dalam graf hasil, sehingga saat di-query ulang dengan `dbo:Film`, hasilnya 0.

## Bagian C - Materialisasi
- Output demo_d.py: 
  Sebelum: 0
  Sesudah: 3
  Ada Rina: 3
- Mengapa Ada Rina bernilai 3: Karena proses materialisasi (penambahan triple turunan) hanya dijalankan sekali di awal skrip. Ketika data Rina (`ex:rina a ex:DosenTetap`) ditambahkan di akhir skrip, aturan inferensi tidak dijalankan ulang secara otomatis. Akibatnya, `ex:rina` belum memiliki triple turunan `a foaf:Person`, sehingga jumlah total `foaf:Person` tetap 3 (hanya Budi, Ani, dan Charlie).
- Output materialisasi_ulang.py: 
  Putaran 1: 4 triple baru | Person: 3
  Rina masuk | Person: 3
  Putaran 2 | Person: 4
  Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: `ex:budi a ex:DosenTetap`, `ex:ani a ex:Dosen`, dan `ex:charlie a ex:Mahasiswa`. Ini adalah triple yang sudah ada secara eksplisit di `kampus.ttl`. Bagian dari jalur `a/rdfs:subClassOf*` yang mencetaknya adalah saat panjang jalur (path length) bernilai 0 (nol), di mana operator `*` mencocokkan kelas individu tersebut dengan dirinya sendiri (misalnya: `ex:DosenTetap` dianggap sebagai subkelas dari `ex:DosenTetap`).
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Berkas terpisah ini berguna untuk isolasi data inferensi. Jika suatu hari taksonomi berubah (misalnya `ex:Dosen` bukan lagi subkelas `foaf:Person`), kita cukup membuang berkas turunan lama dan menghitung ulang tanpa merusak data eksplisit asli. Langkah manual yang tetap harus dilakukan adalah membersihkan (menghapus) triple turunan lama dari graf utama (`kampus_v4.ttl`) sebelum menambahkan hasil materialisasi baru agar tidak terjadi inkonsistensi atau duplikasi data.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | Variabel `?film` di CONSTRUCT tidak terikat di WHERE (seharusnya `?f` atau ubah WHERE jadi `?film`) | 3 triple |
| rusak_b | 4 triple | Dua nilai yang tampak sama | Joko Anwar memiliki dua `rdfs:label` dengan tag bahasa berbeda (`@id` dan `@en`), dan query mengambil semua tanpa filter bahasa | 3 triple |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Pola `?x a ex:Permukiman` tidak mengikuti jalur `rdfs:subClassOf*` untuk menelusuri hierarki kelas | 3 triple |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan (dijalankan via browser Wikidata yang sudah memiliki UA default) | Dipenuhi: Baris `UA = "KelasWebSemantik/1.0 (email@kampus.ac.id)"` mengatur agen yang bermakna. |
| 2 LIMIT | Dipenuhi: Menggunakan `LIMIT 10` di akhir query untuk membatasi jumlah solusi saat eksplorasi. | Tidak dipakai secara eksplisit, namun query sudah sangat spesifik (hanya film Christopher Nolan) sehingga hasilnya kecil dan aman. |
| 3 Simpan, jangan ulangi | Tidak relevan (hanya query eksplorasi di browser) | Dipenuhi: Graf disimpan ke `film_nolan.ttl` (`g.serialize`), lalu query kedua dijalankan secara lokal tanpa menghubungi endpoint lagi. |
| 4 Jangkar jalur | Dipenuhi: Jalur `wdt:P17 wd:Q252` (negara Indonesia) menjadi jangkar IRI tetap yang mempersempit pencarian. | Dipenuhi: Query mencari `dbo:director dbr:Christopher_Nolan`, di mana `dbr:Christopher_Nolan` adalah IRI tetap yang menjangkarkan pencarian. |

- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: 
  Query: `?kota wdt:P31/wdt:P279* ?tipe . ?tipe wdt:P17 ?negara . ?negara wdt:P31* wd:Q252 .`
  Alasan: Tanpa jangkar langsung ke `wd:Q252` (Indonesia) di awal, mesin harus mengevaluasi `?negara` dari *semua* entitas di Wikidata terlebih dahulu sebelum mencocokkannya ke Indonesia. Ini menyebabkan beban komputasi masif (full graph scan) dan sangat berisiko menyebabkan timeout di endpoint publik.

### Diskusi 1 - Taksonomi berubah
Jika suatu hari taksonomi berubah (misalnya, `ex:Dosen` diputuskan bukan lagi subkelas dari `foaf:Person`), maka triple materialisasi yang tersimpan di `kampus_v4.ttl` seperti `ex:budi a foaf:Person` menjadi salah secara semantik. Kita dapat menemukannya dengan membandingkan isi `kampus_turunan.ttl` (yang berisi riwayat inferensi) terhadap aturan hierarki yang baru. Langkah yang harus dilakukan secara manual adalah: (1) tidak memuat atau menghapus semua triple turunan lama dari graf utama, dan (2) menjalankan ulang skrip materialisasi dari awal menggunakan `kampus.ttl` yang bersih. Inilah mengapa memisahkan `kampus_turunan.ttl` (seperti di Bagian C2) sangat krusial: kita cukup timpa berkas turunan tersebut tanpa risiko menghapus atau merusak data eksplisit asli yang masih valid. Dengan pemisahan ini, proses pemeliharaan ontologi menjadi jauh lebih aman, terukur, dan tidak merusak data eksplisit asli yang masih valid di dalam sistem.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota, `SELECT` jauh lebih tepat karena dashboard membutuhkan data terstruktur (tabel) yang dapat diurutkan (misalnya `ORDER BY DESC(?populasi)`) atau dihitung agregasinya. `CONSTRUCT` lebih cocok untuk integrasi data dari tiga sumber berbeda karena dapat menormalisasi skema yang beragam menjadi satu skema target seragam. Namun, temuan Bagian A mengingatkan bahwa `CONSTRUCT` dengan `LIMIT` bisa mengecoh karena membatasi jumlah *solusi*, bukan *triple*, berpotensi menghasilkan data tidak lengkap. Selain itu, temuan `rusak_b.rq` menunjukkan bahwa penggabungan predikat (seperti `foaf:name|rdfs:label`) rentan menghasilkan duplikasi akibat perbedaan tag bahasa. Oleh karena itu, jika menggunakan `CONSTRUCT` untuk integrasi, kita wajib menambahkan `FILTER` bahasa (seperti pada `perbaikan_b.rq`) untuk memastikan satu nilai unik per entitas, atau lebih baik gunakan `SELECT` dengan `GROUP BY` dan `SAMPLE` untuk membersihkan data sebelum disimpan ke graf. Pendekatan ini menjamin integritas data saat menggabungkan berbagai sumber eksternal.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian D: `rusak_b.rq` mencetak 4 triple karena 1 solusi memiliki 2 nilai `?n` berbeda; jika sama persis, CONSTRUCT akan menggabungkannya. |
| 2 | Bagian D: `rusak_a.rq` memiliki variabel `?film` tak terikat di WHERE, menghasilkan 0 triple tanpa pesan error sama sekali. |
| 3 | Bagian D: `rusak_b.rq` menggunakan `foaf:name\|rdfs:label\|schema:name` dan `VALUES` untuk menyatukan pencarian dari beberapa predikat/nilai. |
| 4 | Bagian D: `perbaikan_c.rq` menggunakan `?x a/rdfs:subClassOf* ex:Permukiman` untuk menemukan instance tanpa menyebut kelas perantara (`ex:Kota`/`ex:Desa`). |
| 5 | Bagian C: Pada `demo_d.py`, saat Rina ditambahkan, jumlah `foaf:Person` tetap 3 sampai fungsi `materialisasi` dipanggil ulang secara eksplisit. |