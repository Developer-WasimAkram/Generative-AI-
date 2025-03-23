from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'nitish', 'age':'35'}
new_person1: Person = {'name':'nitish', 'age':34}

print(new_person)
print(new_person1)