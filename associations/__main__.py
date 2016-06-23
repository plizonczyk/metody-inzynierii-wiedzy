from pprint import pprint

data_file = 'associations/data.txt'
min_support_coeff = 0.3
min_confidence_coeff = 0.6

print("Using coefficients: support", min_support_coeff, "confidence", min_confidence_coeff, '\n')

transactions = {}

# read data and do equivalent class transformation
with open(data_file) as data:
    transactions_number = 0
    for row in data:
        elements = row.split()
        element_id = elements[0]
        for element in elements[1:]:
            if element in transactions:
                transactions[element].add(element_id)
            else:
                transactions[element] = set(element_id)
        transactions_number += 1

# extract frequent items in transactions
frequent_threshold = 0.33 * transactions_number
frequent_items = [(k, len(v)/transactions_number) for k, v in transactions.items() if len(v) >= frequent_threshold]
print("Frequent items:", frequent_items, '\n')

# find associations
associations = []
for item1 in transactions.keys():
    for item2 in transactions.keys():
        if item1 == item2:
            continue
        support = len(transactions[item1] | transactions[item2]) / transactions_number
        confidence = len(transactions[item1] & transactions[item2]) / len(transactions[item1])
        if support >= min_support_coeff and confidence >= min_confidence_coeff:
            associations.append((item1, item2, support, confidence))

print("Associations:")
pprint(associations)
