import pandas as pd
import numpy as np
import subprocess as sub
from common.utils import build, plot
from matplotlib import pyplot as plt

N = 2000

build('versus')

p = sub.Popen(['bin/versus.out', str(N)], stdout=sub.PIPE)

data = pd.read_csv(p.stdout)

race, no_race = data['race'], data['no_race']

plt.rcParams.update({ 'font.size': 27 })

plt.title('Diferença entre os tempos médios de execução com e sem condição de corrida')

plt.xlabel('Número da execução')
plt.ylabel('Diferença de tempo de execução (ns)')

diff = race - no_race

plot('versus', np.arange(N), diff, mode='scatter', s=7)

print(f'Race time was greater than No Race\'s {(diff > 0).sum()} times')
print(f'No Race time was greater than Race\'s {(diff < 0).sum()} times')

lims = [-N//20, N + N//20]

plt.plot(lims, [0, 0], ls='dotted', color='orange', lw=2)

plt.xlim(lims)

plt.show()
