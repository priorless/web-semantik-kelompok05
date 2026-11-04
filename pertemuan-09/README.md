
# Pertemuan 9 - SPARQL Dasar: Tell & Ask dan Endpoint

## Langkah 1 - Tabel Binding

| Tahap | ?dosen | ?mk | ?namaMK |
|-------|--------|-----|---------|
| Pola 1, baris 1 | ex:budi | ex:tif2305 | - |
| Pola 1, baris lain | ex:sari | ex:tif2410 | - |
| Pola 1, baris lain | ex:sari | ex:tif2305 | - |
| Pola 2, baris 1 | - | ex:tif2305 | Web Semantik |
| Pola 2, baris 2 | - | ex:tif2410 | Data Mining |
| Hasil akhir | ex:budi | ex:tif2305 | Web Semantik |
| Hasil akhir | ex:sari | ex:tif2410 | Data Mining |
| Hasil akhir | ex:sari | ex:tif2305 | Web Semantik |

- Jumlah baris hasil akhir: 3 baris.
- Peran ?mk: Variabel ?mk digunakan untuk menghubungkan pola pertama dan pola kedua. Walaupun tidak ditampilkan pada SELECT, variabel ini tetap digunakan untuk mencocokkan mata kuliah yang diajar oleh dosen dengan nama mata kuliah yang tersedia.



## Refleksi

**1. Di titik mana SPARQL berbeda dari SQL?**

SPARQL digunakan untuk mengambil informasi dari graf RDF berdasarkan hubungan antar data, sedangkan SQL digunakan untuk mengelola dan mengambil data dari tabel dalam database relasional. Perbedaannya terlihat dari cara pencarian datanya, SPARQL menggunakan pola triple untuk mencocokkan informasi, sementara SQL menggunakan tabel dan relasi antar tabel.

**2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?**

Graf lokal menggunakan rdflib ketika ingin mengelola, menambahkan, atau menguji data RDF milik sendiri. Sedangkan endpoint publik digunakan ketika ingin mencari informasi dari sumber data online seperti Wikidata tanpa harus menyimpan seluruh datanya secara lokal.

**3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.**

Hasil query yang cukup menarik adalah ketika satu dosen muncul lebih dari satu kali pada hasil SELECT. Hal ini terjadi karena dosen tersebut mengajar lebih dari satu mata kuliah. Jadi, satu dosen bisa memiliki beberapa hubungan dengan mata kuliah yang berbeda di dalam graf RDF.
