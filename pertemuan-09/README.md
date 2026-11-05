
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


## Langkah 2 - ASK dan dunia terbuka
1. Apa hasil ASK { ex:budi ex:mengajar ex:tif2410 }? Bagaimana tafsir yang tepat menurut asumsi dunia terbuka?

**Hasil query               :** `FALSE`

**Penjelasan & Tafsir OWA   :**  
Dalam *Open World Assumption* (OWA) yang digunakan pada Web Semantik, hasil `FALSE` pada query `ASK` bukan berarti Pak Budi pasti tidak mengajar TIF2410 secara mutlak di dunia nyata. Hasil `FALSE` di sini hanya bermakna bahwa kebenaran/triple tersebut saat ini tidak ada/tidak tertulis (unknown/not asserted) di dalam basis data RDF tempat query dijalankan. OWA mengasumsikan pengetahuan di dunia ini tidak terbatas, sehingga ketidakhadiran fakta di dalam graf lokal tidak secara otomatis membuktikan bahwa fakta tersebut salah.



2. Berapa baris hasil SELECT ?a ?b WHERE { ?a ex:mengajar ?mk . ?b ex:mengajar ?mk . }? Mengapa muncul baris dengan ?a sama dengan ?b?

**Jumlah baris hasil akhir  :** 5 baris

| ?a | ?b | ?mk |
| --- | --- | --- |
| ex:budi | ex:budi | ex:tif2305 |
| ex:sari | ex:sari | ex:tif2305 |
| ex:sari | ex:budi | ex:tif2305 |
| ex:budi | ex:sari | ex:tif2305 |
| ex:sari | ex:sari | ex:tif2410 |

**Penyebab munculnya baris ?a sama dengan ?b:**  
SPARQL mencocokkan pola (*pattern matching*) secara independen untuk tiap variabel tanpa asumsi implisit bahwa `?a` dan `?b` harus menunjuk pada entitas yang berbeda. Karena `ex:budi` mengajar `ex:tif2305`, maka triple tersebut cocok untuk `?a ex:mengajar ex:tif2305` sekaligus cocok untuk `?b ex:mengajar ex:tif2305` pada mata kuliah yang sama (`?mk` yang sama). Jika ingin memastikan `?a` dan `?b` tidak sama, harus ditambahkan filter eksplisit: `FILTER(?a != ?b)`.



3. Pola ?mk ex:nama "Web Semantik" menghasilkan nol baris pada graf yang menulis "Web Semantik"@id. Jelaskan penyebabnya.

**Penyebab utama    :**  
Pada SPARQL dan RDF, literal polos tanpa *language tag* (`"Web Semantik"`) dispesifikasikan sebagai node yang berbeda secara ketat dari literal yang diberi *language tag* (`"Web Semantik"@id`).

**Penjelasan detail :**  
Pencocokan string pada triple pattern SPARQL bersifat *exact matching* (mencakup karakter teks, tipe data, dan tag bahasa). Mesin SPARQL memperlakukan `datatype` atau `langTag` sebagai bagian integral dari nilai literal tersebut, sehingga `"Web Semantik"` != `"Web Semantik"@id`. Untuk mencocokkannya, query harus menambahkan tag bahasa secara eksplisit (`?mk ex:nama "Web Semantik"@id`) atau menggunakan pemroses fungsi string seperti `FILTER(STR(?nama) = "Web Semantik")`.

## Refleksi

**1. Di titik mana SPARQL berbeda dari SQL?**

SPARQL digunakan untuk mengambil informasi dari graf RDF berdasarkan hubungan antar data, sedangkan SQL digunakan untuk mengelola dan mengambil data dari tabel dalam database relasional. Perbedaannya terlihat dari cara pencarian datanya, SPARQL menggunakan pola triple untuk mencocokkan informasi, sementara SQL menggunakan tabel dan relasi antar tabel.

**2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?**

Graf lokal menggunakan rdflib ketika ingin mengelola, menambahkan, atau menguji data RDF milik sendiri. Sedangkan endpoint publik digunakan ketika ingin mencari informasi dari sumber data online seperti Wikidata tanpa harus menyimpan seluruh datanya secara lokal.

**3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.**

Hasil query yang cukup menarik adalah ketika satu dosen muncul lebih dari satu kali pada hasil SELECT. Hal ini terjadi karena dosen tersebut mengajar lebih dari satu mata kuliah. Jadi, satu dosen bisa memiliki beberapa hubungan dengan mata kuliah yang berbeda di dalam graf RDF.
