import matplotlib.pyplot as plt
a = 1.1

def initialize():
    global x, result
    x = 1.
    result = [x]


def observe():
    global x, result
    result.append(x)




def update():
    global x, result
    x = a * x

initialize()
for t in range(30):
    update()
    observe()


plt.plot(result)
plt.show()
print(result)
        
