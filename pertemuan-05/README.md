# Ontology dan Arsitektur Web Semantik

## Mengenali Anatomi Ontology

Domain yang digunakan dalam latihan ini adalah **kampus Universitas Sumatera Utara (USU)**. Ontology dibuat untuk menggambarkan beberapa konsep dan hubungan sederhana yang terdapat dalam lingkungan kampus.

| Komponen | Makna | Contoh Domain USU |
|---|---|---|
| **Class** | Konsep atau kelompok abstrak | `Mahasiswa`, `Dosen`, `MataKuliah` |
| **Subclass** | Class yang lebih khusus dari class lain | `MahasiswaTI` subclassOf `Mahasiswa`, `DosenTI` subclassOf `Dosen` |
| **Individual** | Instance konkret dari suatu class | `Quinsha` bertipe `MahasiswaTI`, `BasisData` bertipe `MataKuliah` |
| **Property** | Hubungan atau nilai suatu entitas | `mengambilMataKuliah`, `mengajarMataKuliah` |
| **Axiom** | Pernyataan yang memberikan makna atau aturan pada ontology | `Mahasiswa disjointWith Dosen` |

### Rancangan Ontology

**Class:**
- `Mahasiswa`
- `Dosen`
- `MataKuliah`

**Subclass:**
- `MahasiswaTI` subclassOf `Mahasiswa`
- `DosenTI` subclassOf `Dosen`

**Individual:**
- `Quinsha` bertipe `MahasiswaTI`
- `BasisData` bertipe `MataKuliah`

**Property:**
- `mengambilMataKuliah`: menghubungkan `Mahasiswa` dengan `MataKuliah`
- `mengajarMataKuliah`: menghubungkan `Dosen` dengan `MataKuliah`

**Axiom:**
- `Mahasiswa disjointWith Dosen`, yang berarti seorang individu tidak dapat menjadi `Mahasiswa` dan `Dosen` secara bersamaan dalam model ontology ini.

## Refleksi

1. **Apa perbedaan ontology dan taksonomi?**
   Taksonomi lebih fokus pada pengelompokan konsep berdasarkan tingkatan, sedangkan ontology juga menjelaskan hubungan dan aturan antar konsep dalam suatu domain.

2. **Mengapa domain pada OWL bukan constraint database?**
   Karena domain pada OWL digunakan untuk menunjukkan class yang berkaitan dengan suatu property. Domain tidak membatasi data seperti constraint pada database, tetapi dapat membantu reasoner menarik kesimpulan.

3. **Mengapa kosakata yang sudah ada sebaiknya dipakai kembali sebelum membuat yang baru?**
   Agar tidak membuat istilah yang sebenarnya sudah tersedia dan supaya ontology lebih mudah dipahami serta dapat digunakan bersama dengan ontology atau sistem lain.
