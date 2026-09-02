## 2. Analisis Kesalahan XML

| No | Bagian yang Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | `<nama> Budi Santoso </Nama>` | XML bersifat case-sensitive, tag pembuka menggunakan huruf kecil `<nama>` sedangkan tag penutup menggunakan huruf besar `</Nama>` | Ubah tag penutup sehingga menjadi `<nama>Budi Santoso</nama>` |
| 2 | `<angkatan>2024` |  Elemen `<angkatan>` tidak memiliki tag penutup | Tambahkan tag menutup `</angkatan>` sehingga menjadi `<angkatan>2024</angkatan>` |
| 3 | `Saya suka AI & Web Semantik` | Simbol `&` tidak boleh ditulis langsung di XML karena termasuk karakter khusus. Jadi, tanda tersebut harus ditulis sebagai `&amp;` supaya XML bisa dibaca dengan benar.  | Ubah menjadi `Saya suka AI `&amp;` Web Semantik` |

## 3. Analisis XML Schema

1. Apa nama root element yang diizinkan?
jawaban:
Nama root yang diizinkan ialah buku, hal ini dibisa dilihat dari tingkat atas skema.

2. Apa tipe data elemen judul?
jawaban:
Tipe data judul : xs:string, yang mewakili data berupa teks atau sekumpulan karakter.

3. Apa tipe data elemen tahun?
jawaban:
Tipe data tahun : xs:gYear, yang mewakili format tahun kalender Gregorian empat digit (contoh: 2024).

4. Apa tipe data elemen harga?
jawaban:
Tipe data harga : xs:decimal, yang mewakili bilangan desimal untuk nilai numerik presisi.

5. Apakah atribut isbn boleh tidak dituliskan? Jelaskan.
jawaban: 
Atribut isbn tidak boleh dihilangkan. atribut ini bersifat wajib karena memiliki atribut use='required" pada XSD. 


## 4. Analisis Namespace

1. Mengapa kedua elemen title tersebut tidak dianggap sama?
jawaban: 
Kedua elemen tidak dianggap sama karena masing-masing terikat pada namespace unik yang berbeda, sehingga mewakili konteks data yang berbeda secara makna.

2. Apa fungsi prefix buku: dan web:?
jawaban:
Berfungsi sebagai penanda ringkas (alias) untuk membedakan elemen dengan nama sama yang berasal dari konteks/kosakata berbeda.

3. Apa fungsi atribut xmlns?
jawaban:
Xmlns berfungsi untuk mendeklarasikan namespace serta memetakan prefix ke suatu URI tertentu.

4. Apakah URI namespace harus dapat dibuka sebagai halaman web? Jelaskan.
jawaban:
Tidak harus. URI dalam namespace hanya berfungsi sebagai pengenal unik (unique identifier) berbasis teks untuk mencegah bentrokan nama, bukan sebagai lokasi link web fisik yang harus diakses.





## Pertanyaan Evaluasi

1. Apa perbedaan utama XML dan HTML?
XML digunakan untuk menyimpan dan mengatur data, sedangkan HTML digunakan untuk menampilkan data pada halaman web. XML juga memungkinkan kita membuat nama tag sendiri sesuai dengan data yang ingin disimpan.

2. Apa yang dimaksud dokumen XML yang well-formed?
XML well-formed adalah XML yang sudah mengikuti aturan dasar penulisan XML. Contohnya, setiap tag harus memiliki tag penutup, penulisan tag harus benar, dan dokumen hanya memiliki satu root element.

3. Jelaskan perbedaan well-formed dan valid.
Well-formed berarti struktur XML sudah benar sesuai aturan dasar XML. Sedangkan valid berarti XML tersebut tidak hanya memiliki struktur yang benar, tetapi juga mengikuti aturan atau struktur yang sudah ditentukan dalam DTD atau XSD.

4. Mengapa XSD lebih kuat dibandingkan DTD?
XSD lebih kuat karena dapat menentukan tipe data dengan lebih detail, seperti string, integer, date, dan lainnya. XSD juga menggunakan sintaks XML sehingga lebih mudah digunakan bersama teknologi XML lainnya.

5. Mengapa namespace penting ketika data XML berasal dari beberapa kosakata berbeda?
Namespace digunakan untuk membedakan elemen yang memiliki nama sama tetapi berasal dari kosakata yang berbeda. Dengan namespace, XML dapat mengetahui elemen tersebut berasal dari sumber atau kelompok data yang mana sehingga tidak terjadi konflik nama.

6. Apa kegunaan XPath dalam pengolahan dokumen XML?
XPath digunakan untuk mencari atau memilih bagian tertentu dari dokumen XML. Dengan XPath, kita dapat mengambil data tertentu berdasarkan nama elemen, atribut, atau posisi elemen dalam struktur XML.
