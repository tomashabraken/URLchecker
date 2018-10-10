import requests 

url = input("What url?").strip()

r = requests.get(url)

status = int(r.status_code)

#print(r.status_code)


if status != 200:
	print("Error server not found")
	exit()

else:
    print("Welcome to the server")

#print(r.headers)

header = r.headers

for key, value in header.items():
    print(key, value)
        