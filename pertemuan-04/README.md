# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber

Sumber belajar yang digunakan adalah video pembelajaran dari YouTube dengan informasi sebagai berikut.

| Elemen        | Nilai                                                                                                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Judul**     | *Introduction: The Semantic Web Foundation: RDF, URIs, and Ontologies Explained*                                                                                                         |
| **Pembuat**   | Mohamed Yoosuf Aathil                                                                                                                                                                    |
| **Deskripsi** | Video pengantar tentang dasar-dasar Web Semantik yang membahas RDF, URI, RDFS, dan OWL serta perannya dalam membantu aplikasi bertukar data dengan tetap mempertahankan makna informasi. |
| **Tanggal**   | 2025-10-23                                                                                                                                                                               |
| **Jenis**     | Video pembelajaran                                                                                                                                                                       |
| **Bahasa**    | en                                                                                                                                                                                       |
| **Hak**       | Hak cipta oleh pembuat video                                                                                                                                                             |

## Pemetaan Dublin Core Terms

Prefix yang digunakan:

`dcterms: http://purl.org/dc/terms/`

| Properti Dublin Core Terms | Fungsi                                              | Nilai                                                                                                                                                                                    |
| -------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`dcterms:title`**        | Menyatakan judul sumber belajar                     | *Introduction: The Semantic Web Foundation: RDF, URIs, and Ontologies Explained*                                                                                                         |
| **`dcterms:creator`**      | Menyatakan pihak yang membuat sumber                | Mohamed Yoosuf Aathil                                                                                                                                                                    |
| **`dcterms:description`**  | Menjelaskan isi atau ringkasan sumber               | Video pengantar tentang dasar-dasar Web Semantik yang membahas RDF, URI, RDFS, dan OWL serta perannya dalam membantu aplikasi bertukar data dengan tetap mempertahankan makna informasi. |
| **`dcterms:created`**      | Menyatakan tanggal pembuatan atau penerbitan sumber | 2025-10-23                                                                                                                                                                               |
| **`dcterms:type`**         | Menyatakan jenis sumber                             | Video pembelajaran                                                                                                                                                                       |
| **`dcterms:language`**     | Menyatakan bahasa yang digunakan dalam sumber       | en                                                                                                                                                                                       |
| **`dcterms:rights`**       | Menyatakan informasi mengenai hak atas sumber       | Hak cipta oleh pembuat video                                                                                                                                                             |

### Alasan Pemilihan Properti

Ketujuh properti tersebut dipilih karena dapat menggambarkan informasi utama dari sumber belajar secara jelas. `dcterms:title` digunakan untuk mengidentifikasi judul video, sedangkan `dcterms:creator` menunjukkan pihak yang membuat sumber tersebut. `dcterms:description` digunakan untuk memberikan gambaran mengenai isi video.

`dcterms:created` digunakan untuk mencatat tanggal sumber, yaitu 23 Oktober 2025 dalam format ISO 8601. `dcterms:type` menunjukkan bahwa sumber yang digunakan berupa video pembelajaran. `dcterms:language` menunjukkan bahwa bahasa sumber adalah bahasa Inggris dengan kode `en`. Sementara itu, `dcterms:rights` digunakan untuk memberikan informasi mengenai hak atas sumber.

Dalam sumber ini, `dcterms:creator` digunakan untuk menyatakan **Mohamed Yoosuf Aathil sebagai pembuat video**. Properti `dcterms:publisher` tidak digunakan karena informasi yang tersedia tidak menunjukkan adanya pihak penerbit atau penyedia yang berbeda dari pembuat sumber.

## Hasil validasi
- JSON-LD Playground: Berhasil diproses tanpa galat sintaksis (0 error). Pemrosesan ke format N-Quads/RDF Triples berhasil mengekstrak seluruh properti dcterms (title, creator, description, created, type, language, rights) secara tepat sesuai dengan URI subjek yang ditentukan.
- Schema Markup Validator: Berhasil terdeteksi sebagai tipe LearningResource dengan status 0 ERRORS dan 0 WARNINGS. Seluruh properti schema.org (name, description, inLanguage, dateCreated, license) terpisah dan terstruktur dengan benar.

## Refleksi
1. Mengapa URI yang sama penting untuk Turtle dan JSON-LD?
Jawaban: Agar sistem Semantic Web mengenali bahwa berkas Turtle dan JSON-LD tersebut merujuk pada entitas/sumber data yang sama persis (Resource Identification), sesuai prinsip Linked Data.
2. Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?
Jawaban: DC Terms (Dublin Core) berfokus pada standar kearsipan/katalogisasi metadata umum (seperti pencipta, judul, dan hak cipta), sedangkan schema.org berfokus pada pemahaman struktur data oleh mesin pencari (Search Engine Optimization / SEO Google).
3. Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.
Jawaban: Terjadi ketidakcocokan data (data ambiguity/mismatch), sehingga mesin atau sistem agregator Semantic Web bisa salah menafsirkan informasi atau gagal menggabungkan data (interoperability fail).

## Catatan akhir
