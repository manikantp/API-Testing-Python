import requests
import json
import jsonpath

url =  "https://www.reqres.in/api/users"

#Read Input from Json file
file= open('E:\\API\\POSTRequest.json','r')
json_input = file.read()

request_json = json.loads(json_input)

#Make PUT request with Json Input Body

response = requests.put(url,request_json )
# print(response.content)

assert response.status_code == 200

#Parse response to json format
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])