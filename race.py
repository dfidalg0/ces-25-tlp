# import json
import subprocess as sub
import numpy as np
from matplotlib import pyplot as plt
from common.utils import build, plot

build('race')

p = sub.run(['bin/race.out', '1000000'], stdout=sub.PIPE, universal_newlines=True)

data = [int(n) for n in p.stdout.split('\n')[:-1]]

x, y = np.unique(data, return_counts=True)

# with open('data/race.json') as f:
#     data = json.load(f)
#     x, y = data['x'], data['y']

plt.rcParams.update({ 'font.size': 30 })

plt.title('Condição de corrida no problema incremento - decremento')

plt.xlabel('Valor da variável')
plt.ylabel('Frequência')

plot('race', x, y)

plt.show()
