import  requests
import json
import jsonpath

#API_URL
url= "https://www.reqres.in/api/users"

#Read Input from Json file
file= open('E:\\API\\POSTRequest.json','r')
json_input = file.read()
# parse into json format
request_json = json.loads(json_input)

#print(request_json)   To check if we are reading the value from json file

#Make POST request with Json Input Body

response = requests.post(url,request_json)
# print(response.content)

#validating response code
assert response.status_code == 201

#Fetch Headers from response
print(response.headers.get('Content-Length'))

#Parse response to json format
response_json = json.loads(response.text)

# Pick id using Json Path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])