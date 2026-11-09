# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: tepat 30. `LIMIT 10` membatasi 10 solution, bukan triple. Tiap solution mencetak 3 pola template (`a ex:Kota`, `rdfs:label`, `ex:populasi`), jadi batas atasnya 10 x 3 = 30. Pada hasil saya, ke-10 solution adalah 10 kota berbeda dengan satu populasi masing-masing, sehingga tidak ada triple kembar yang digabung dan batas atas tercapai. Pola `a ex:Kota` dan `rdfs:label` baru mencetak triple kembar jika satu kota muncul di lebih dari satu solution (misalnya punya beberapa nilai populasi), dan itu tidak terjadi di data saya.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia (endpoint https://dbpedia.org/sparql)
- Triple yang tetap tercetak untuk film tanpa tanggal: tiga triple, yaitu `a schema:Movie`, `schema:name`, dan `schema:director dbr:Christopher_Nolan`. Yang tidak tercetak hanya `schema:datePublished`. Pada hasil saya semua 16 film tidak punya `dbo:releaseDate`, sehingga tiap film hanya mencetak 3 triple (16 x 3 = 48). Tidak ada pesan error karena `?rilis` berada di `OPTIONAL`: bila tidak cocok, variabelnya tak terikat, dan triple template yang memuat variabel tak terikat dilewati diam-diam, bukan dianggap kesalahan.
- Query lokal tanpa internet: hasilnya 16. Berhasil karena datanya sudah ada di berkas laptop. Jika demo_c.py dijalankan offline, program error karena tidak bisa menghubungi DBpedia.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: berkas itu berisi hasil template CONSTRUCT, yaitu `a schema:Movie`. `dbo:Film` hanya ada di WHERE (data sumber di DBpedia) dan tidak pernah ditulis ke berkas, sehingga pola `?f a dbo:Film` tidak cocok dengan apa pun.

## Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0, Sesudah: 3, Ada Rina: 3
- Mengapa Ada Rina bernilai 3: materialisasi hanya menyimpan kesimpulan untuk data yang ada saat aturan dijalankan. Rina masuk sesudahnya dan hanya punya `a ex:DosenTetap`. SPARQL tidak menyimpulkan sendiri, jadi ia belum dihitung sebagai `foaf:Person` sampai aturan dijalankan ulang.
- Output materialisasi_ulang.py: Putaran 1: 4 triple baru | Person: 3; Rina masuk | Person: 3; Putaran 2 | Person: 4; Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: `ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, `ex:andi a ex:Mahasiswa`. Dicetak oleh langkah nol dari `rdfs:subClassOf*` (arti `*` adalah nol atau lebih), jadi hasilnya sama dengan data asli. 7 - 4 = 3.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: berkas ini memisahkan kesimpulan dari fakta asli. Kalau `ex:Dosen` tidak lagi subkelas `foaf:Person`, cukup berkas ini yang dibuang dan dibuat ulang, sedangkan fakta di `kampus.ttl` tidak tersentuh. Di `kampus_v4.ttl` fakta dan kesimpulan bercampur sehingga tidak bisa dipisahkan. Yang masih manual: memperbarui `rdfs:subClassOf` di `kampus.ttl`, menjalankan ulang aturan, lalu mengganti turunan lama dengan yang baru.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error| Baris `?f dbo:director ...` mengikat `?f`, sedangkan template memakai `?film`, sehingga variabel template tak terikat. | 3 triple (`?f` diganti `?film`) |
| rusak_b | 4 triple | Dua nilai yang tampak sama | Baris `?o foaf:name\|rdfs:label\|schema:name ?n` memberi nama Nolan dengan dan tanpa tag `@en`, dua literal berbeda yang tidak digabung. | 3 triple (ditambah `BIND(STR(?n) AS ?nama)`) |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Baris `?x a ex:Permukiman` hanya cocok dengan tipe langsung, tanpa jalur `rdfs:subClassOf*`. | 3 triple: Medan, Surabaya, Tomok (dipakai `a/rdfs:subClassOf*`) |

Versi perbaikan disimpan di `perbaikan_a.rq`, `perbaikan_b.rq`, dan `perbaikan_c.rq`.

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak ada baris di berkas; query dijalankan lewat browser (query.wikidata.org) yang mengirim User-Agent sendiri, jadi aturan ini tidak relevan di berkas | `UA = "KelasWebSemantik/1.0 (email@...)"` dan `SPARQLWrapper(..., agent=UA)` |
| 2 LIMIT | Baris `LIMIT 10` | Tidak ada LIMIT; query berjangkar `dbr:Christopher_Nolan` sehingga hasilnya kecil (48 triple untuk 16 film) |
| 3 Simpan, jangan ulangi | Tidak dipenuhi: query dijalankan 3 kali (LIMIT 10, LIMIT 30, SELECT). Lebih baik unduh hasil sekali sebagai `.ttl` | `g.serialize("film_nolan.ttl")`, lalu query kedua dijalankan lokal dari berkas |
| 4 Jangkar jalur | `wdt:P31/wdt:P279* wd:Q515` berjangkar di Q515 (ujung kanan), ditambah `wdt:P17 wd:Q252` | Tidak ada jalur `*` atau `+`; pola `dbo:director dbr:Christopher_Nolan` berjangkar IRI |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:

```sparql
PREFIX ex: <http://contoh.id/>
CONSTRUCT {
  ?kota a ex:Kota ;
        rdfs:label ?namaKota ;
        ex:populasi ?populasi .
}
WHERE {
  ?kota wdt:P31/wdt:P279* ?kelas ;
        wdt:P17 wd:Q252 ;
        wdt:P1082 ?populasi ;
        rdfs:label ?namaKota .
  FILTER ( LANG(?namaKota) = "id" )
}
LIMIT 10
```

Alasan: baris `wd:Q515` diganti `?kelas`, sehingga jalur `P31/P279*` berangkat dari dua variabel. Mesin harus menelusuri rantai subkelas dari tipe setiap item yang cocok, sampai kelas paling atas, tanpa titik awal yang menyempitkan pencarian. Setiap kota juga cocok dengan semua superkelasnya, sehingga satu kota menghasilkan banyak solution. `LIMIT` hanya memotong hasil di akhir, bukan pekerjaan telusurnya. Akibatnya timeout dan beban berat bagi server publik.

### Diskusi 1 - Taksonomi berubah
Pada Demo D, materialisasi menyimpan kesimpulan sebagai triple biasa. Misalkan setahun kemudian `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`. Triple yang kini salah adalah tiga yang diturunkan lewat sisi itu: `ex:budi a foaf:Person`, `ex:sari a foaf:Person`, dan `ex:rina a foaf:Person`. Triple `ex:andi a foaf:Person` tetap benar karena berasal dari `ex:Mahasiswa`.

Masalahnya, di `kampus_v4.ttl` (16 triple) fakta asli dan kesimpulan tercampur. `ex:budi a ex:DosenTetap` adalah fakta, sedangkan `ex:budi a ex:Dosen` adalah turunan, dan keduanya tampak sama, sehingga tidak ada cara membedakannya. Di `kampus_turunan.ttl` (6 triple) semua kesimpulan sudah terpisah. Cara menemukannya: ubah `kampus.ttl`, jalankan ulang ATURAN pada fakta asli (hasilnya tidak lagi memuat tiga triple tersebut), lalu bandingkan dengan `kampus_turunan.ttl`. Selisihnya adalah triple yang harus dihapus, dan sisanya ditambahkan. Menghapus semua triple `foaf:Person` begitu saja berisiko, karena sebuah triple bisa tetap sah lewat jalur lain (andi).

Pengalaman Demo D juga menunjukkan hal sebaliknya: saat Rina masuk, jumlah Person tetap 3 sampai aturan dijalankan ulang (putaran 2 menjadi 4). Jadi materialisasi mudah usang ke dua arah, baik karena data baru maupun karena taksonomi berubah, dan menyimpannya terpisah membuat perbaikan menjadi diff yang jelas, bukan penelusuran manual.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota saya memakai SELECT. Dashboard membutuhkan tabel baris dan satu angka per kota, sedangkan CONSTRUCT mengembalikan graf. Pada Bagian A, 10 solution pertama saya memang berisi 10 kota berbeda sehingga hasilnya tepat 30 triple. Namun data Wikidata tidak menjamin satu populasi per kota, karena `wdt:P1082` dapat berisi beberapa sensus. Contohnya ada di `kota.ttl`: Medan memiliki 2435252 dan 2097610. Pada CONSTRUCT, kedua nilai menjadi triple terpisah tanpa keterangan tahun, sedangkan dengan SELECT saya bisa memilih satu nilai lewat `ORDER BY`, `MAX`, atau `SAMPLE`.

Untuk menggabungkan data kota dari tiga sumber saya memakai CONSTRUCT, karena tujuannya memetakan vokabuler yang berbeda ke satu skema (seperti `ex:nama`) dan hasilnya tetap berupa graf yang bisa disimpan lalu di-query lagi. Tetapi penggabungan tidak otomatis menyatukan nilai. Bukti dari `rusak_b`: nama Nolan dari `foaf:name` (tanpa tag) dan `rdfs:label` (`@en`) menghasilkan 4 triple, bukan 3, karena dua literal itu dianggap berbeda. Setelah `STR()` jumlahnya 3. Pada penggabungan tiga sumber, tag bahasa dan tipe data harus dinormalkan di dalam query CONSTRUCT, jika tidak, duplikat semu akan merusak hitungan di dashboard.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: `LIMIT 10` menghasilkan 30 triple (10 solution x 3 pola) dan `LIMIT 30` menghasilkan 90 (30 x 3), jadi template dicetak sekali per solution. Penggabungan triple kembar: `perbaikan_c` memberi 3 triple untuk Medan, Surabaya, Tomok, padahal Medan cocok lewat dua jalur (`ex:KotaMetropolitan` dan `ex:KotaDiIndonesia`) dan triple-nya identik; `rusak_b` 4 triple menjadi 3 setelah `STR()` karena dua nilai Nolan menjadi sama |
| 2 | `rusak_a` menghasilkan 0 triple tanpa error karena `?film` tak terikat; di Bagian B, 16 film tanpa `dbo:releaseDate` tidak mencetak `schema:datePublished` dan tidak ada error |
| 3 | `rusak_b`: jalur `\|` dan `VALUES` menyatukan `foaf:name`, `rdfs:label`, `schema:name` dari 3 orang menjadi `ex:nama` (4 triple, lalu 3 setelah `STR()`) |
| 4 | `perbaikan_c`: `a/rdfs:subClassOf*` menemukan Medan, Surabaya, Tomok (3 triple) tanpa menyebut `ex:Kota`, `ex:Desa`, atau `ex:KotaMetropolitan`. Demo D: budi terhubung ke `foaf:Person` tanpa menyebut `ex:Dosen` |
| 5 | Demo D: Sebelum 0, Sesudah 3, tetapi Ada Rina tetap 3 (tidak ikut). Setelah dihitung ulang, Putaran 2 menjadi 4 dan triple turunan 6 |