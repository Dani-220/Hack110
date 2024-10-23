"""Practice in Class with For Loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet that they're a good boy!
for animal in pets:
    print(f"Good boy, {animal}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# Print each index: name
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")

for x in [1, 2, 3]:
    print(x)
