import requests
import pprint

url = "https://backend.akumotechnology.com/api/students/me/certificates"
cookie = {"access_token_cookie": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb25hdGhhbnJhdGhqZW5AeWFob28uY29tIiwiZXhwIjoxNzUwMTI3MjE1fQ.DN_uyjvmoDBTOaQ1mcqovSan4tWABXr4wQu4L8IXuoU"}

response = requests.get(url,cookies = cookie)
pprint.pprint(response.json())

