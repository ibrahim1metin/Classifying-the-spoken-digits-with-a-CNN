import matplotlib.pyplot as plt
import os
from groupData import names

counts=[len(os.listdir(f"data/{i}")) for i in names]
print(counts)
plt.bar(names,counts)
plt.show()