def dictionary(lenght):
    result_dict = {}

    for _ in range(lenght):
        text = input().split()
        country = text[0]
        cities = text[1:]
        temp_dict = dict.fromkeys(cities, country)
        result_dict.update(temp_dict)

    return result_dict

