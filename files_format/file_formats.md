# File formats

Saving information in computer science to different file formats means storing data in a way that can be read and processed by different programs or devices.
Different file formats have different advantages and disadvantages, such as size, compatibility, readability, and security. Some of the common file formats are:

- **TXT**: A plain text file that can store any text *without formatting* or special characters. It is widely compatible and easy to read, but it cannot store images, tables, or other complex data.

- **CSV**: A comma-separated values file that can store *tabular data* in a plain text format. Each row is a record and each column is a field separated by commas. It is often used for data analysis and exchange, but it cannot store formatting, formulas, or multiple sheets.

- **XML**: An extensible markup language file that can store *structured data* in a plain text format. It uses tags and attributes to define the data elements and their relationships. It is often used for data transfer and web development, but it can be *verbose and complex to parse.*

- **JSON**: A JavaScript object notation file that can store *structured data* in a plain text format. It uses key-value pairs and arrays to define the data elements and their relationships. It is often used for data interchange and web development.

- **YAML**: A *human-readable* data-serialization language that uses indentation and keywords to define the data structure. It is commonly used *for configuration files* and can store complex data types such as references and collections. However, it is *more verbose* and less compatible than JSON.

- **others**: There are many other file formats that can store different types of data, such as images, videos, audio, documents, archives, etc. Some examples are jpg, png, gif, mp4, mp3, wav, docx, pdf, zip, rar, etc. Each of these formats has its own specifications and features that make it suitable for certain purposes.

## Example of the same data stored in txt, csv, xml and json

Let’s say the data is about Bob and Carol, who have different names, ages, and hobbies. Here is how it could look like in each format:

- **txt**: A plain text file that could store the data as follows:

``` txt
Name: Bob
Age: 32
Hobbies: soccer, guitar, cooking

Name: Carol
Age: 28
Hobbies: painting, yoga, gardening
```

- **csv**: A comma-separated values file that could store the data as follows:

``` csv
Name,Age,Hobbies
Bob,32,"soccer,guitar,cooking"
Carol,28,"painting,yoga,gardening"
```

- **xml**: An extensible markup language file that could store the data as follows:

``` xml
<persons>
  <person>
    <name>Bob</name>
    <age>32</age>
    <hobbies>
      <hobby>soccer</hobby>
      <hobby>guitar</hobby>
      <hobby>cooking</hobby>
    </hobbies>
  </person>
  <person>
    <name>Carol</name>
    <age>28</age>
    <hobbies>
      <hobby>painting</hobby>
      <hobby>yoga</hobby>
      <hobby>gardening</hobby>
    </hobbies>
  </person>
</persons>
```

- **json**: A JavaScript object notation file that could store the data as follows:

``` json
[
  {
    "name": "Bob",
    "age": 32,
    "hobbies": ["soccer", "guitar", "cooking"]
  },
  {
    "name": "Carol",
    "age": 28,
    "hobbies": ["painting", "yoga", "gardening"]
  }
]
```
