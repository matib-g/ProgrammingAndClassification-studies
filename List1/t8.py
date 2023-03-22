s = ['a', 'b', 'c', 'd']


def powerset(s):
    if len(s) <= 1:
        yield s
        yield []
    else:
        for item in powerset(s[1:]):
            yield [s[0]]+item
            yield item


seq = [i for i in powerset(s)]

print(seq)
