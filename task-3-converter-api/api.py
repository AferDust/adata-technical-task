from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
import json
import dicttoxml
from starlette import status


app = FastAPI(
    title="JSON to XML Converter API",
    description="This API provides two endpoints: one for converting JSON from a request body to XML, and another for "
    "converting an uploaded JSON file to XML.",
    version="1.0.0",
)


@app.post(
    "/convert-json-request-body-to-xml",
    status_code=status.HTTP_200_OK,
    summary="Convert JSON from Request Body to XML",
    description="""
              This endpoint accepts a JSON object in the request body and converts it to an XML format. 
              It returns the XML as a response with `application/xml` content-type.
    """,
    response_description="XML data generated from the input JSON.",
)
async def convert_json_request_body_to_xml(body: dict):
    try:
        xml_data = dicttoxml.dicttoxml(body, custom_root="root", attr_type=False)

        return Response(content=xml_data, media_type="application/xml")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post(
    "/convert-json-file-to-xml",
    status_code=status.HTTP_200_OK,
    summary="Convert Uploaded JSON File to XML",
    description="""
                This endpoint accepts a JSON file uploaded by the client and converts it to XML format. 
                The response is returned in `application/xml` format.
    """,
    response_description="XML data generated from the uploaded JSON file.",
)
async def convert_json_file_to_xml(file: UploadFile = File(...)):
    if file.content_type != "application/json":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only JSON files are " "allowed.",
        )

    try:
        contents = await file.read()
        json_data = json.loads(contents)

        xml_data = dicttoxml.dicttoxml(json_data, custom_root="root", attr_type=False)

        return Response(content=xml_data, media_type="application/xml")
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid JSON format."
        )
