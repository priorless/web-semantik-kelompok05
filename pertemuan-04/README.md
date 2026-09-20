# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber

Sumber belajar yang digunakan adalah video pembelajaran dari YouTube dengan informasi sebagai berikut.

- Judul: Introduction: The Semantic Web Foundation: RDF, URIs, and Ontologies Explained
- Pembuat: Mohamed Yoosuf Aathil
- URI sumber: https://priorless.github.io/web-semantik-kelompok05/251402087/sumber-belajar
- Jenis sumber: MovingImage

| Elemen        | Nilai                                                                                                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Judul**     | *Introduction: The Semantic Web Foundation: RDF, URIs, and Ontologies Explained*                                                                                                         |
| **Pembuat**   | Mohamed Yoosuf Aathil                                                                                                                                                                    |
| **Deskripsi** | "Video pembelajaran mengenai fondasi Semantic Web, Resource Description Framework (RDF), URIs, dan Ontologies." |
| **Tanggal**   | 2025-10-23                                                                                                                                                                               |
| **Jenis**     | MovingImage                                                                                                                                                                       |
| **Bahasa**    | en                                                                                                                                                                                       |
| **Hak**       | Creative Commons Attribution 4.0 International.                                                                                                                                                             |

## Pemetaan Dublin Core Terms

Prefix yang digunakan:

`dcterms: http://purl.org/dc/terms/`

| Properti Dublin Core Terms | Fungsi                                              | Nilai                                                                                                                                                                                    |
| -------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`dcterms:title`**        | Menyatakan judul sumber belajar                     | *Introduction: The Semantic Web Foundation: RDF, URIs, and Ontologies Explained*                                                                                                         |
| **`dcterms:creator`**      | Menyatakan pihak yang membuat sumber                | Mohamed Yoosuf Aathil                                                                                                                                                                    |
| **`dcterms:description`**  | Menjelaskan isi atau ringkasan sumber               | Video pembelajaran mengenai fondasi Semantic Web, Resource Description Framework (RDF), URIs, dan Ontologies. |
| **`dcterms:created`**      | Menyatakan tanggal pembuatan atau penerbitan sumber | 2025-10-23                                                                                                                                                                               |
| **`dcterms:type`**         | Menyatakan jenis sumber                             | MovingImage                                                                                                                                                                      |
| **`dcterms:language`**     | Menyatakan bahasa yang digunakan dalam sumber       | en                                                                                                                                                                                       |
| **`dcterms:rights`**       | Menyatakan informasi mengenai hak atas sumber       | Creative Commons Attribution 4.0 International                                                                                                                                                             |

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
Seluruh metadata pada berkas HTML (`sumber-belajar.html`), Turtle (`metadata-sumber.ttl`), JSON-LD DC Terms (`metadata-sumber.jsonld`), dan JSON-LD Schema.org (`metadata-schema.jsonld`) telah diselaraskan secara penuh. Setiap berkas menggunakan URI subjek yang identik (`https://priorless.github.io/web-semantik-kelompok05/251402087/sumber-belajar`), nilai atribut dasar yang konsisten (judul, pembuat, deskripsi, tanggal buat, bahasa, serta lisensi CC BY 4.0), dan sintaksis yang valid sesuai spesifikasi format masing-masing.