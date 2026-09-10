# Latihan Pertemuan 3 - JSON-LD dan Structured Data

## Identitas
- Nama: Dian Indriani
- NIM: 241502040

## 1. JSON Biasa dan JSON-LD
1. Apa perbedaan fungsi antara pasangan nama/pekerjaan dan name/jobTitle?
jawaban: Nama dan pekerjaan merupakan pasangan kunci-nilai lokal yang hanya dipahami secara internal, sedangan name/jobTitle merupakan suatu properti yang terhubung ke kosakata global Schema.org.

2. Apa fungsi @context, @type, dan @id?
jawaban: @context: Memetakan istilah/kunci lokal ke URI/IRI kosakata standar global
@type: Menentukan tipe entitas objek yang sedang dibahas. Contoh place, person, dll.
@id: Menjadi pengenal unik berformat IRI/URI untuk node tersebut di tingkat web.

3. Apa yang terjadi pada sebuah node jika tidak memiliki @id?
jawaban:Jika sebuah node tidak memiliki @id, maka node tersebut dianggap sebagai node kosong. Datanya tetap valid, tetapi entitas tersebut tidak dapat dirujuk secara langsung dari luar. 


## 4. Triple dari JSON-LD Playground
Tuliskan satu baris N-Quads yang terbentuk:

```
<https://usu.ac.id/mhs/251402137> <http://schema.org/name> "Quinsha Ilmi Azzahra" .
```

## 5. Hasil Validasi
- Schema Markup Validator: 5 item `Person` terdeteksi, tidak ada kesalahan dan tidak ada peringatan.
- Rich Results Test: 1 item valid terdeteksi. Data terstruktur yang terdeteksi adalah `Acara`. Masalah non-kritis terdeteksi.
- JSON-LD Playground: N-Quads berhasil terbentuk.

## 6. Refleksi

1. Mengapa `@context` disebut jembatan menuju makna?  
   Karena `@context` menghubungkan data yang kita tulis dengan kosakata yang memiliki makna, seperti `schema.org`. Jadi, data yang awalnya hanya berupa teks dapat dipahami maksudnya.

2. Apa perbedaan fungsi Schema Markup Validator dan Rich Results Test?  
   Schema Markup Validator digunakan untuk mengecek apakah tipe dan properti yang digunakan sudah sesuai dengan `schema.org`. Sementara itu, Rich Results Test digunakan untuk melihat apakah data terstruktur tersebut memenuhi syarat untuk ditampilkan sebagai hasil kaya di Google.

3. Mengapa isi JSON-LD harus sama dengan konten yang terlihat pada halaman?  
   Karena informasi dalam JSON-LD harus sesuai dengan informasi yang benar-benar ada di halaman. Dengan begitu, data yang dibaca mesin tidak berbeda dengan informasi yang dilihat oleh pengunjung.