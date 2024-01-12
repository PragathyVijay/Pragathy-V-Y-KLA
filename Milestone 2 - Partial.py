import matplotlib.pyplot as plt
from numpy import sin, cos, pi, linspace

input_file = "Testcase1.txt"
output_file = "mile1o1.txt"

with open(input_file, "r") as file1:
    lines = file1.readlines()
temp = []
for x in lines:
    temp.append(x)
D = temp[0]
DS = temp[1]
DSV = temp[2]
RD = temp[3]
diameter = int(D[14:])
diesize = int(DS[8:10].strip())
dieshiftvector = DSV[15:].strip()
referencedie = RD[13:]

count = int(diameter/diesize)

x = -1
y = -1

coords = []
coords.append((0,0))
for i in range(0, count):
    x += 1
    for y in range(0, count):
        y += 1
        coords.append((x,y))
        coords.append((-x,-y))
print(coords)

plt.plot(0,0, color = 'red', marker = 'o')

r = diameter/2
angles = linspace(0 * pi, 2 * pi, 100) 
xs = cos(angles)
ys = sin(angles)

plt.plot(xs, ys, color = 'green')
