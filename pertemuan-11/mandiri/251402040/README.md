# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: [30]
- Triple dengan LIMIT 30: [90]
- Baris SELECT LIMIT 10 / kota berbeda: [10] / [10]
- Mengapa tidak (atau mengapa tepat) 30 triple: [Hasil CONSTRUCT LIMIT 10 tepat menghasilkan 30 triple karena terdapat 10 kota berbeda dan setiap kota menghasilkan 3 triple sesuai pola pada template, yaitu tipe kota, nama kota, dan populasi. Tidak terdapat triple kembar yang mengurangi jumlah hasil.]

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: [48] triple, film tanpa tanggal: [16]
- Sumber data: DBpedia 
- Triple yang tetap tercetak untuk film tanpa tanggal: [df:type schema:Movie, schema:name, dan schema:director. Triple schema:datePublished tidak tercetak untuk film tersebut karena variabel ?rilis tidak memiliki nilai. Tidak ada error karena menggunakan OPTIONAL.]
- Query lokal tanpa internet: [Query lokal tetap bisa dijalankan tanpa internet karena data sudah disimpan di film_nolan.ttl. Tetapi, jika seluruh demo_c.py dijalankan ulang tanpa internet, pengambilan data dari DBpedia akan gagal.]
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: [Query kedua menggunakan schema:Movie, karena itulah tipe yang dicetak oleh template CONSTRUCT. Tipe dbo:Film tidak ikut disimpan sehingga pencarian dengan tipe tersebut menghasilkan 0.]

## Bagian C - Materialisasi
- Output demo_d.py: [Sebelum: 0 Sesudah: 3 Ada Rina: 3]
- Mengapa Ada Rina bernilai 3: [Ada Rina tetap bernilai 3 karena materialisasi hanya dilakukan sebelum Rina ditambahkan. Ketika Rina masuk, aturan untuk menghasilkan hubungan kelas belum dijalankan kembali. Jadi, Rina belum mendapatkan triple turunan foaf:Person.]
- Output materialisasi_ulang.py: [Putaran 1: 4 triple baru | Person: 3
Rina masuk | Person: 3
Putaran 2 | Person: 4
Triple turunan disimpan terpisah: 6]
- Tiga triple yang bukan baru: [Tiga triple lama itu tercetak akibat sifat zero-length path (simbol *) pada a/rdfs:subClassOf*, yang mencetak ulang deklarasi tipe langsung (indeks 0) dari entitas tersebut.]
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: [kampus_turunan.ttl berguna untuk memisahkan hasil inferensi dari data asli. Jika aturan kelas berubah, hasil inferensi lama perlu diperiksa dan dihitung ulang secara manual agar tidak menyimpan kesimpulan yang sudah tidak berlaku.]

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | [ketidaksesuaian nama variabel.] | ?f dbo:director dbr:Christopher_Nolan ; rdfs:label ?j . | 3 triple |
| rusak_b | 4 triple | Dua nilai yang tampak sama | ?o foaf:name rdfs:label schema:name ?n . | 3 triple |
| rusak_c | 0 triple | Superkelas tidak ditemukan. |3 triple |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | [Tidak ada] | [Ada pada baris UA] |
| 2 LIMIT | [Ada LIMIT 10] | [Tidak ada] |
| 3 Simpan, jangan ulangi | [Tidak menyimpan graf] | [Menyimpan ke film_nolan.ttl] |
| 4 Jangkar jalur | [Ada wd:Q515 dan wd:Q252] | [Tidak menggunakan property path] |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: CONSTRUCT {
  ?x a ex:Kota .
}
WHERE {
  ?x a/rdfs:subClassOf* ?y .
}

query tanpa jangkar akan memaksa endpoint menelusuri seluruh kemungkinan hierarki subkelas di seluruh database yang sangat membebani server.

