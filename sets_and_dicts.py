new_set={1,2,3,4,5,4,4,5}

print(new_set)

new_set.clear()
new_set.add("Docker")
print(new_set)

new_set.add(1)
new_set.add(2)
new_set.add(3)
new_set.add(4)
new_set.add(50)
new_set.add(600)
print(new_set)
new_set.pop()

print(new_set)


#######dicts 

first_dict={
    id: "1",
    'name':"Daniyal",
    'age':"25",
    "type":"student",
}

print(first_dict)

print(first_dict.values())

id=first_dict[id]
name_of_student=first_dict["type"]
print(id)
print(name_of_student)

marks={'maths': "20",'chemistry':"30",'physics':"50",}

for mark in marks.values():
    print(mark)

for mark in marks:
    print(marks)