import json

with open('faktine_nacionaline_kitu_energijos_saltiniu_gamyba.json') as file:
    output_data = json.load(file)

print(output_data)
print(type(output_data))
