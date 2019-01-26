print("rawrr")

'''
fingerTest = [
61,
45,
63,
28,
48,
46,
1,
17,
15,
31,
52,
36,
54,
21,
7,
23,
41,
40,
24,
25,
10,
42,
12,
27,
51,
32,
2,
34,
55,
39,
56,
57,
58,
43,
11,
26,
13,
29,
60,
44,
62,
47,
0,
16,
14,
30,
49,
33,
50,
35,
3,
18,
53,
37,
4,
20,
6,
22,
5,
19,
59,
8,
9,
38
]



'''


#mappedOutput = []

fileIn = open("fingerTest_mapping.txt", "rt")

fingerTest = []

for line in fileIn:
	fingerTest.append(int(line))

'''
for item in fingerTest:
	print(item)#print(type(item))
'''

fileOut = open("converted_mapping.txt", "wt")

index = 0

for i in range(len(fingerTest)):
	for j in fingerTest:
		if i == j:
			fileOut.write(str(index) + "\n")
		index = index + 1
	index = 0

'''
for i in mappedOutput:
	print(i)
'''




			
