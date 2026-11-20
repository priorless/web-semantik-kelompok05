# Pertemuan 12 - Inferensi dan Reasoning

## Langkah 1 - Closure dengan tangan
| # | Triple turunan | Aturan | Premis |
|---|----------------|--------|--------|
| 1 | `ex:budi a ex:Dosen` | rdfs2 | `ex:membimbing rdfs:domain ex:Dosen` + `ex:budi ex:membimbing ex:andi` |
| 2 | `ex:andi a ex:Mahasiswa` | rdfs3 | `ex:membimbing rdfs:range ex:Mahasiswa` + `ex:budi ex:membimbing ex:andi` |
| 3 | `ex:budi ex:mengenal ex:andi` | rdfs7 | `ex:membimbing rdfs:subPropertyOf ex:mengenal` + `ex:budi ex:membimbing ex:andi` |
| 4 | `ex:sari a ex:Dosen` | rdfs9 | `ex:DosenTamu rdfs:subClassOf ex:Dosen` + `ex:sari a ex:DosenTamu` |
| 5 | `ex:DosenTamu rdfs:subClassOf ex:Pegawai` | rdfs11 | `ex:DosenTamu rdfs:subClassOf ex:Dosen` + `ex:Dosen rdfs:subClassOf ex:Pegawai` |
| 6 | `ex:Dosen rdfs:subClassOf ex:Orang` | rdfs11 | `ex:Dosen rdfs:subClassOf ex:Pegawai` + `ex:Pegawai rdfs:subClassOf ex:Orang` |
| 7 | `ex:budi a ex:Pegawai` | rdfs9 | `ex:Dosen rdfs:subClassOf ex:Pegawai` + `ex:budi a ex:Dosen`|
| 8 | `ex:budi a ex:Orang` | rdfs9 | `ex:Pegawai rdfs:subClassOf ex:Orang` + `ex:budi a ex:Pegawai` |
| 9 | `ex:andi a ex:Orang` | rdfs9 | `ex:Mahasiswa rdfs:subClassOf ex:Orang` + `ex:andi a ex:Mahasiswa` |
| 10 | `ex:sari a ex:Pegawai` | rdfs9 | `ex:Dosen rdfs:subClassOf ex:Pegawai` + `ex:sari a ex:Dosen` |
| 11 | `ex:sari a ex:Orang` | rdfs9 | `ex:Pegawai rdfs:subClassOf ex:Orang` + `ex:sari a ex:Pegawai`|
| 12 | `ex:DosenTamu rdfs:subClassOf ex:Orang` | rdfs11 | `ex:DosenTamu rdfs:subClassOf ex:Dosen` + `ex:Dosen rdfs:subClassOf ex:Orang`|

- Jumlah triple turunan bermakna: **12 triple** (8 triple `rdf:type`, 1 triple `ex:mengenal`, dan 3 triple `rdfs:subClassOf`). Triple umum bawaan seperti `rdfs:Resource` atau `rdf:Property` diabaikan.
- Triple yang baru ditemukan di putaran kedua: `ex:budi a ex:Pegawai`, `ex:budi a ex:Orang`, `ex:andi a ex:Orang`, `ex:sari a ex:Pegawai`, `ex:sari a ex:Orang`, dan `ex:DosenTamu rdfs:subClassOf ex:Orang`. Semuanya baru bisa diturunkan setelah memakai hasil dari putaran pertama sebagai premis baru (misalnya `ex:andi a ex:Orang` baru muncul setelah `ex:andi a ex:Mahasiswa` didapatkan dari `rdfs3`).
- Triple asserted yang tidak menurunkan apa pun, dan alasannya: `ex:andi a ex:MahasiswaBerprestasi`. Karena di skema tidak ada aturan `ex:MahasiswaBerprestasi rdfs:subClassOf ...`, aturan `rdfs9` tidak bisa dijalankan. Jadi reasoner tidak bisa menebak dari kemiripan nama kelas saja bahwa `MahasiswaBerprestasi` adalah bagian dari `Mahasiswa` (Andi jadi `ex:Mahasiswa` murni karena `rdfs:range` dari `ex:membimbing`).


## Langkah 2 - Tebak lalu cek

