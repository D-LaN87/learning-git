shopping_list = {
    "piekarnia" : ["chleb", "pączek", "bułki", "drożdżówka"],
    "warzywniak" : ["marchew", "seler", "rukola", "pomidor"],
}
for k, v in shopping_list.items():
    print("Wchodzę do " + str(k).title() + ", kupuję tu następujące rzeczy: " + str(v).title())

items = 0

for item in shopping_list.keys():
    number_of_items = shopping_list[item]
    for i in number_of_items:
        items = items + 1
        
print("W sumię kupuję " + str(items) + " produktów. \n")
