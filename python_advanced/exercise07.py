# 要求：编写图形管理器，将其变为可迭代对象,并迭代

class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__graphics)


class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


class Graphic:
    def calculate_area(self):
        raise NotImplementedError()


if __name__ == '__main__':
    manager = GraphicManager()
    manager.add_graphic(Graphic())
    manager.add_graphic(Graphic())
    manager.add_graphic(Graphic())
    iterator = manager.__iter__()

    while True:
        try:
            item = iterator.__next__()

        except StopIteration:
            break
        print(item)
