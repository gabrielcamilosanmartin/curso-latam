import requests

def request(url, api_key):
	payload = {'api_key': api_key}
	response = requests.request('GET', url, params=payload)
	return response.json()


def build_web_page(fotos):
	response = """<html>
	<head>
	</head>
	<body>
		<ul>
"""
	for foto in fotos['photos']:
		response += "			<li><img src='" + foto['img_src'] + "'></li>\n"

	response += """		</ul>
	</body>
</html>"""
	with open("index.html", "w") as file:
		file.write(response)


def photos_count(fotos):
	respuesta = {}
	for foto in fotos['photos']:
		if not foto['camera']['name'] in respuesta:
			respuesta[foto['camera']['name']] = 1
		else:
			respuesta[foto['camera']['name']] += 1
	return respuesta

response = request('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?page=1&sol=1000','PM3LUgiiSqRvbQdibmvQIaaC1k2veOMdH6DqKuzZ')
build_web_page(response)
print(photos_count(response))
