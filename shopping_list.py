shopping_list = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"],
}

for k, v in shopping_list.items():
    print("Wchodzę do " + str(k).title() + ", kupuję tu następujące rzeczy: " + str(v).title())
