import json

with open('./data/tags.json', 'r') as tags_file:
    tags = json.load(tags_file)
o = open("new_opc_tags.csv", "w")
o.write("tag,inital\n")
for i in tags:
    print(i)
    if i.get("derived"):
        continue
    try:
        value = i["value"]
    except:
        value = i["initial"]
    o.write(f"{i['name']},{value}\n")
o.close()
