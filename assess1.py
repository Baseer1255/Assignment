#Q1
mylist=[67,873,90,50,70,
        8.6,9.8,10.8,7.9,8.8,
        "baseer","hi","now","hi"]
#Q2
mylist.append("yet")
#append function is used to add values at the end.
#Q3
list2=[]
#this is an empty list.
list2.insert(0,98)
#insert 98 at index 0
#Q4
for lists in list2:
   print(lists)
#Q5
we=[89,34,82,67,983,836,29,93,76,3]
we.sort(reverse=False)
#values in ascending
print(we)
we.sort(reverse=True)
#values in descending
print(we)
#Q6
x=["hi","hello","bye","my","no","hey","how","why","what","like"]
x.sort(reverse=True)
print(x)
x.sort(reverse=False)
print(x)
#Q7
now=[]
now=[]
pos=int(input("enter location where to add element"))
val=int(input("enter value"))
for i in now:
    print(i)
#Q8
print(max(we))
print(min(we))
#Q9
h=[873,764,[897,9]]
print(h)
#Q10
y=[8,98,46,34,67,43]
y.append(99)
y.insert(3,81)
y.remove(8)
f=y.copy()
o=y.pop(4)
print(y)
print(f)
print(o)


    
