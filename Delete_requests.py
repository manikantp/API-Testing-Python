import requests
import jsonpath
import _json

#API_URL

url = "https://reqres.in/api/users/2"

response = requests.delete(url)

#Fetch Response code
print(response.status_code)

#assertion
assert response.status_code==204