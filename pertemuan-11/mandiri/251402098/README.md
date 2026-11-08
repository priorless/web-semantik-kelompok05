# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: tepat 30, karena LIMIT 10 membatasi 10 solution, bukan triple. Tiap solution mencetak 3 pola template (a ex:Kota, rdfs:label, ex:populasi), jadi batas atasnya 10 × 3 = 30. Pada hasil saya, ke-10 solution adalah 10 kota berbeda dengan satu populasi masing-masing. Karena itu tidak ada triple kembar yang digabung, dan batas atas 30 tercapai. Pola a ex:Kota dan rdfs:label baru akan mencetak triple kembar jika satu kota muncul di lebih dari satu solution (misalnya punya beberapa nilai populasi), dan itu tidak terjadi di data saya.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia (endpoint https://dbpedia.org/sparql)
- Triple yang tetap tercetak untuk film tanpa tanggal: tiga triple, yaitu a schema:Movie, schema:name, dan schema:director dbr:Christopher_Nolan. Yang tidak tercetak hanya schema:datePublished. Pada hasil saya semua 16 film tidak punya dbo:releaseDate, sehingga tiap film hanya mencetak 3 triple (16 x 3 = 48). Tidak ada pesan error karena ?rilis berada di OPTIONAL: bila tidak cocok, variabelnya tak terikat, dan triple template yang memuat variabel tak terikat dilewati diam-diam, bukan dianggap kesalahan.
- Query lokal tanpa internet: Q_TANPA_TANGGAL berhasil karena dijalankan pada film_nolan.ttl, berkas di laptop. rdflib memuatnya ke memori dan mengeksekusi SPARQL di sana, tanpa menghubungi DBpedia. Jika seluruh demo_c.py dijalankan tanpa internet, program gagal di sp.queryAndConvert() (error koneksi) di langkah pertama, sebelum berkas disimpan dan sebelum query lokal tercapai.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: berkas itu berisi hasil template CONSTRUCT, yaitu a schema:Movie. dbo:Film hanya ada di WHERE (data sumber di DBpedia) dan tidak pernah ditulis ke berkas, sehingga pola ?f a dbo:Film tidak cocok dengan apa pun.
- Query lokal tanpa internet: hasilnya 16. Berhasil karena datanya sudah ada di berkas laptop. Jika demo_c.py dijalankan offline, program error karena tidak bisa menghubungi DBpedia.

## Bagian C - Materialisasi
- Output demo_d.py: [isi]
- Mengapa Ada Rina bernilai 3: [jawaban]
- Output materialisasi_ulang.py: [isi]
- Tiga triple yang bukan baru: [jawaban]
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: [jawaban]

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | [isi] | [isi] | [isi] | [isi] |
| rusak_b | [isi] | [isi] | [isi] | [isi] |
| rusak_c | [isi] | [isi] | [isi] | [isi] |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | [isi] | [isi] |
| 2 LIMIT | [isi] | [isi] |
| 3 Simpan, jangan ulangi | [isi] | [isi] |
| 4 Jangkar jalur | [isi] | [isi] |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: [isi]

### Diskusi 1 - Taksonomi berubah
[150-250 kata]

### Diskusi 2 - SELECT atau CONSTRUCT
[150-250 kata]

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | [isi] |
| 2 | [isi] |
| 3 | [isi] |
| 4 | [isi] |
| 5 | [isi] |