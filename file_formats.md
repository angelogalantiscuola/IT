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

## File handling

### Parsing

> A file is a bunch of information that is stored on a computer or a phone or a tablet. Sometimes the information is words or numbers or pictures or sounds or anything else. But the computer or the phone or the tablet doesn’t know what the information means or how to use it. It needs to sort it out first before it can do anything with it. Sorting the information is like parsing a file.

To parse a file means to read in a data stream and **build a representation of the semantic content of that data**, in order to facilitate performing some kind of transformation on the data.

> For example, parsing a CSV file means extracting the values from each row and column and storing them in an array or an object.

Parsing a file usually involves following some rules or grammar that define the structure and meaning of the data. Different file formats have different rules or grammar, such as delimiters, quotes, tags, etc.

### Reading, parsing and writing json server-side in Node.js

``` js
// To write to a JSON file, you need to use the fs module in Node.js and the JSON.stringify() method to convert a JavaScript object into a JSON string. 
const fs = require("fs");
const data = require("./data.json");
console.log(data);
// { "name": "Alice", "age": 25, "hobbies": ["reading", "hiking", "chess"] }
data.age = 26;
data.hobbies.push("cooking");
const newData = JSON.stringify(data);
fs.writeFile("./data.json", newData, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log("Data updated successfully!");
  }
});
```

### Writing json client-side in the browser

It is difficult to write a JSON file from the browser because the browser has limited access to the local file system for **security reasons**.
The browser does not want to allow malicious web pages to read or write files without the user’s consent or knowledge.
Therefore, the browser usually provides some mechanisms to read or write files, such as the File API, the Blob API, or the File System Access API, but they have some restrictions.

#### Alternatives to writing files on the web client

Some alternatives to writing files on the web client are:

- Using **web storage APIs**, such as localStorage, sessionStorage, IndexedDB, or Cache API, to store data in the browser’s storage. These APIs allow you to store key-value pairs or structured data in different scopes and capacities. They are useful for storing temporary or persistent data that does not need to be shared with other devices or users. However, they have some limitations, such as browser compatibility, storage quota, security risks, and user control.

- Using **cookies** to store data in small text files that are sent to and from the server with each HTTP request. Cookies allow you to store simple data that can be used for session management, personalization, or tracking. However, they have some drawbacks, such as size limit, performance overhead, security issues, and user consent.

- Using cloud services or APIs to store data on a **remote server** or database. Cloud services or APIs allow you to store large amounts of data that can be accessed from anywhere and by anyone with the right credentials. They are useful for storing complex or sensitive data that needs to be synchronized or backed up. However, they require internet connection, authentication, and payment.

- Using **browser extensions** or plugins to access the local file system or other resources. Browser extensions or plugins allow you to extend the functionality of the browser and interact with native applications or devices. They are useful for accessing files or data that are not available through the web platform. However, they require installation, permission, and trust from the user.

### Request a json from the client to the server and parse it

``` js
// Replace URL with your JSON URL
const url = "https://example.com/data.json";
// Use fetch() to send a request and get a response
fetch(url)
  // Parse the response as JSON
  .then(res => res.json())
  // Use the parsed data
  .then(data => {
    // Display the data object
    // { "name": "Alice", "age": 25, "hobbies": ["reading", "hiking", "chess"] }
    document.getElementById("content").innerHTML = JSON.stringify(data);
    // Do something else with the data
    // For example, parse a property of the data object that is a JSON string
    var subData = JSON.parse(data.name);
    // Display the subData object
    document.getElementById("name").innerHTML = JSON.stringify(subData);
  })
  // Handle any errors
  .catch(error => {
    console.error(error);
  });
```

### Difference between JSON.parse() and JSON.stringify()?

JSON.parse() and JSON.stringify() are two methods that belong to the JSON object in JavaScript. They are used to convert between JSON strings and JavaScript objects.
The difference between them is:

- JSON.parse() takes a JSON string as an argument and returns a JavaScript object that corresponds to the JSON data. It is used to **parse JSON data that is received from a server or a file into a usable JavaScript object**. For example:

``` js
// A JSON string
var jsonString = '{"name":"Alice","age":25,"hobbies":["reading","hiking","chess"]}';

// Parse the JSON string into an object
var jsonObject = JSON.parse(jsonString);

// Access the object properties
console.log(jsonObject.name); // Alice
console.log(jsonObject.hobbies[1]); // hiking
```

- JSON.stringify() takes a JavaScript object as an argument and returns a JSON string that represents the object. It is used to **serialize a JavaScript object into a JSON format that can be sent to a server or a file**. For example:

``` js
// A JavaScript object
var jsonObject = {
  name: "Bob",
  age: 32,
  hobbies: ["soccer", "guitar", "cooking"]
};

// Stringify the object into a JSON string
var jsonString = JSON.stringify(jsonObject);

// Display the JSON string
console.log(jsonString); 
// {"name":"Bob","age":32,"hobbies":["soccer","guitar","cooking"]}
```
