import collections
deque = collections.deque(["5000","6000","7000"])
print(deque)

print("Adding to right:")
deque.append("8000")
print(deque)


print("Adding to left:")
deque.appendleft("4000")
print(deque)

print("Removing to the right:")
deque.pop()
print(deque)

print("Removing to the left:")
deque.popleft()
print(deque)

print("Reversing the deque:")
deque.reverse()
print(deque)
