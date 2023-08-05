import collections

numbersDeque = collections.deque((20,40,60,80))


# l = [20,40,60,80]

elem = numbersDeque.popleft()

print("popleft removed the number : %d"%(elem))


print("Deque elements after a popleft:")

print(list(numbersDeque))
