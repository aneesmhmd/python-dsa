class Heap:
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
        parent_idx = self.parent(curr)

        while curr != 0 and self.heap[parent_idx] > self.heap[curr]:
            self.heap[parent_idx], self.heap[curr] = self.heap[curr], self.heap[parent_idx]
            curr = parent_idx
            parent_idx = self.parent(curr)

    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        small = index

        if left < len(self.heap) and self.heap[left] < self.heap[small]:
            small = left
        if right < len(self.heap) and self.heap[right] < self.heap[small]:
            small = right

        while small != index:
            self.heap[small], self.heap[index] = self.heap[index], self.heap[small]
            self.heapify(small)

    def extract_min(self):
        if self.heap is None:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return val


heap = Heap()
nums = [45, 6, 1, 67, 3, 232]
for num in nums:
    heap.insert(num)

print(heap.heap)
# print(heap.extract_min())
print(heap.heap)
