data = [
    ["David Smith", "Auroville", 1, "Screen Protector", 17, "Cash"],
    ["Bob Johnson", "Capitol Hill", 1, "Powerbank Black", 90, "Credit Card"],
    ["David Smith", "Auroville", 3, "Powerbank Black", 100, "Cash"],
    ["Alice Lee", "Capitol Hill", 4, "Splitter", 50, "Credit Card"],
    ["Claire R", "The Heights", 5, "Splitter", 55, "Credit Card"],
    ["David Chen", "Auroville", 10, "Powerbank Pink", 100, "Credit Card"],
    ["David Smith", "The Heights", 21, "Splitter", 55, "Credit Card"],
    ["David Smith", "Auroville", 22, "Firewire", 15, "EMI"],
    ["Isabella Lee", "Capitol Hill", 23, "Firewire", 10, "Cash"],
    ["Alice Lee", "Capitol Hill", 24, "Firewire", 20, "EMI"],
    ["Bob Johnson", "Capitol Hill", 25, "Firewire", 15, "EMI"]
]

store_data = {}

for row in data:
    store_location = row[1]
    selling_price = row[4]

    if store_location in store_data:
        if selling_price > store_data[store_location][0]["price"]:
            store_data[store_location] = [{
                "name": row[0],
                "month": row[2],
                "product": row[3],
                "price": selling_price,
                "payment": row[5]
            }]
        elif selling_price == store_data[store_location][0]["price"]:
            store_data[store_location].append({
                "name": row[0],
                "month": row[2],
                "product": row[3],
                "price": selling_price,
                "payment": row[5]
            })
    else:
        store_data[store_location] = [{
            "name": row[0],
            "month": row[2],
            "product": row[3],
            "price": selling_price,
            "payment": row[5]
        }]

for location, entries in store_data.items():
    for entry in entries:
        print(f"{entry['name']}")

import sys
sys.exit()

# import pandas as pd
#
# df = pd.read_csv('test.csv', index_col=0)
#
# df['price'] = df.Year.rank(method='dense').astype(int)
#
# data_columns = ['name', 'month', 'product','price','payment']