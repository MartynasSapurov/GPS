my_list = ["a123", "b123", "c123", "d123"]
my_tuple = ("a123", "b123", "c123", "d123")
my_set = {"a123", "b123", "c123", "d123"}
my_dict = {"vienas": "one", "du":"two", "trys":"three"}

my_construction = [{"vienas": "one", "du":"two", "trys":"three"}, ["a123", "b123", "c123", "d123"], 5]


print(my_list)
print(type(my_list))

print(my_list[1][:-1])
print("*"*40)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[1][:-1])

my_list.append("e123")
print(my_list)
print(type(my_list))
other_tuple = ("e123", )
print("*"*40)

my_tuple += other_tuple
print(my_tuple)
print(type(my_tuple))
print("*"*40)

print(my_set)
print(type(my_set))
print("*"*40)

print(my_dict)
print(type(my_dict))
print(my_dict["vienas"])

print("*"*40)
for item in my_dict:
    print(f"Indeksas = {item}, vertė = {my_dict[item]}")
print("*"*40)

print(my_construction[1][1][2])

my_gen = tuple(x for x in(range(20)))

print(my_gen)

my_new_dict = {value: item for item, value in my_dict.items()}

print(my_new_dict)
