

list = ["poop", "pee", "fart", "fart"]
list_2 = ["poop", "fart"]
if "fart" in list:
    print("Fart")

for x in list_2:
    if x in list:
        print(x)
