# Task 3 JSON to XML Converter API

This project provides a simple API to convert JSON data into XML format using the **FastAPI** framework. It exposes two endpoints: one for converting JSON from a request body to XML, and another for converting an uploaded JSON file to XML.

---

## 🚀 Quickstart With Docker
 ***Running the application in a Docker container, follow these steps:***
 
### 1. Build the Docker image:
```bash
  docker build -t json-to-xml-converter .
```

### 2. Run the Docker container:
```bash
  docker run -d -p 8000:8000 json-to-xml-converter
```

***The API will now be accessible at ``http://localhost:8000``.***

***To view swagger open ``http://localhost:8000/docs``.***

---

## 📌 API Endpoints
### 1. Convert JSON from Request Body to XML
* URL: ``/convert-json-request-body-to-xml``
* Method: ``POST``
* Description: ``Converts a JSON object sent in the request body to XML.``
* Response: ``The response will be the converted XML data.``

#### Example Request:
```bash
  POST /convert-json-request-body-to-xml
  Content-Type: application/json

  {
      "name": "John",
      "age": 30,
      "city": "New York"
  }
```
#### Example Response:
```bash
  <root>
    <name>John</name>
    <age>30</age>
    <city>New York</city>
  </root>
```

### 2. Convert Uploaded JSON File to XML
* URL: ``/convert-json-file-to-xml``
* Method: ``POST``
* Description: ``Converts a JSON file uploaded by the user to XML``.
* Response: ``The response will be the converted XML data``.

#### Example Request:
Upload a file named ``data.json`` with the following conten
```bash
  {
    "name": "Alice",
    "job": "Engineer"
  } 
```
#### Example Response:
```bash
  <root>
    <name>Alice</name>
    <job>Engineer</job>
  </root>
```

