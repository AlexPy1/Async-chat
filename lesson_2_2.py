import json

def write_order_to_json(item, quantity, price, buyer, date):
    data_dict = {'item': item, 'quantity': quantity,
                 'price': price, 'buyer': buyer, 'date':date}

    with open('result.json', 'w') as f:
        json.dump(data_dict, f,sort_keys= True, indent=4)

write_order_to_json('item',4, 1234, 'buyer', 'data')