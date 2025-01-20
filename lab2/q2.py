person={
    "name": "Palak",
    "age": 22,
    "city": "Dehradun"
}
print("Name: ",person["name"])
print("Age: ",person["age"])
print("City: ",person["city"])
person["email"]="palak.109569@stu.upes.ac.in"
person["age"]=23
print("Updated dictionary: ",person)
if "city"=="Dehradun" in person:
    print("Key city exists in dictionary")
print("Keys: ",list(person.keys()))
print("Values: ",list(person.values()))