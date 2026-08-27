# Web-Semantik-Kelompok05


# [Pertemuan 1] - Pengenalan Web Semantik
 
 ## 1. Eksplorasi Wikidata

Pada langkah ini, kami melakukan pencarian entitas **Universitas Sumatera Utara** melalui Wikidata. Berdasarkan informasi yang ditemukan, entitas tersebut memiliki identifier unik Q4200341. Identifier ini digunakan untuk membedakan Universitas Sumatera Utara dari entitas lain yang mungkin memiliki nama yang sama atau berbeda.

Informasi yang diperoleh adalah sebagai berikut:

- **Nama entitas:** Universitas Sumatera Utara
- **Identifier Wikidata:** Q4200341
- **Deskripsi:** Universitas negeri di Sumatera Utara, Indonesia.
- **Negara:** Indonesia
- **Lokasi:** Medan, Sumatera Utara
- **Tahun berdiri:** 20 November 1957
- **Website:** https://www.usu.ac.id/
  
Informasi lain yang menarik adalah bahwa Universitas Sumatera Utara juga dikenal dengan singkatan (USU), memiliki nama dalam bahasa Inggris University of North Sumatra, dan termasuk dalam kategori universitas.

## 2. Entitas, Atribut, dan Relasi

Berdasarkan informasi yang diperoleh dari Wikidata, informasi mengenai Universitas Sumatera Utara dapat dikelompokkan menjadi entitas, atribut, dan relasi sebagai berikut.

| Informasi | Kategori | Alasan |
|---|---|---|
| Universitas Sumatera Utara | Entitas | Objek utama yang memiliki identitas unik di Wikidata, yaitu Q4200341 |
| Indonesia | Entitas | Negara yang memiliki identitas dan dapat dibedakan dari negara lain |
| Medan | Entitas | Wilayah atau lokasi yang memiliki identitas tersendiri |
| Tahun berdiri | Atribut | Informasi yang menjelaskan kapan Universitas Sumatera Utara didirikan |
| Website resmi | Atribut | Informasi yang menunjukkan alamat situs resmi Universitas Sumatera Utara |
| Deskripsi universitas | Atribut | Informasi yang menjelaskan Universitas Sumatera Utara sebagai universitas negeri di Sumatera Utara, Indonesia |
| Singkatan USU | Atribut | Informasi yang menjelaskan bentuk singkat dari Universitas Sumatera Utara | |
| Universitas Sumatera Utara → located in → Medan | Relasi | Menunjukkan hubungan antara Universitas Sumatera Utara dengan Medan sebagai lokasi universitas |
| Universitas Sumatera Utara → country → Indonesia | Relasi | Menunjukkan hubungan antara Universitas Sumatera Utara dengan Indonesia sebagai negara tempat universitas berada |


## 3. Eksplorasi Scema.org

 Dalam langkah mengidentifikasi properti yang sesuai, kami melakukan eksplorasi standar Schema.org untuk mendeskripsikan entitas perguruan tinggi. Berdasarkan eksplorasi tersebut, berikut 5 properti yang dipilih beserta fungsi dan contoh nilainya.

| Property | Fungsi | Contoh Nilai |
| -------- | ------ | ------------ |
| legalName | Nama resmi universitas yang terdaftar. | Universitas Sumatera Utara |
| slogan | Slogan atau motto yang terkait dengan universitas tersebut. | The Era of Ultimate Excellence |
| address | Alamat dimana suatu universitas terkait berada. | Jl. Dr. T. Mansur No. 9, Kampus Padang Bulan, Medan, 20155, Sumatera Utara |
| hasCredential | Kredensial atau akreditasi yang diberikan kepada universitas. | Akreditasi Unggul (BAN-PT) |
| foundingDate | Tanggal berdirinya universitas. | 4 Juni 1952 |
| alumni | Alumni suatu universitas. | Tengku Erry Nuradi |

## 4. Pertanyaan Evaluasi

1. Apa perbedaan web tradisional dan Web Semantik?
Jawaban:
Menurut kami, web tradisional itu lebih banyak berisi halaman atau dokumen yang dibuat untuk dibaca oleh manusia. Sedangkan Web Semantik membuat informasi menjadi lebih jelas dengan memberikan makna dan hubungan antar data, sehingga komputer juga bisa memproses dan memahaminya.

2. Mengapa entitas membutuhkan identifier unik?
Jawaban:
Identifier unik dibutuhkan agar suatu entitas tidak tertukar dengan entitas lain. Soalnya, satu nama bisa saja memiliki arti yang berbeda. Dengan adanya identifier, komputer bisa mengetahui dengan jelas entitas mana yang sebenarnya sedang dibahas.

3. Jelaskan subject, predicate, dan object.
Jawaban:
Subject adalah sesuatu yang sedang dibicarakan. Predicate adalah hubungan atau keterangan dari subject, sedangkan object adalah sesuatu yang berhubungan dengan subject tersebut.

Contohnya:
Medan → terletakDi → Sumatera Utara
Pada contoh tersebut, Medan adalah subject, terletakDi adalah predicate, dan Sumatera Utara adalah object.

4. Apa keuntungan hubungan antarentitas?
Jawaban:
Keuntungannya ialah dengan adanya hubungan antarentitas, informasi jadi lebih mudah dipahami dan tidak berdiri sendiri. Hubungan tersebut juga bisa membantu komputer menemukan atau menyimpulkan informasi lain. Misalnya, jika Medan berada di Sumatera Utara dan Sumatera Utara berada di Indonesia, maka dapat diketahui bahwa Medan juga berada di Indonesia.

5. Bagaimana Knowledge Graph membantu AI?
Jawaban:
Menurut kami, Knowledge Graph membantu AI karena informasi di dalamnya sudah disusun sebagai fakta-fakta yang saling berhubungan. Jadi, AI bisa lebih mudah memahami hubungan antar informasi dan menggunakan fakta tersebut untuk memberikan jawaban yang lebih tepat.
