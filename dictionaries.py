mont_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"

}
# Ordered from python version 3.7 and above
# Every key in dictionary needs to be unique and behind every key pair value there needs to be comma

print(mont_Conversions.get("Jan", ))
print(mont_Conversions["Nov"])
# There are multiple ways to get  the value you want from dictionary
# When using .get with dictionaries u can set default value to spit out when the key is not found
print(mont_Conversions.get("Paprika", "Key not found error"))
print(mont_Conversions["Jan"])

d = {'k1': 1, "k2": 2, "k3": [0, 1, 2]}
print(d["k3"][0])  # u can put list into a dictionary and access the objects of the list
for smth, itm in d.items():
    print(itm)
d["k3"][0] = 3  # u can even change single objects of the list with dictionaries
print(d["k3"])
# we use ** to unpack dictionaries
d["k4"] = 500
print(d["k4"])
print(d.keys())
print(d.values())
print(d.items())
