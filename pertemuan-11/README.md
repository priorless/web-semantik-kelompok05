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

## Refleksi

**1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?**

Karena hasil CONSTRUCT berbentuk graf RDF yang tidak menyimpan triple yang sama lebih dari satu kali. Jadi, meskipun ada beberapa baris SELECT yang menghasilkan triple identik, triple tersebut hanya dihitung satu kali. Selain itu, jika ada variabel yang tidak memiliki nilai, triple tersebut tidak akan ikut dihasilkan.

**2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?**

Triple turunan yang sudah ada di kampus_usu_v4.ttl tidak otomatis berubah mengikuti taksonomi yang baru. Jadi, kita perlu menjalankan kembali program materialisasi agar triple turunannya sesuai dengan perubahan hierarki kelas terbaru.

**3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?**

CSV digunakan ketika hasil query berbentuk data tabel yang berisi baris dan kolom, misalnya jumlah universitas berdasarkan kota. Sedangkan Turtle digunakan ketika ingin menyimpan data dalam bentuk graf RDF yang menunjukkan hubungan antara satu data dengan data lainnya.

