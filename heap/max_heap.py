class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def insert(self, val):
        self.heap.append(val)
        curr = len(self.heap) - 1
        while curr != 0 and self.heap[self.parent(curr)] < self.heap[curr]:
            self.heap[self.parent(curr)], self.heap[curr] = self.heap[curr], self.heap[self.parent(curr)]
            curr = self.parent(curr)

    def extract_max(self):
        if self.heap is None:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return val

    def heapify(self, index):
        l = self.left(index)
        r = self.right(index)
        large = index

        if l < len(self.heap) and self.heap[l] > self.heap[large]:
            large = l
        if r < len(self.heap) and self.heap[r] > self.heap[large]:
            large = r

        if index != large:
            self.heap[large], self.heap[index] = self.heap[index], self.heap[large]
            self.heapify(large)

heap = MaxHeap()

nums = [23,45,6,1,67,3,232]
for i in nums:
    heap.insert(i)

print(heap.heap)
print(heap.extract_max())