| Soal | Profil | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|--------|---------|-------------|-------------------------|
| A | RDFS | 3 baris | 3 baris | Tebakan sesuai dengan hasil mesin. |
| B | OWL RL | 10 baris | 10 baris | Tebakan sesuai dengan hasil mesin. |
| C | RDFS | 0 baris | 0 baris | Tebakan sesuai dengan hasil mesin. |
| C | OWL RL | 1 baris | 1 baris | Tebakan sesuai dengan hasil mesin. |
| D | OWL RL | False | False | Tebakan sesuai dengan hasil mesin. |

### Penjelasan Hasil

- **A:** Terdapat 3 individu yang termasuk kelas Orang, yaitu Budi, Sari, dan Andi. Budi menjadi Dosen melalui domain properti membimbing, Sari menjadi Dosen melalui hierarki subkelas DosenTamu, sedangkan Andi menjadi Mahasiswa melalui range properti membimbing. Ketiganya kemudian dapat disimpulkan sebagai Orang.

- **B:** Terdapat 10 hubungan beradaDi karena properti tersebut memiliki sifat transitif. Dari 5 lokasi yang saling terhubung, reasoner dapat menurunkan hubungan langsung maupun tidak langsung.

- **C (RDFS):** Hasilnya 0 baris karena profil RDFS tidak mengenali owl:inverseOf. Oleh karena itu, hubungan dibimbing tidak dapat diturunkan.

- **C (OWL RL):** Hasilnya 1 baris karena OWL RL mengenali owl:inverseOf. Dari triple Budi membimbing Andi, reasoner menurunkan triple Andi dibimbing Budi.

- **D:** Hasilnya False karena tidak terdapat informasi yang membuktikan bahwa Medan merupakan anggota kelas Tempat. Berdasarkan prinsip dunia terbuka, informasi yang tidak ditemukan tidak otomatis dianggap salah.

### Kesimpulan

Seluruh tebakan pada latihan ini sesuai dengan hasil yang diperoleh dari program Python. Perbedaan profil RDFS dan OWL RL terlihat pada kemampuan OWL RL dalam menggunakan aksioma OWL, seperti owl:inverseOf dan owl:TransitiveProperty.

## Langkah 3 - Reasoner pada graf kampus

- **Berkas sumber dan IRI dasar graf:**  
  `../pertemuan-09/kampus_usu_v2.ttl` |  
  `https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#`

- **Statistik Graf:**  
  Asserted: **38** | Closure: **99** | Inferred: **61** | Bermakna: **8**

- **Triple di v4 yang tidak ada di asserted:**  
  **6** triple (merupakan hasil materialisasi hierarki kelas dari Pertemuan 11).

- **Turunan yang muncul karena domain dan range `ex:mengajar`:**  
  Berdasarkan isi `kampus_usu_inferred.ttl`, aturan domain dan range menghasilkan turunan berikut:
  1.  **Range (`rdfs:range ex:Course`)**: Individu `ex:mk_baru_pertemuan09` yang sebelumnya hanya memiliki properti nama, kini otomatis mendapatkan tipe `rdf:type ex:Course` karena menjadi objek dari properti `ex:mengajar`.
  2.  **Domain (`rdfs:domain ex:Lecturer`)**: Ketiga dosen (`isa_dadi`, `opim_salim`, `umaya`) yang menggunakan properti `ex:mengajar` secara implisit bertipe `ex:Lecturer`. Melalui rantai subclass (`Lecturer ⊑ Pegawai ⊑ foaf:Person`), reasoner juga menurunkan triple `a ex:Pegawai` dan `a foaf:Person` untuk ketiganya.
  3.  **Transitivitas**: Muncul triple `ex:Lecturer rdfs:subClassOf foaf:Person` sebagai hasil inferensi transitif dari hierarki kelas yang didefinisikan.

- **Bila menambah dosen baru:**  
  Cukup menambahkan fakta asserted (data mentah) dosen baru ke dalam berkas sumber `kampus_usu_v2.ttl` (contoh: `ex:dosenBaru ex:mengajar ex:mkBaru .`). Setelah itu, jalankan ulang skrip `reasoner_lokal.py`. Reasoner akan menghitung ulang *closure* dan menghasilkan semua triple turunan (tipe Lecturer, Pegawai, Person, Course) secara otomatis tanpa perlu penulisan manual, berbeda dengan pendekatan materialisasi statis di Pertemuan 11.
  
