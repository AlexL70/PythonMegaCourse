import requests as req

URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg/220px-Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg"

response = req.get(URL)
if response.status_code == 200:
    with open("george_washington.jpg", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
