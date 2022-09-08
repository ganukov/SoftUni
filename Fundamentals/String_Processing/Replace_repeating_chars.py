from itertools import groupby, chain, islice

text = input()
print(''.join(chain.from_iterable(islice(g, 1) for k, g in groupby(text))))