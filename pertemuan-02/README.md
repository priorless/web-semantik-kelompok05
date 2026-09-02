




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
Atribut isbn tidak boleh dihilangkan. atribut ini bersifat wajib karena memmiliki atribut use='required" pada XSD. 