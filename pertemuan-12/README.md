# Pertemuan 12 - Inferensi dan Reasoning

## Langkah 4 - Wikidata
- ?n Q8 / Q9: 877 / 1343
- Penyebab selisih: Q8 hanya menghitung entitas yang statement `P31`-nya langsung menunjuk ke `Q3918` (universitas), sehingga hasilnya 877. Banyak universitas di Wikidata dicatat dengan kelas yang lebih spesifik, misalnya politeknik, universitas swasta, dan universitas negeri, yang baru terhubung ke `Q3918` lewat rantai `P279` (*subclass of*).
  Q9 memakai `P31/P279*`, sehingga ikut menghitung instance dari semua subkelas universitas dan hasilnya 1343, selisih 466. Hierarki kelas yang disimpan Wikidata sama untuk kedua query, tetapi hanya Q9 yang menelusurinya. Karena tanda `*` mencakup nol langkah, instance langsung tetap terhitung, sehingga Q9 >= Q8 (1343 >= 877).
- Satu subkelas yang menyumbang selisih: Politeknik (`wd:Q845392`) dengan 375 universitas Indonesia, disusul universitas swasta (`wd:Q902104`) dengan 320 dan universitas negeri (`wd:Q875538`) dengan 73.
  Total seluruh baris query bantu (801) lebih besar dari selisih 466 karena satu entitas bisa punya beberapa nilai `P31` dan sebagian juga sudah dicatat langsung sebagai `Q3918` sehingga terhitung di Q8.
  Q7 Pertemuan 11 hanya mendaftar subkelas universitas (`P279+ Q3918`) tanpa menghitung instance dan tanpa filter Indonesia, sedangkan query bantu menghitung universitas Indonesia per subkelas dan menghasilkan 14 kelas.
  Politeknik tidak tampil di hasil Q7 Pertemuan 11 karena Q7 memakai `LIMIT 30` sehingga daftarnya terpotong. Setelah `LIMIT` dihapus, politeknik muncul, jadi politeknik memang subkelas universitas yang terhubung ke `Q3918` lewat `P279+`.
- WDQS: materialisasi, saat query, atau tidak keduanya: **Tidak keduanya.**
  - Bukan materialisasi, karena triple turunan seperti `?univ wdt:P31 wd:Q3918` untuk instance subkelas tidak disimpan. Yang tersimpan hanya data asserted.
  - Bukan penalaran otomatis, karena tanpa `/wdt:P279*` Q8 tidak menalar sama sekali.
  - Yang terjadi adalah penelusuran jalur (*property path*) saat query dijalankan. Aturan `rdfs9` (instance dari subkelas juga instance dari superkelasnya) ditulis sendiri oleh penulis query dalam bentuk `P31/P279*`, lalu dievaluasi oleh mesin query.
  - Jadi yang menjalankan `rdfs9` di Q9 adalah saya lewat pola query, bukan sebuah reasoner.