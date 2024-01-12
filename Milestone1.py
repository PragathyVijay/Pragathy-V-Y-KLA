import matplotlib.pyplot as plt
from numpy import sin, cos, pi, linspace
import math

def deg2rad(deg):
    return deg * pi / 180

input_file = "Testcase1.txt"
output_file = "mile1o1.txt"

with open(input_file, "r") as file1:
    lines = file1.readlines()
temp = []
for x in lines:
    temp.append(x)
D = temp[0]
N = temp[1]
A = temp[2]
diameter = int(D[-4:].strip())
n = int(N[-3:])
if input_file == "Testcase3.txt" or input_file == "Testcase4.txt":
    angle = int(A[-3:])
elif input_file == "Testcase2.txt":
    angle = int(A[-2:])
else:
    angle = int(A[-1:])

plt.plot(0,0, color = 'red', marker = 'o')

r = diameter/2
angles = linspace(0 * pi, 2 * pi, 100) 
xs = cos(angles)
ys = sin(angles)

plt.plot(xs, ys, color = 'green')
plt.xlim(-r, r)
plt.ylim(-r, r)
plt.gca().set_aspect('equal')

plt.plot(r-0.5, 0, marker = 'P', color = 'blue')
plt.plot(-r+0.5, 0, marker = 'o', color = 'red')
plt.plot([r, -r], [0, 0], color = 'red')

plt.plot([0, r * cos(deg2rad(angle))], [0, r * sin( deg2rad(angle))], color = "black")

x = r*math.cos(deg2rad(angle))
y = r*math.sin(deg2rad(angle))

xstep = (2*x)/(n-1)
ystep = (2*y)/(n-1)

a = -x
b = -y
coords = []
coords.append((round(a,4),round(b,4)))

for i in range(0, n-1):
    a += xstep
    an = round(a,4)
    b += ystep
    bn = round(b,4)
    coords.append((an,bn))

with open(output_file, "w") as file2:
    for x in coords:
        x = str(x)
        file2.write(x)
        file2.write("\n")
