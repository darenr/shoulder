from __future__ import print_function

import heapq

class MaxHeapObj(object):

    def __init__(self, key, val):
        self.key= key
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class MaxHeap(object):

    def __init__(self):
        self.h = []

    def heap_push(self, k, v):
        heapq.heappush(self.h, MaxHeapObj(k, v))

    def heap_pop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i].val

    def __len__(self):
        return len(self.h)

if __name__ == '__main__':
    maxh = MaxHeap()
    maxh.heap_push(1, 12)
    maxh.heap_push(2, 69)
    maxh.heap_push(3, 2)
    print(maxh.heap_pop().key)
