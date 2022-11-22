# Team Terrifying Yuppies
## Yusha Aziz & Talia Hsia

### DISCOS
- You can use `requests.get(*api link*)` to retrieve data from the api
- You can also convert the data you got from above to .text by storying the above code in a varaible, for example response_API, and doing `reponse_API.text`. It is advised that you store this also into a variable, such as `info`.
- You can convert `info` into a json file, using `json.loads(info)`, and store it in a variable such as `parse_json`.
- The json file is sort of like a dictionary with keys, so for this assignment we want the picture url so you can retrieve it via `parse_json['url']`

### QCC
- What type of data is json.loads actually, it seems like a dictionary, but could it be something else? 