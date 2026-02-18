dictionary_data = {"Ram":100,"Kiran":90,"Sneha":99.999,"String":33.33,"list1":[12,22],"tuple1":("Ram","Sita")}
print(dictionary_data.items()) #Return a set-like object providing a view on the dict's items.
print(dictionary_data["list1"]) #In Dictionary , Index are defined !
print(dictionary_data.keys()) #Return Keys
print(dictionary_data.values()) #Return Values
print(dictionary_data.get("Rama")) #Return the value for key if key is in the dictionary, else default.
dictionary_data.update({"Ram":33.333}) #Returns None , And .update used to Update the Value of the key
print(dictionary_data.copy()) #Return a shallow copy of the dict.
print(dictionary_data.pop("Ram")) # if the key is not found, return the default if given; otherwise, raise a KeyError.
print(dictionary_data.fromkeys({"Rakesh","Prasant"})) #Create a new dictionary with keys from iterable and values set to value.
print(dictionary_data.setdefault(("Stunt",12422)))  #setdefault() gets the value if key exists ,Adds the key if it doesn't ,Returns the value either way
print(dictionary_data.clear()) #removes all items from the dictionary.
print(dictionary_data) #Print the original dictionary
