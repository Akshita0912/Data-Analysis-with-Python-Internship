#Python program to create a dictionary and perform operations like addition,
#removal and modification 
dict={"name":"Akshita","age":"20","city":"Hyderabad"}
dict["country"] = "India"
del dict["city"]
dict["age"]=19
print("Original Dictionary:",dict)
print("Dictionary after adding a key-value pair:",dict)
print("Dictionary after removing a key-value pair:", dict)
print("Dictionary after modifying a value:",dict)
