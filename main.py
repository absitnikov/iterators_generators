nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

# Задание 1
class FlatIterator:
    def __init__(self, list_iter):
        self.main = [x for xs in list_iter for x in xs]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor == len(self.main) - 1:
            raise StopIteration

        self.cursor += 1
        return self.main[self.cursor]


for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# Задание 2
def flat_generator(list_gen):
    for item in list_gen:
        for xs in item:
            yield xs


for item in flat_generator(nested_list):
    print(item)


# Задание 3
class FlatIterator:
    def __init__(self, list_iter):
        self.list_iter = list_iter

    def __iter__(self):
        self.iter_list = [iter(self.list_iter)]
        return self

    def __next__(self):
        while self.iter_list:
            try:
                item = next(self.iter_list[-1])
            except StopIteration:
                self.iter_list.pop()
                continue
            if isinstance(item, list):
                self.iter_list.append(iter(item))
                continue
            else:
                return item
        raise StopIteration


for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# Задание 4
def flat_generator(list_gen):
    for item in list_gen:
        if isinstance(item, list):
            for xs in flat_generator(item):
                yield xs
        else:
            yield item


for item in flat_generator(nested_list):
    print(item)