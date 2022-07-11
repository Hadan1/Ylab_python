class CyclicIterator:
    """Циклический итератор."""

    def __init__(self, input_data):
        self.input_data = input_data
        self.iterator = iter(self.input_data)

    def __iter__(self):
        return self

    def __next__(self):
        """Проводит итерацию, после всех итераций переинициализируется и начинается заново."""
        try:
            return next(self.iterator)
        except StopIteration:
            self.__init__(self.input_data)
            return next(self.iterator)


if __name__ == '__main__':
    data = [1, 'Test', (1, 2, 3)]  # входные данные, указываются вручную

    for i in CyclicIterator(data):
        print(i)
