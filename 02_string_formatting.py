# python >3.6

name = "Bob"
greeting = f"Hello, {name}"

print(greeting)
print(f"Hello, {name}")

name = "Rolf"

print(greeting)
print(f"Hello, {name}")

name = "Ramsy"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Maan")

print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Ramsy","Monday")

print(formatted)

