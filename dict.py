my_dict = {

    "name": "asit",
    "age": 22,
    "salary": 100.50,
    "has_6_pack_abs": False

}

# ways to print a key's value from a dict
print("ways to print a key's value from a dict")
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.get("gender"))        # no such key so None will be printed
print(my_dict.get("gender","NA"))   # if no such key NA will be printed
print()


# ways to iterate on the dict
print("ways to iterate on the dict")
for i in my_dict:       # this only gives the keys
    print(i)


for i,j in my_dict.items():     # both key and value
    print(f"{i}:{j}")

for i,j in zip(my_dict.keys(),my_dict.values()):    ## both key and value part 2
    print(f"{i}:{j}")

for ind,(i,j) in enumerate(my_dict.items(),start=1):    ## part 3
    print(f"{ind} = {i}:{j}")

print()



# other operations
print("other operations")
print(my_dict.keys())
print(my_dict.values())
print()



my_dict["gender"]="female"      # adds a key
my_dict.update({"gender": "male"})      # adds a key, updates the value of the key already exists
print(f"my dict after gender addition {my_dict}")


dict_copy = my_dict.copy()

dict_copy["name"]="shankar"

print(my_dict)
print(dict_copy)



#dict_copy.pop("name") # this will just pop that key
dict_copy["full_name"]=dict_copy.pop("name")
print(dict_copy)



# check availability of gender key in dict
if "gender" in dict_copy:
    print("gender key is available in dict")


last_item = dict_copy.popitem()
print(last_item)