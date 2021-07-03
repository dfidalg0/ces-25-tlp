from pathlib import Path
import json
import os
from matplotlib import pyplot as plt

ROOT = Path(__file__).parent.parent.resolve()

def root(f):
    def wrapper(*args, **kw):
        cwd = os.getcwd()
        os.chdir(ROOT)
        ret = f(*args, **kw)
        os.chdir(cwd)

        return ret

    return wrapper

@root
def build (*names):
    if not os.path.isdir('bin'):
        os.makedirs('bin')

    def build_single(name):
        print(f'Building {name}... ', end='', flush=True)
        os.system(f'g++ src/{name}.cpp -lpthread -o bin/{name}.out')
        print('Done')

    if names:
        for name in names:
            build_single(name)
    else:
        for name in os.listdir('src'):
            build_single(name[:-4])

@root
def plot(name, X, Y, *, mode='plot', **opts):
    if not os.path.isdir('data'):
        os.makedirs('data')

    with open(f'data/{name}.json', 'w') as f:
        json.dump({
        'x': [float(x) for x in X],
        'y': [float(y) for y in Y]
    }, f)

    if not os.path.isdir('img'):
        os.makedirs('img')

    getattr(plt, mode)(X, Y, **opts)

    plt.savefig(f'img/{name}.pgf')
