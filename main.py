import yaml

data = {
    "num": [2, 1, -1]

}

with open("data.yaml", "w", encoding='utf-8') as f:
    yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)
