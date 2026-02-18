d1 = {"Ram":100,"Kiran":90,"Sneha":99.999,"String":33.33,"l1":[12,22],"t1":("Ram","Sita")} 
print(d1.items()) #Return a set-like object providing a view on the dict's items.
print(d1["l1"]) #In Dictionary , Index are defined ! 
print(d1.keys()) #Return Keys 
print(d1.values()) #Return Values
print(d1.get("Rama")) #Return the value for key if key is in the dictionary, else default.
d1.update({"Ram":33.333}) #Returns None , And .update used to Update the Value of the key
print(d1.copy()) #Return a shallow copy of the dict.
print(d1.pop("Ram")) # if the key is not found, return the default if given; otherwise, raise a KeyError.
print(d1.fromkeys({"Rakesh","Prasant"})) #Create a new dictionary with keys from iterable and values set to value.
print(d1.setdefault(("Stunt",12422)))  #setdefault() gets the value if key exists ,Adds the key if it doesn’t ,Returns the value either way
print(d1.clear()) #removes all items from the dictionary.
print(d1) #Print the original dictionary