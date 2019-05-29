import requests

def request(method, url, payload = {}):

	if method == "GET":
		response = requests.request(method, url)
	else:
		response = requests.request(method, url, data=payload)

	if method == "DELETE":
		return response
	else:
		return response.json()


print(request("GET", "https://reqres.in/api/users"))
print(request("POST", "https://reqres.in/api/users", {"name": "prueba", "job": "prueba"}))
print(request("PUT", "https://reqres.in/api/users/2", {"name": "prueba", "job": "prueba"}))
print(request("DELETE", "https://reqres.in/api/users/2", {}))
