#Set

set1 = {1, 2, 3, 4, 5, False, True, "Aman", 23.23, "Rajesh", "Patel", "Sharma"} #Set1
set2 = {1, 2, 3, 4, 5, "Rajesh", "Patel", "ranjit"}
set3 = {462, 3297}
set4 = {"freefire", "enormous"}
set1.add("Ram chandra ") #Add an element to a set
set1.clear() #remove all elements from the set
print(set1.copy()) #Return a shallow copy of a set.
print(set1.difference(set2)) #Return a new set with elements in the set that are not in the others. (Return the value but doesn't with Original Set)
set1.difference_update(set2) #Update the set, removing elements found in others. (Work with Original Set)
set1.discard(1) #Remove an element from a set if it is a member.
print(set1.intersection(set2)) #Return a new set with elements common to the set and all others.(Return the value but doesn't with Original Set)
set1.intersection_update(set2) #Update the set, keeping only elements found in it and all others.(Work with Original Set)
print(set1.isdisjoint(set2)) #Return True if two sets have a null intersection.
print(set2.issubset(set1)) #Report whether another set contains this set.
print(set1.issuperset(set2)) #Report whether this set contains another set.
set2.pop() #Pop Any Element
set1.remove(False) #Remove an element from a set; it must be a member.
print(set1.symmetric_difference(set2)) #Return a new set with elements in either the set or other but not both.
set1.symmetric_difference_update(set2) #Update the set, keeping only elements found in either set, but not in both.
print(set1.union(set2)) #Return a new set with elements from the set and all others.
set1.update(set2, set3, set4) #Update the set, adding elements from all others.
print(set1) #Print the Set
