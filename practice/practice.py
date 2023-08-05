from typing import List



################# Using Set





inp_str = "Hello word"

freq = {}
j=""
for i in inp_str:

    if i in freq:

        freq[i] += 1

    else:

        freq[i] = 1

for v,k in freq.items():

    j = j + str(v) + str(k)


print(j)


print("Occurrence of all characters in GeeksforGeeks is : \n" + str(freq))

