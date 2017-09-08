import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

min_value = 1
max_value = 10
players = 8
buyers = np.random.random_integers(min_value,max_value,players)
sellers = np.random.random_integers(min_value,max_value,players)

def counts(n,vec):
    for i in range(1,n+1):
        yield sum(vec==i)

count_buyers= np.fromiter(counts(max_value,buyers),dtype=int)
count_sellers= np.fromiter(counts(max_value,sellers),dtype=int)

tbuyers = np.column_stack((np.arange(10)+1,count_buyers,np.cumsum(count_buyers[::-1])))
tsellers = np.column_stack((count_sellers,np.cumsum(count_sellers)))
tableo = np.column_stack((tbuyers,tsellers))


davalues = open('davalues1.txt', 'w')
davalues.write(tabulate(tableo[:,[0,1,3]], tablefmt='psql'))
davalues.close()
print(tabulate(tableo[:,[0,1,3]]))
plt.figure()
plt.step(tbuyers[:,2],tbuyers[:,0][::-1],label=('Demand'))
plt.step(tsellers[:,1],tbuyers[:,0],label=('Supply'))
plt.legend()
plt.axis([0, players, 0, max_value])
plt.xlabel('traders')
#plt.savefig('daplot.png')
plt.show()

