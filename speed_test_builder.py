import abc
import random
import time

"""
0.951164170831
0.635751526473
0.880094673958
0.515287716476
0.853595653037
0.849445300196
0.861526385984
0.4431506249
0.152568525955
0.182548381711
10490.0288582
"""

# Director
class RandomDirector(object):
    def __init__(self):
        self.builder = None

    def create(self):
        # Create a new instance of the Product
        # To avoid sharing state.
        self.builder.new_randomnumbergetter_instance()
        self.builder.make_random_list()
        return self.builder.randomnumbergetter

# Builder Abstract Interface
# Defines that `make_random_list` should exist,
# but not how.
class RandomBuilderInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_random_list(self):
        raise

# Concrete Builder
# Uses random.random() method.
class RandomFloatGenerator(RandomBuilderInterface):

    def __init__(self, size):
        # Constructed with an instance of the product
        self.randomnumbergetter = None
        self.size = size

    # The director explicitly calls this method
    # to create a new instance of the product.
    # this avoids sharing state.
    # See: https://github.com/faif/python-patterns/blob/master/creational/builder.py
    def new_randomnumbergetter_instance(self):
        self.randomnumbergetter = RandomNumberGetter()

    def make_random_list(self):
        random_list = [
            random.random() for i in range(0, self.size)
        ]
        self.randomnumbergetter.random_list = random_list

class RandomIntGenerator(RandomBuilderInterface):

    def __init__(self, size):
        # Constructed with an instance of the product
        self.randomnumbergetter = RandomNumberGetter()
        self.size = size

    def make_random_list(self):
        self.randomnumbergetter.random_list = [
            random.randint() for i in range(0, self.size)
            ]

# Product
class RandomNumberGetter(object):

    def __init__(self):
        self.random_list = None

if __name__ == '__main__':
    start_time = time.time()
    # Instanciate the director
    d = RandomDirector()
    d.builder = RandomFloatGenerator(1000000)

    # Build an instance of the product
    random_instances = [d.create() for i in range(0, 10)]
    for inst in random_instances:
        print inst.random_list[500]

    end_time = time.time()
    print (end_time - start_time) * 10000
