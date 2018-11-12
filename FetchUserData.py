import requests
import json
import jsonpath


# API URL
url = "https://reqres.in/api/users?page=2"

# Send GET Requests

response= requests.get(url)
#printing the response
print(response)

#Displaying Response
#print(response.content)

#Displaying Requests
# print(response.headers)
#
# #Validating status code
# print(response.status_code)
#
# #asserting status code
# assert response.status_code == 200
#
# #Fetching specific data in the header
# print(response.headers.get('Server'))
#
# #Fetching cookies
# print(response.cookies)
#
# #Fetching encoding
# print(response.encoding)
#
# #Fetching elapsed time
# print(response.elapsed)

#parse response into json format
#json_response= json.loads(response.text)
# print(json_response)

#Fetch values using JsonPath
# pages = jsonpath.jsonpath(json_response,'total_pages')
# assert pages[0] == 4

# Fetch values using Advanced JsonPath
# for i in range(0,3):
#
#     first_name=jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
# print((first_name[0]))