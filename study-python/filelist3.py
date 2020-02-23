import pathlib

path = pathlib.Path('.')

for po in path.iterdir():
    if po.match('*.py'):
        print(po)