### Diskusi 1 - Taksonomi berubah
Ketika tim menyimpan hasil materialisasi langsung ke dalam graf produksi secara permanen seperti pada Demo D (yang menghasilkan kampus_v4.ttl), kita secara otomatis mencampuradukkan data asli (fakta dasar) dengan data hasil inferensi (kesimpulan turunan). Jika setahun kemudian taksonomi berubah—misalnya, entitas ex:Dosen tidak lagi didefinisikan sebagai subkelas dari foaf:Person—maka triple turunan seperti [http://contoh.id/kampus/rina](http://contoh.id/kampus/rina) a foaf:Person akan menjadi salah dan tidak valid lagi di dalam sistem.

Menemukan dan membersihkan triple yang salah ini di dalam kampus_v4.ttl sangatlah sulit. Kita tidak bisa dengan mudah membedakan mana triple a foaf:Person yang memang dideklarasikan secara eksplisit sejak awal dan mana yang murni merupakan hasil bentukan aturan taksonomi yang lama. Kita harus melacaknya satu per satu secara manual.

Sebaliknya, pendekatan pada Bagian C2 yang memisahkan hasil materialisasi ke dalam berkas kampus_turunan.ttl menawarkan arsitektur data yang jauh lebih tangguh dan terkelola. Jika aturan taksonomi di masa depan berubah, kita tidak perlu membongkar graf utama. Kita cukup mengosongkan atau menghapus berkas kampus_turunan.ttl yang lama, memperbarui aturan hierarki kelasnya, lalu menjalankan ulang fungsi materialisasi (materialisasi_ulang.py) pada graf dasar. Sistem akan membangun ulang kesimpulan baru yang 100% selaras dengan taksonomi mutakhir tanpa merisikokan integritas data asli.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk kebutuhan back-end sebuah dashboard populasi kota, penggunaan query SELECT adalah pendekatan yang jauh lebih tepat. Dashboard analitik, tabel, dan diagram umumnya mengonsumsi data secara langsung dalam bentuk tabular baris demi baris (seperti JSON atau CSV). SELECT memberikan hasil berupa tabel variabel (bindings) yang terikat kuat secara komputasi. Selain itu, temuan pada Bagian A membuktikan bahwa CONSTRUCT memproses solution menjadi graf (himpunan/set) yang secara matematis meleburkan atau menggabungkan triple kembar menjadi satu. Dalam skenario data mentah dashboard, jika skema tidak unik, peleburan otomatis dari CONSTRUCT berisiko menyembunyikan atau menghilangkan baris data ganda yang sebenarnya valid.

Sebaliknya, untuk skenario menggabungkan data kota dari tiga sumber (endpoint) yang berbeda, CONSTRUCT adalah pilihan mutlak. Sumber yang berbeda hampir pasti menggunakan kosakata (vocabulary) yang berbeda pula. Kasus diagnosis pada rusak_b.rq mendemonstrasikan masalah ini dengan sangat jelas: satu nama bisa dipanggil dengan foaf:name, rdfs:label, atau schema:name yang bervariasi dengan berbagai tag bahasa. Melalui query CONSTRUCT, kita bisa mendesain satu template penyelarasan yang memaksa keragaman sumber tersebut masuk ke dalam satu predikat standar lokal (misalnya ex:nama). Hasil keluaran CONSTRUCT berupa RDF/Turtle murni yang bisa di-merge atau digabungkan ke triplestore lokal kita secara mulus, mengeliminasi konflik skema dari sumber-sumber yang heterogen tersebut.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1. CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar | [Bagian A] |
| 2. Variabel tak terikat tidak dicetak tanpa error | [Bagian D, rusak_a] |
| 3. UNION, jalur, dan VALUES menyatukan predikat berbeda | [Bagian D, rusak_b] |
| 4. Jalur + dan * menelusuri hierarki | [Bagian C dan D] |
| 5. Materialisasi menyimpan kesimpulan tetapi harus dihitung ulang | [Bagian C] |