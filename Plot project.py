

import matplotlib.pyplot as plt
x = range(30)
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.plot(x, y)
label=  [15, 52, 36, 80]
Data=['GABA', 'Dopamine', 'Seratonine', 'pottasium']
ax.set_xticks(label)
ax.set_xticklabels(Data)
plt.show()