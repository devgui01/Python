#List Methods
my_list = ["ram","gyan",1111.222,444,"33","Ramit sioeo","ram","ram"]
my_list.append("sita gita") #Append object to the end of the list.
ram_count = my_list.count("ram")#Return number of occurrences of value.
my_list.extend("slice")#Extend list by appending elements from the iterable.
ram_index = my_list.index("ram") #Return first index of value.
my_list.insert(1,"sita")#Insert object before index.
popped_item = my_list.pop(2)#Remove and return item at index (default last).
my_list.remove("ram") #Remove first occurrence of value.
my_list.reverse() #reverse the list
my_list.sort() #Sort the list in ascending order and return None.
print(ram_count, ram_index, my_list, popped_item) #print and return value (if possible)