## Langkah 4 - Wikidata
- ?n Q8 / Q9: 877 / 1343
- Penyebab selisih: Q8 hanya menghitung entitas yang statement `P31`-nya langsung menunjuk ke `Q3918` (universitas), sehingga hasilnya 877. Banyak universitas di Wikidata dicatat dengan kelas yang lebih spesifik, misalnya politeknik, universitas swasta, dan universitas negeri, yang baru terhubung ke `Q3918` lewat rantai `P279` (*subclass of*).
  Q9 memakai `P31/P279*`, sehingga ikut menghitung instance dari semua subkelas universitas dan hasilnya 1343, selisih 466. Hierarki kelas yang disimpan Wikidata sama untuk kedua query, tetapi hanya Q9 yang menelusurinya. Karena tanda `*` mencakup nol langkah, instance langsung tetap terhitung, sehingga Q9 >= Q8 (1343 >= 877).
- Satu subkelas yang menyumbang selisih: Politeknik (`wd:Q845392`) dengan 375 universitas Indonesia, disusul universitas swasta (`wd:Q902104`) dengan 320 dan universitas negeri (`wd:Q875538`) dengan 73.
  Total seluruh baris query bantu (801) lebih besar dari selisih 466 karena satu entitas bisa punya beberapa nilai `P31` dan sebagian juga sudah dicatat langsung sebagai `Q3918` sehingga terhitung di Q8.
  Q7 Pertemuan 11 hanya mendaftar subkelas universitas (`P279+ Q3918`) tanpa menghitung instance dan tanpa filter Indonesia, sedangkan query bantu menghitung universitas Indonesia per subkelas dan menghasilkan 14 kelas.
  Politeknik tidak tampil di hasil Q7 Pertemuan 11 karena Q7 memakai `LIMIT 30` sehingga daftarnya terpotong. Setelah `LIMIT` dihapus, politeknik muncul, jadi politeknik memang subkelas universitas yang terhubung ke `Q3918` lewat `P279+`.
- WDQS: materialisasi, saat query, atau tidak keduanya: **Tidak keduanya.**
  - Bukan materialisasi, karena triple turunan seperti `?univ wdt:P31 wd:Q3918` untuk instance subkelas tidak disimpan. Yang tersimpan hanya data asserted.
  - Bukan penalaran otomatis, karena tanpa `/wdt:P279*` Q8 tidak menalar sama sekali.
  - Yang terjadi adalah penelusuran jalur (*property path*) saat query dijalankan. Aturan `rdfs9` (instance dari subkelas juga instance dari superkelasnya) ditulis sendiri oleh penulis query dalam bentuk `P31/P279*`, lalu dievaluasi oleh mesin query.
  - Jadi yang menjalankan `rdfs9` di Q9 adalah saya lewat pola query, bukan sebuah reasoner.


  ## Langkah 5 - Konsistensi

- **Pesan galat RDFS / OWL RL:** Pada kondisi sebelum perbaikan, RDFS menghasilkan 0 pesan galat, sedangkan OWL RL menghasilkan 2 pesan galat.
- **Individu yang disebut pesan:** `isa_dadi` dan `web_semantik`. Keduanya terdeteksi sebagai individu yang termasuk dalam kelas `Pegawai` sekaligus `Course`, padahal kedua kelas tersebut telah dinyatakan saling terpisah menggunakan `owl:disjointWith`.
- **Setelah baris terbalik dihapus:** RDFS menghasilkan 0 pesan galat dan OWL RL juga menghasilkan 0 pesan galat.
- **Isi `laporan_kelas.csv` sebelum dan sesudah:**
  
  Sebelum perbaikan:
  | kelas | asserted | rdfs | owl_rl |
  |---|---:|---:|---:|
  | Lecturer | 3 | 4 | 4 |
  | Pegawai | 0 | 4 | 4 |
  | Course | 3 | 5 | 5 |

  Sesudah perbaikan:
  | kelas | asserted | rdfs | owl_rl |
  |---|---:|---:|---:|
  | Lecturer | 3 | 3 | 3 |
  | Pegawai | 0 | 3 | 3 |
  | Course | 3 | 4 | 4 |

- **Dari mana dosen menjadi mata kuliah:** Hal ini terjadi karena properti `mengajar` memiliki `rdfs:range ex:Course`. Ketika terdapat triple yang menyatakan seorang dosen sebagai objek dari properti `mengajar`, reasoner menyimpulkan bahwa dosen tersebut merupakan anggota kelas `Course`. Selain itu, `rdfs:domain ex:Lecturer` membuat subjek dari properti `mengajar` disimpulkan sebagai `Lecturer`. Karena `Lecturer` merupakan subclass dari `Pegawai`, individu tersebut juga disimpulkan sebagai `Pegawai`.