from collections import namedtuple, deque, Counter

# namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person(name="Alice", age=30)
print("Person:", p)
print("Person:", p) 
print("Name:", p.name)  
print("Age:", p.age)
# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
print("Deque:", dq)

# Counter
counter = Counter('abracadabra')
print("Character count:", counter)
