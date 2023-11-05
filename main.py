dict = {"number":{"name":"ivo", "age": 15}}
for k, v in dict.items():
    for inner_v in v.values():
        print(inner_v)
