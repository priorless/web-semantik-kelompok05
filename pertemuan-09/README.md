
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
