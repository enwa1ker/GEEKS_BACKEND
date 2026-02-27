def closest_number(numbers, target):

    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))

    return (target, sorted_numbers)

prices = [100, 250, 50, 400]

tax = list(map(lambda price: price * 1.2, prices))

print(f"Цены с налогом: {tax}")

words = ["geeks", "программирование", "код", "ноутбук", "github"]

long_words = list(filter(lambda word: len(word) > 4, words))

print(f"Длинные слова: {long_words}")
