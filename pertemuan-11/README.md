
## Langkah 2 - Tebak lalu cek

| Soal | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|---------|-------------|-------------------------|
| A | 3 baris | 3 baris | Hasil sesuai karena terdapat tiga kelas yang memiliki jalur menuju ex:Dosen, termasuk kelas Dosen itu sendiri. |
| B | 4 baris | 4 baris | Hasil sesuai karena Sari memiliki dua jalur menuju ex:Pegawai melalui DosenTetap dan DosenTamu. |
| C | 3 triple | 3 triple | Hasil sesuai karena Budi, Sari, dan Rudi menghasilkan tiga triple bertipe Pegawai. |
| D | 0 triple | 0 triple | Hasil sesuai karena variabel ?n tidak terikat. Rudi tidak memiliki properti ex:nama sehingga tidak ada triple yang dapat dicetak. |


## Refleksi

**1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?**

Karena hasil CONSTRUCT berbentuk graf RDF yang tidak menyimpan triple yang sama lebih dari satu kali. Jadi, meskipun ada beberapa baris SELECT yang menghasilkan triple identik, triple tersebut hanya dihitung satu kali. Selain itu, jika ada variabel yang tidak memiliki nilai, triple tersebut tidak akan ikut dihasilkan.

**2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?**

Triple turunan yang sudah ada di kampus_usu_v4.ttl tidak otomatis berubah mengikuti taksonomi yang baru. Jadi, kita perlu menjalankan kembali program materialisasi agar triple turunannya sesuai dengan perubahan hierarki kelas terbaru.

**3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?**

CSV digunakan ketika hasil query berbentuk data tabel yang berisi baris dan kolom, misalnya jumlah universitas berdasarkan kota. Sedangkan Turtle digunakan ketika ingin menyimpan data dalam bentuk graf RDF yang menunjukkan hubungan antara satu data dengan data lainnya.

