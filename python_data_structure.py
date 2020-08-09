Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DATA_STRUCTURES_PYTHON
>>> 
>>> #		1) LIST
>>> 
>>> names=['joey','chandler','ross']
>>> print (names)
['joey', 'chandler', 'ross']
>>> type(names)
<class 'list'>
>>> 
>>> numberlist=[1,2,3,4,5]
>>> print(numberlist)
[1, 2, 3, 4, 5]
>>> type(numberlist)
<class 'list'>
>>> 
>>> numbers1=[1,2,4,5,7,8]
>>> numbers2=[10,20,40,50,70,80]
>>> print(numbers1+numbers2)
[1, 2, 4, 5, 7, 8, 10, 20, 40, 50, 70, 80]
>>> print(numbers1*3)
[1, 2, 4, 5, 7, 8, 1, 2, 4, 5, 7, 8, 1, 2, 4, 5, 7, 8]
>>> numbers2[3]
50
>>> numbers2[3:]
[50, 70, 80]
>>> numbers2[0:3]
[10, 20, 40]
>>> del numbers1[4]
>>> prunt(numbers1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    prunt(numbers1)
NameError: name 'prunt' is not defined
>>> print(numbers1)
[1, 2, 4, 5, 8]
>>> 
>>> 
>>> numbers1.append(1)
>>> print(numbers1)
[1, 2, 4, 5, 8, 1]
>>> 
>>> numbers1.index(1)
0
>>> string=['mangoes','apples','bananas']
>>> string.index('apples')
1
>>> 
>>> #			2 ) TUPLES
>>> 
>>> 
>>> myTuple=("C","C++","Python")
>>> print(myTuple)
('C', 'C++', 'Python')
>>> print(myTuple[2])
Python
>>> print(len(myTuple))
3
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> """Tuples are similar to list in that they store elements of varying data-types"""
'Tuples are similar to list in that they store elements of varying data-types'
>>> """...............
"""
'...............\n'
>>> """The main distiction between tuples and lists is that tuples are immutable
(Once you have created a tuple, you can't update the value of any element in the tuple, nor you can delete an element)
In terms of syntax, tuples differ from the list in that they use parenthesis, whereas lists use sqauare-brackets.
Even with all of these differences, tuples are still very similar to lists. Elements can be accessed through same process"""
"The main distiction between tuples and lists is that tuples are immutable\n(Once you have created a tuple, you can't update the value of any element in the tuple, nor you can delete an element)\nIn terms of syntax, tuples differ from the list in that they use parenthesis, whereas lists use sqauare-brackets.\nEven with all of these differences, tuples are still very similar to lists. Elements can be accessed through same process"
>>> """Python provides the following functionalities on  LIST--
	1) Add elements to list
	2) Delete elements from list
	3) Assigning elements to different lists
	4) Accessing elements from different lists

Python provides the following functionalities on TUPLES--
	1) Accessing elements from a Tuple
	2) Deleting elements from a tuple/different tuples"""
'Python provides the following functionalities on  LIST--\n\t1) Add elements to list\n\t2) Delete elements from list\n\t3) Assigning elements to different lists\n\t4) Accessing elements from different lists\n\nPython provides the following functionalities on TUPLES--\n\t1) Accessing elements from a Tuple\n\t2) Deleting elements from a tuple/different tuples'
>>> 
>>> 
>>> 
>>> #			3) SETS
>>> 
>>> 
>>> """A SET is an unorderd and unindexed collection of data-type that is iterable, mutable, and has no duplicate elements.
	It is represented using curly braces{}
The mjor advantage of using SET,as opposed to LIST,is that it has highly optimized method for checking whether a specific element is contained in the set
(based on a data structure- HASH TABLE)

Python provides the followinf methods on SETS:
	1) Adding elements into SET(s)
	2) Insertion of SETS
	3) Difference between SETS
	4) Clear SETS"""
'A SET is an unorderd and unindexed collection of data-type that is iterable, mutable, and has no duplicate elements.\n\tIt is represented using curly braces{}\nThe mjor advantage of using SET,as opposed to LIST,is that it has highly optimized method for checking whether a specific element is contained in the set\n(based on a data structure- HASH TABLE)\n\nPython provides the followinf methods on SETS:\n\t1) Adding elements into SET(s)\n\t2) Insertion of SETS\n\t3) Difference between SETS\n\t4) Clear SETS'
>>> 
>>> 
>>> mySet={"C","C++","Python"}
>>> print(mySet)
{'Python', 'C', 'C++'}
>>> 
>>> print(len(mySet))
3
>>> mySet.add("Java")
>>> print(mySet)
{'Java', 'Python', 'C', 'C++'}
>>> 
>>> mySet.remove("C")
>>> print(mySet)
{'Java', 'Python', 'C++'}
>>> 
>>> """SETS DO'NT SUPPORT INDEXING"""
"SETS DO'NT SUPPORT INDEXING"
>>> 
>>> mySet[2]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    mySet[2]
TypeError: 'set' object is not subscriptable
>>> print(mySet[2])
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(mySet[2])
TypeError: 'set' object is not subscriptable
>>> 
>>>  """SETS DO'NT SUPPORT SORTING"""
 
SyntaxError: unexpected indent
>>> """SETS DO'NT SUPPORT SORTING"""
"SETS DO'NT SUPPORT SORTING"
>>> 
>>> mySet.sort()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    mySet.sort()
AttributeError: 'set' object has no attribute 'sort'
>>> 
>>> 
>>> 
>>> #			DICTIONARY
>>> 
>>> """Like lists and tuples , dictionary data structures store a collection of elements .However, they differ quite a bit from tuples and lists because they are key-balue stores.
(you give each value a key; most commonly, a string or an integer -- that can be used to access the elements at a later-time )
When you have a large amount of data, this is more efficient for accessing data, than traversing an entire list to find your element.

Python provides the following Functionalities on Dictionaries--
	1) Accessing Dictionary elements
	2) Assigning values to dictionary elements
	3) Deleting Dictionary elements"""
'Like lists and tuples , dictionary data structures store a collection of elements .However, they differ quite a bit from tuples and lists because they are key-balue stores.\n(you give each value a key; most commonly, a string or an integer -- that can be used to access the elements at a later-time )\nWhen you have a large amount of data, this is more efficient for accessing data, than traversing an entire list to find your element.\n\nPython provides the following Functionalities on Dictionaries--\n\t1) Accessing Dictionary elements\n\t2) Assigning values to dictionary elements\n\t3) Deleting Dictionary elements'
>>> 
>>> 
>>> myDict= {"C":"Basic", "C++":"Moderate","Java":"Advanced"}
>>> print(myDict)
{'C': 'Basic', 'C++': 'Moderate', 'Java': 'Advanced'}
>>> 
>>> print(len(myDict))
3
>>> myDict[2]
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    myDict[2]
KeyError: 2
>>> myDict["Java"]
'Advanced'
>>> 
>>> myDict.get("C")
'Basic'
>>> 
>>> myDict["Python"]=["Cool"]
>>> myDict
{'C': 'Basic', 'C++': 'Moderate', 'Java': 'Advanced', 'Python': ['Cool']}
>>> 
>>> 
>>> myDict["PHP"]="Web Development"
>>> myDict
{'C': 'Basic', 'C++': 'Moderate', 'Java': 'Advanced', 'Python': ['Cool'], 'PHP': 'Web Development'}
>>> 
>>> del myDict["Python"]
>>> myDict
{'C': 'Basic', 'C++': 'Moderate', 'Java': 'Advanced', 'PHP': 'Web Development'}
>>> 
>>> myDict["C"]="Beginner"
>>> myDict
{'C': 'Beginner', 'C++': 'Moderate', 'Java': 'Advanced', 'PHP': 'Web Development'}
>>> 
>>> myDict.pop("PHP")
'Web Development'
>>> myDict
{'C': 'Beginner', 'C++': 'Moderate', 'Java': 'Advanced'}
>>> myDict["PHP"]
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    myDict["PHP"]
KeyError: 'PHP'
>>> myDict.get("PHP")
>>> myDict.clear()
>>> myDict
{}
>>> del myDict
>>> myDict
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    myDict
NameError: name 'myDict' is not defined
>>> 
