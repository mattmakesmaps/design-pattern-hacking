import random
import time
import copy

"""
The `clone()` method actually returns a copy of random list,
and doesn't generate a new random list

500th Element from each clone
0.371727186702
0.371727186702
0.371727186702
0.371727186702
0.371727186702
0.371727186702
0.371727186702
0.371727186702
0.371727186702
0.371727186702

Time - 111484.570503
"""

class RandomNumberGetter(object):

    def __init__(self, count):
        self.random_list = [random.random() for i in range(0, count)]

    def clone(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    start_time = time.time()
    # Generate Single Random Number Instance
    r = RandomNumberGetter(1000000)
    # Generate a list of of 10 clones()
    random_clones = [r.clone() for i in range(0, 10)]
    for clone in random_clones:
        print clone.random_list[500]
    end_time = time.time()
    print (end_time - start_time) * 10000

