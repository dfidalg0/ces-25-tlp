import pandas as pd
import numpy as np
import subprocess as sub
from common.utils import build, plot
from matplotlib import pyplot as plt
# import json

N = 2000

build('timeops')

p = sub.Popen(['bin/timeops.out', str(N)], stdout=sub.PIPE, universal_newlines=True)

data = pd.read_csv(p.stdout)

inc, dec = data['increment'], data['decrement']

# with open('data/timeops.json') as f:
#     data = json.load(f)

plt.rcParams.update({ 'font.size': 27 })

plt.title('Diferença entre os tempos médios de incremento e decremento\ndurante execuções')

plt.xlabel('Número da execução')
plt.ylabel('Incremento - Decremento (ns)')

# dummy, diff = data['x'], np.array(data['y'])

# fig = plt.gcf()

# plt.scatter(dummy, diff, s=7)

# fig.savefig('img/timeops.pgf')

diff = inc - dec

plot('timeops', np.arange(N), diff, mode='scatter', s=7)

print(f'Increment time was greater than decrement\'s {(diff > 0).sum()} times')
print(f'Decrement time was greater than increment\'s {(diff < 0).sum()} times')

lims = [-N//20, N + N//20]

plt.plot(lims, [0, 0], ls='dotted', color='orange', lw=2)

plt.xlim(lims)
plt.ylim([-5, 5])

plt.show()
