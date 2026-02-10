def famous_births(scientists_data):

    sorted_scientists = sorted(scientists_data.values(), key=lambda x: x["date_of_birth"])
    export_data = [f"{scientist['name']} is a great scientist born in {scientist['date_of_birth']}"
        for scientist in sorted_scientists
    ]
    for line in export_data:
        print(line)

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}

famous_births(women_scientists)