# Pertemuan 6 - RDF Dasar

## IRI dasar graf

Graf RDF menggunakan namespace berikut:

* `ex:` — `http://example.org/kampus/`
* `rdf:` — `http://www.w3.org/1999/02/22-rdf-syntax-ns#`

## Contoh triple

Berikut contoh pemodelan kalimat menjadi triple RDF.

| Kalimat                                       | Subject          | Predicate    | Object           |
| --------------------------------------------- | ---------------- | ------------ | ---------------- |
| Ida Adi adalah dosen.                         | `ex:ida`         | `rdf:type`   | `ex:Lecturer`    |
| Ida Adi mengajar Web Semantik.                | `ex:ida`         | `ex:teaches` | `ex:WebSemantik` |
| Mata kuliah itu memiliki nama "Web Semantik". | `ex:WebSemantik` | `ex:name`    | `"Web Semantik"` |

Subject merupakan entitas yang dibahas, predicate menunjukkan hubungan atau sifatnya, sedangkan object merupakan entitas lain atau nilai yang berkaitan dengan subject.

## IRI, Literal, Blank Node, dan Prefix

### 1. Identifikasi jenis node untuk ex:ida, "Ida Adi"@id, dan [ ex:kota "Medan" ]
- ex:ida → *IRI*, karena merupakan identitas atau resource yang dapat digunakan sebagai subject maupun object dalam RDF.
- "Ida Adi"@id → *Literal*, karena merupakan nilai berupa teks dengan language tag id.
- [ ex:kota "Medan" ] → *Blank Node*, karena merupakan node yang tidak memiliki nama atau IRI yang diberikan secara langsung.

### 2. Mengapa literal tidak boleh menjadi subject RDF?
Literal tidak boleh menjadi subject RDF karena literal digunakan sebagai nilai atau informasi akhir, seperti nama, tanggal, angka, atau teks. Subject harus berupa IRI atau blank node agar dapat menjadi identitas suatu resource dan memiliki hubungan dengan pernyataan RDF lainnya.

### 3. Buat IRI dasar untuk graf Anda dengan pola HTTP
IRI dasar yang digunakan adalah:
https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#


### 4. Tuliskan kepanjangan namespace rdf, rdfs, xsd, dan foaf
- *rdf* = Resource Description Framework
- *rdfs* = RDF Schema
- *xsd* = XML Schema Definition
- *foaf* = Friend of a Friend

## Ringkasan graf
- Jumlah triple: 32 triple
- Namespace yang digunakan: `ex`, `foaf`, `rdf`, `xsd`
- Entitas: 3 Dosen (Isa Dadi, Umayya, Opim Salim), 3 Mata Kuliah (Web Semantik, Basis Data, Dasar Pemrograman), 2 Mahasiswa (Indah, Keizya), dan 1 Universitas (USU).

## Contoh triple
1. ex:isa_dadi - rdf:type - ex:Lecturer
2. ex:keizya - ex:mengambil - ex:basis_data
3. ex:dasar_pemrograman - ex:jumlahKredit - "3"^^xsd:integer

## Perbandingan serialisasi
- Turtle: Formatnya lebih ringkas dan sangat mudah dibaca oleh manusia. Format ini memanfaatkan prefix (seperti `ex:` dan `foaf:`) sehingga penulisan IRI tidak perlu diulang-ulang secara penuh.
- JSON-LD: Formatnya berupa struktur data JSON (pasangan *key-value*). Bentuk ini sangat memudahkan mesin atau aplikasi web modern untuk memproses data graf, dengan menggunakan `@id` untuk merepresentasikan IRI.
- Pernyataan yang sama (contoh nama dosen):
  - **Turtle:** 
    `ex:umaya foaf:name "Umayya"@id .`
  - **JSON-LD:**
    ```json
    {
      "@id": "[https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#umaya](https://priorless.github.io/web-semantik-kelompok05/251402087/kampus#umaya)",
      "[http://xmlns.com/foaf/0.1/name](http://xmlns.com/foaf/0.1/name)": [
        {
          "@language": "id",
          "@value": "Umayya"
        }
      ]
    }
    ```

## Refleksi

**1. Kapan object harus berupa IRI dan kapan berupa literal?**

Object menggunakan IRI kalau merujuk pada entitas lain, misalnya mata kuliah Web Semantik. Kalau object berisi nilai seperti nama mata kuliah, maka digunakan literal, contohnya `"Web Semantik"`.

**2. Mengapa prefix membantu keterbacaan tanpa mengubah IRI?**

Prefix membuat penulisan IRI yang panjang menjadi lebih singkat dan mudah dibaca. Prefix hanya sebagai pengganti bagian awal IRI, jadi alamat IRI aslinya tetap sama.

**3. Sebutkan satu kesalahan pemodelan yang Anda hindari pada graf ini.**

Kesalahan yang saya hindari adalah menggunakan literal sebagai subject. Contohnya, `"Web Semantik"` digunakan sebagai nilai nama mata kuliah, bukan sebagai subject. Subject harus berupa IRI atau blank node.
