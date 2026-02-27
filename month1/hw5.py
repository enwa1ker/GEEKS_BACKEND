data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")


designations = [] 
codes = []         


for item in data:
    if item.isdigit():   
        codes.append(item)
    else:                
        designations.append(item)

operators = dict(zip(designations, [{c} for c in codes]))

operators.pop("Katel", None)
operators.pop("Fonex", None)

operators["O!"].update({"0700", "0500"})
operators["Megacom"].update({"0999", "0555"})
operators["Beeline"].update({"0222", "0777"})


for company, nums in operators.items():
    print(f"{company} - {nums}")


# Тут короче мой прошлый код и решения на счет текущего 

# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

# designations = []
# codes = []

# for item in data:
#     if item.isdigit():
#         codes.append(item)
#     else:
#         designations.append(item)

# # Создаём словарь через while
# operators = {}
# i = 0
# while i < len(designations) and i < len(codes):
#     operators[designations[i]] = {codes[i]}  # сразу как множество
#     i += 1

# # Удаляем нефункционирующие операторы
# if "Katel" in operators:
#     del operators["Katel"]
# if "Fonex" in operators:
#     del operators["Fonex"]
# operators = {}
# to_remove = ['Katel', 'Fonex']

# for d, c in zip(designations, codes):
#     if d not in to_remove:
#         operators[d] = {c}

#  Еще один способ удаления
# del operators["Katel"]
# del operators["Fonex"]

# operators['O!'].add('0700')
# operators['O!'].add('0500')

# operators['Megacom'].add('0999')
# operators['Megacom'].add('0555')

# operators['Beeline'].add('0222')
# operators['Beeline'].add('0777')


# for company, nums in operators.items():
#     print(f"{company} - {nums}")


