# Create a function call gen_elements that when given an integer n returns
# an array of all n-size arrays that contains all possible
# boolean combinations of 0 and 1.

from enum import Enum

def gen_elements(n):
    if n == 1:
        return [[0], [1]]
    else:
        return [[0] + x for x in gen_elements(n-1)] + [[1] + x for x in gen_elements(n-1)]

class Index(Enum):
    ALICE = 0
    BOB = 1
    CAROL = 2
    GLOVES = 3
    HAT = 4

preconditions = [
    # lambda arr: not arr[Index.GLOVES.value] or (arr[Index.GLOVES.value] and not arr[Index.BOB.value]),
    # lambda arr: not arr[Index.HAT.value] or (arr[Index.HAT.value] and not arr[Index.CAROL.value]),
    # lambda arr: bool(arr[Index.GLOVES.value]) or (not arr[Index.GLOVES.value] and not arr[Index.ALICE.value])
    lambda arr: not arr[Index.GLOVES.value] or not arr[Index.BOB.value],
    lambda arr: bool(arr[Index.CAROL.value]) or arr[Index.HAT.value],
    lambda arr: bool(arr[Index.GLOVES.value]) or not arr[Index.ALICE.value]
]

def to_string(arr):
    return " & ".join(["T" if x else "F" for x in arr])

elements = gen_elements(5)


def filterElements(arr):
    sum = arr[0] + arr[1] + arr[2]
    return sum == 2

elements = filter(filterElements, elements)

results = []

for(element) in elements:
    truthful = 0
    print(to_string(element), end=" & ")
    for(precondition) in preconditions:
        print("T" if precondition(element) else "F" , end=" & ")
        truthful += 1 if precondition(element) else 0
    if truthful == 1:
        results.append(element)
    print()

print("Results:")
for(result) in results:
    print(to_string(result), end = " & ")
    for(precondition) in preconditions:
        print("T" if precondition(result) else "F" , end=" & ")
    print()



# print(gen_elements(3))