#Set

s1 = {1,2,3,4,5,False,True,"Aman",23.23,"Rajesh","Patel","Sharma"} #Set1
s2 = {1,2,3,4,5,"Rajesh","Patel","ranjit"}
s3 = {462,3297}
s4 = {"freefire","enormous"}
s1.add("Ram chandra ") #Add an element to a set
s1.clear() #remove all elements from the set
print(s1.copy()) #Return a shallow copy of a set.
print(s1.difference(s2)) #Return a new set with elements in the set that are not in the others. (Return the value but doesn't with Original Set)
s1.difference_update(s2) #Update the set, removing elements found in others. (Work with Original Set)
s1.discard(1) #Remove an element from a set if it is a member.
print(s1.intersection(s2)) #Return a new set with elements common to the set and all others.(Return the value but doesn't with Original Set)
s1.intersection_update(s2) #Update the set, keeping only elements found in it and all others.(Work with Original Set)
print(s1.isdisjoint(s2)) #Return True if two sets have a null intersection.
print(s2.issubset(s1)) #Report whether another set contains this set.
print(s1.issuperset(s2)) #Report whether this set contains another set.
s2.pop() #Pop Any Element
s1.remove(False) #Remove an element from a set; it must be a member.
print(s1.symmetric_difference(s2)) #Return a new set with elements in either the set or other but not both.
s1.symmetric_difference_update(s2) #Update the set, keeping only elements found in either set, but not in both.
print(s1.union(s2)) #Return a new set with elements from the set and all others.
s1.update(s2,s3,s4) #Update the set, adding elements from all others.
print(s1) #Print the Set 




