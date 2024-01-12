def parent(n):
    return (n-1)//2
def left(n):
    return 2*n + 1
def right(n):
    return 2*n + 2

class MinHeap():
    def __init__(self, key):
        self.key = key
        self.heap = []
        self.index_map = {}

    def extract_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.index_map[self.heap[0]] = 0
        val = self.heap.pop()
        self._siftdown(0)
        return val
    
    def insert(self, item):
        self.heap.append(item)
        self.index_map[item] = len(self)-1
        self._siftup(len(self.heap)-1)

    def priority_decreased(self, val):
        self._siftup(self.index_map[val])

    def _siftdown(self, n):
        m = c = n
        while c <= parent(len(self)-1):
            if left(c) < len(self)\
                    and self.key(self.heap[left(c)]) < self.key(self.heap[m]):
                m = left(c)
            if right(c) < len(self)\
                    and self.key(self.heap[right(c)]) < self.key(self.heap[m]):
                m = right(c)
            if m != c:
                self.heap[c], self.heap[m] = self.heap[m], self.heap[c]
                self.index_map[self.heap[c]] = c
                self.index_map[self.heap[m]] = m
                c = m
            else:
                return

    def _siftup(self, n):
        c = n
        while c != 0:
            if self.key(self.heap[parent(c)]) > self.key(self.heap[c]):
                self.heap[parent(c)], self.heap[c] = self.heap[c], self.heap[parent(c)]
                self.index_map[self.heap[parent(c)]] = parent(c)
                self.index_map[self.heap[c]] = c
                c = parent(c)
            else:
                return

    def __len__(self):
        return len(self.heap)
