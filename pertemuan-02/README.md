




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

2.Apa fungsi prefix buku: dan web:?
jawaban:
Berfungsi sebagai penanda ringkas (alias) untuk membedakan elemen dengan nama sama yang berasal dari konteks/kosakata berbeda.

3. Apa fungsi atribut xmlns?
jawaban:
Xmlns berfungsi untuk mendeklarasikan namespace serta memetakan prefix ke suatu URI tertentu.

4. Apakah URI namespace harus dapat dibuka sebagai halaman web? Jelaskan.
jawaban:
Tidak harus. URI dalam namespace hanya berfungsi sebagai pengenal unik (unique identifier) berbasis teks untuk mencegah bentrokan nama, bukan sebagai lokasi link web fisik yang harus diakses.


