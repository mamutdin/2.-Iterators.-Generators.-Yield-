from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

nested_list2 = [
    ['a', ['b', 'c']],
    ['d', ['e', 'f', ['h', False]]],
    [[1, 2], None]
]

# l1 = chain.from_iterable(nested_list)
# l2 = chain.from_iterable(nested_list)
# print(list(l1))
# for i in list(l2):
#     print(i)

class FlatIterator:

    def __init__(self, my_list):
        self.my_list = sum(my_list, [])

    def __iter__(self):
        self.l = iter(self.my_list)
        return self

    def __next__(self):
        return next(self.l)

def flat_generator(my_list):
    for l in my_list:
        for i in l:
            yield i

def flat_generator2(my_list):
    for l in my_list:
        if isinstance(l,list):
            for i in flat_generator2(l):
                yield i
        else:
            yield l

if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        print(item)
    print('*'*40)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('*'*40)
    for item in flat_generator(nested_list):
        print(item)
    print('*'*40)
    for item in flat_generator2(nested_list2):
        print(item)

