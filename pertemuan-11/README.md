# Pertemuan 11 - CONSTRUCT dan Hierarki Data

## Langkah 2 - Tebak lalu cek

| Soal | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|---------|-------------|-------------------------|
| A | 3 baris | 3 baris | Hasil sesuai karena terdapat tiga kelas yang memiliki jalur menuju ex:Dosen, termasuk kelas Dosen itu sendiri. |
| B | 4 baris | 4 baris | Hasil sesuai karena Sari memiliki dua jalur menuju ex:Pegawai melalui DosenTetap dan DosenTamu. |
| C | 3 triple | 3 triple | Hasil sesuai karena Budi, Sari, dan Rudi menghasilkan tiga triple bertipe Pegawai. |
| D | 0 triple | 0 triple | Hasil sesuai karena variabel ?n tidak terikat. Rudi tidak memiliki properti ex:nama sehingga tidak ada triple yang dapat dicetak. |

## Langkah 3 - Graf kampus lokal
- Berkas sumber dan IRI dasar graf: `../pertemuan-09/kampus_usu_v2.ttl` (v3 dari Pertemuan 10 tidak tersedia, sehingga program otomatis memakai v2). IRI dasar: `https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#`. Triple awal: 34.
- Kelas dosen dan properti nama: kelas `ex:Lecturer` dan properti `foaf:name`.
- Triple hasil pemetaan: 6. Ada 3 dosen (`isa_dadi`, `opim_salim`, `umaya`), tiap dosen menghasilkan 2 triple (`a schema:Person` dan `schema:name`), jadi 3 × 2 = 6. IRI dosen tidak berubah, hanya kosakatanya yang berganti ke schema.org. Hasilnya disimpan di `dosen_schema.ttl`.
- foaf:Person sebelum / sesudah: 0 / 3. Sebelumnya dosen hanya bertipe `ex:Lecturer`, sedangkan `foaf:` hanya dipakai untuk `foaf:name`. Setelah hierarki `ex:Lecturer → ex:Pegawai → foaf:Person` ditambahkan dan dimaterialisasi (6 triple turunan baru), ketiga dosen terbaca sebagai `foaf:Person`. Mahasiswa tidak ikut karena `ex:Student` tidak ada di hierarki tersebut.
- Triple asli vs triple turunan: Dari isi `kampus_usu_v4.ttl` saja **tidak bisa** dibedakan. Setelah `g.add()`, triple turunan bercampur dengan triple asli dalam satu graf, dan Turtle tidak menyimpan asal-usul triple. Misalnya pada `ex:isa_dadi`, tiga tipe tertulis berdampingan (`a foaf:Person, ex:Lecturer, ex:Pegawai`) tanpa penanda mana yang asli (`ex:Lecturer`) dan mana yang turunan (`ex:Pegawai`, `foaf:Person`). Namun, pembedaan **bisa dilakukan dengan membandingkan versi**: hasil `v4 - v2` menunjukkan selisih 8 triple (v2: 34, v4: 42), yaitu 6 triple turunan (`a ex:Pegawai` dan `a foaf:Person` untuk tiga dosen) dan 2 triple `rdfs:subClassOf` dari `INSERT DATA`. Jadi asal-usul triple harus dilacak dari luar berkas, misalnya lewat perbandingan versi atau named graph.
- Dosen baru setelah program selesai: Dosen baru **tidak otomatis** menjadi `ex:Pegawai` atau `foaf:Person`. Materialisasi adalah snapshot: triple turunan dihitung sekali lalu disimpan sebagai fakta biasa. Dosen baru hanya punya `a ex:Lecturer`, sehingga program harus dijalankan ulang agar triple turunannya dibuat. Kelebihan materialisasi: query cepat dan sederhana tanpa property path. Kekurangannya: data bisa basi dan ukuran berkas bertambah. Alternatifnya, hierarki dihitung saat query dengan `a/rdfs:subClassOf*`, yang selalu mutakhir tetapi lebih lambat.

## Langkah 4 - Wikidata
Jumlah triple Q6: 150 triple (asumsi query mengembalikan 50 baris data, karena setiap baris menghasilkan 3 triple).
Jumlah baris Q6 versi SELECT: 50 baris (sesuai dengan LIMIT 50).
Penjelasan perbedaan: Pada query CONSTRUCT, setiap 1 baris hasil pemetaan variabel (?univ, ?nama, ?kota) akan dipecah dan dibuatkan menjadi 3 triple RDF baru, yaitu: ?univ a ex:Universitas, ?univ ex:nama ?nama, dan ?univ ex:lokasi ?kota. Sedangkan pada query SELECT, hasilnya hanya ditampilkan dalam bentuk tabel baris dan kolom tanpa membuat triple baru. Oleh karena itu, jumlah triple pada CONSTRUCT selalu sama dengan 3 × jumlah baris pada SELECT.
Q7 dengan + vs *:
wdt:P279+ (satu atau lebih): Mencari semua subkelas dari "universitas" (wd:Q3918) secara transitif (anak, cucu, cicit, dst.), tetapi tidak menyertakan entitas "universitas" (wd:Q3918) itu sendiri.
wdt:P279* (nol atau lebih): Mencari semua subkelas secara transitif dan bersifat refleksif, sehingga entitas "universitas" (wd:Q3918) itu sendiri juga ikut muncul di dalam hasil query.
Kelas yang mengejutkan dan alasannya:
Kelas: wd:Q30716008 (coast guard academy / akademi penjaga pantai) atau wd:Q42058997 (naval academy / akademi angkatan laut).
Alasan: Secara awam, universitas sering diasosiasikan dengan institusi pendidikan tinggi umum/sekuler. Akademi militer atau penjaga pantai lebih sering dianggap sebagai tempat pelatihan fisik dan taktis ketentaraan. Namun, secara ontologi di Wikidata, banyak akademi militer modern yang memiliki kurikulum akademik terakreditasi penuh dan berhak memberikan gelar Sarjana (S1) atau Magister (S2). Karena fungsi utamanya mencakup pemberian gelar pendidikan tinggi, secara hierarkis entitas ini sah diklasifikasikan sebagai subkelas dari "universitas".

## Refleksi

**1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?**

Karena hasil CONSTRUCT berbentuk graf RDF yang tidak menyimpan triple yang sama lebih dari satu kali. Jadi, meskipun ada beberapa baris SELECT yang menghasilkan triple identik, triple tersebut hanya dihitung satu kali. Selain itu, jika ada variabel yang tidak memiliki nilai, triple tersebut tidak akan ikut dihasilkan.

**2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?**

Triple turunan yang sudah ada di kampus_usu_v4.ttl tidak otomatis berubah mengikuti taksonomi yang baru. Jadi, kita perlu menjalankan kembali program materialisasi agar triple turunannya sesuai dengan perubahan hierarki kelas terbaru.

**3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?**

CSV digunakan ketika hasil query berbentuk data tabel yang berisi baris dan kolom, misalnya jumlah universitas berdasarkan kota. Sedangkan Turtle digunakan ketika ingin menyimpan data dalam bentuk graf RDF yang menunjukkan hubungan antara satu data dengan data lainnya.

