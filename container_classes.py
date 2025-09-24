"""
Container Classes - Week 2
CSC 242 - Advanced Class Concepts

This file demonstrates the implementation of abstract data types (ADTs):
- Queue (FIFO - First In, First Out)
- Stack (LIFO - Last In, First Out)
- Deque (Double-ended queue)
- Priority Queue
- Custom iterators

Author: CSC 242 Teaching Team
"""

from collections import deque
import heapq


# ============================================================================
# QUEUE IMPLEMENTATION (FIFO)
# ============================================================================

class Queue:
    """A First-In-First-Out (FIFO) container implementation"""
    
    def __init__(self):
        """Initialize empty queue"""
        self._items = []
        self._size = 0
    
    def enqueue(self, item):
        """Add item to the rear of the queue"""
        self._items.append(item)
        self._size += 1
        return f"Enqueued: {item}"
    
    def dequeue(self):
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        
        item = self._items.pop(0)
        self._size -= 1
        return item
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def rear(self):
        """Return the rear item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[-1]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self._size == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return self._size
    
    def clear(self):
        """Remove all items from the queue"""
        self._items.clear()
        self._size = 0
    
    def to_list(self):
        """Return a copy of the queue as a list"""
        return self._items.copy()
    
    # Iterator support
    def __iter__(self):
        """Make queue iterable (front to rear)"""
        return iter(self._items)
    
    def __len__(self):
        """Support len() function"""
        return self._size
    
    def __contains__(self, item):
        """Support 'in' operator"""
        return item in self._items
    
    def __str__(self):
        """Human-readable string representation"""
        if self.is_empty():
            return "Queue(empty)"
        return f"Queue(front={self.front()} ... rear={self.rear()}, size={self._size})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Queue({self._items})"


# ============================================================================
# STACK IMPLEMENTATION (LIFO)
# ============================================================================

class Stack:
    """A Last-In-First-Out (LIFO) container implementation"""
    
    def __init__(self):
        """Initialize empty stack"""
        self._items = []
        self._size = 0
    
    def push(self, item):
        """Add item to the top of the stack"""
        self._items.append(item)
        self._size += 1
        return f"Pushed: {item}"
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        
        item = self._items.pop()
        self._size -= 1
        return item
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self._size == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return self._size
    
    def clear(self):
        """Remove all items from the stack"""
        self._items.clear()
        self._size = 0
    
    def to_list(self):
        """Return a copy of the stack as a list (bottom to top)"""
        return self._items.copy()
    
    # Iterator support (top to bottom)
    def __iter__(self):
        """Make stack iterable (top to bottom)"""
        return reversed(self._items)
    
    def __len__(self):
        """Support len() function"""
        return self._size
    
    def __contains__(self, item):
        """Support 'in' operator"""
        return item in self._items
    
    def __str__(self):
        """Human-readable string representation"""
        if self.is_empty():
            return "Stack(empty)"
        return f"Stack(top={self.peek()}, size={self._size})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Stack({self._items})"


# ============================================================================
# DEQUE IMPLEMENTATION (Double-ended Queue)
# ============================================================================

class Deque:
    """A double-ended queue implementation"""
    
    def __init__(self):
        """Initialize empty deque"""
        self._items = []
        self._size = 0
    
    def add_front(self, item):
        """Add item to the front of the deque"""
        self._items.insert(0, item)
        self._size += 1
        return f"Added to front: {item}"
    
    def add_rear(self, item):
        """Add item to the rear of the deque"""
        self._items.append(item)
        self._size += 1
        return f"Added to rear: {item}"
    
    def remove_front(self):
        """Remove and return item from the front"""
        if self.is_empty():
            raise IndexError("Cannot remove from empty deque")
        
        item = self._items.pop(0)
        self._size -= 1
        return item
    
    def remove_rear(self):
        """Remove and return item from the rear"""
        if self.is_empty():
            raise IndexError("Cannot remove from empty deque")
        
        item = self._items.pop()
        self._size -= 1
        return item
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._items[0]
    
    def rear(self):
        """Return the rear item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._items[-1]
    
    def is_empty(self):
        """Check if the deque is empty"""
        return self._size == 0
    
    def size(self):
        """Return the number of items in the deque"""
        return self._size
    
    def clear(self):
        """Remove all items from the deque"""
        self._items.clear()
        self._size = 0
    
    # Iterator support
    def __iter__(self):
        """Make deque iterable (front to rear)"""
        return iter(self._items)
    
    def __len__(self):
        """Support len() function"""
        return self._size
    
    def __contains__(self, item):
        """Support 'in' operator"""
        return item in self._items
    
    def __str__(self):
        """Human-readable string representation"""
        if self.is_empty():
            return "Deque(empty)"
        return f"Deque(front={self.front()} ... rear={self.rear()}, size={self._size})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Deque({self._items})"


# ============================================================================
# PRIORITY QUEUE IMPLEMENTATION
# ============================================================================

class PriorityQueue:
    """A priority queue implementation using heap"""
    
    def __init__(self):
        """Initialize empty priority queue"""
        self._items = []
        self._index = 0  # To handle items with same priority
    
    def enqueue(self, item, priority=0):
        """Add item with given priority (lower number = higher priority)"""
        # Use index to maintain insertion order for items with same priority
        heapq.heappush(self._items, (priority, self._index, item))
        self._index += 1
        return f"Enqueued: {item} (priority: {priority})"
    
    def dequeue(self):
        """Remove and return highest priority item"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty priority queue")
        
        priority, index, item = heapq.heappop(self._items)
        return item
    
    def peek(self):
        """Return highest priority item without removing it"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self._items[0][2]  # Return the item part
    
    def peek_priority(self):
        """Return the priority of the highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self._items[0][0]  # Return the priority part
    
    def is_empty(self):
        """Check if the priority queue is empty"""
        return len(self._items) == 0
    
    def size(self):
        """Return the number of items in the priority queue"""
        return len(self._items)
    
    def clear(self):
        """Remove all items from the priority queue"""
        self._items.clear()
        self._index = 0
    
    def __len__(self):
        """Support len() function"""
        return len(self._items)
    
    def __str__(self):
        """Human-readable string representation"""
        if self.is_empty():
            return "PriorityQueue(empty)"
        return f"PriorityQueue(next={self.peek()}, priority={self.peek_priority()}, size={self.size()})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        items = [(priority, item) for priority, index, item in self._items]
        return f"PriorityQueue({items})"


# ============================================================================
# CIRCULAR BUFFER IMPLEMENTATION
# ============================================================================

class CircularBuffer:
    """A fixed-size circular buffer implementation"""
    
    def __init__(self, capacity):
        """Initialize circular buffer with fixed capacity"""
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self._buffer = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = 0
    
    def enqueue(self, item):
        """Add item to the buffer"""
        if self.is_full():
            # Overwrite oldest item
            self._front = (self._front + 1) % self._capacity
        else:
            self._size += 1
        
        self._buffer[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        return f"Added: {item}"
    
    def dequeue(self):
        """Remove and return oldest item"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty buffer")
        
        item = self._buffer[self._front]
        self._buffer[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self._buffer[self._front]
    
    def is_empty(self):
        """Check if buffer is empty"""
        return self._size == 0
    
    def is_full(self):
        """Check if buffer is full"""
        return self._size == self._capacity
    
    def size(self):
        """Return current number of items"""
        return self._size
    
    def capacity(self):
        """Return maximum capacity"""
        return self._capacity
    
    def to_list(self):
        """Return buffer contents as a list (in order)"""
        if self.is_empty():
            return []
        
        result = []
        index = self._front
        for _ in range(self._size):
            result.append(self._buffer[index])
            index = (index + 1) % self._capacity
        return result
    
    def __iter__(self):
        """Make buffer iterable"""
        return iter(self.to_list())
    
    def __len__(self):
        """Support len() function"""
        return self._size
    
    def __str__(self):
        """Human-readable representation"""
        return f"CircularBuffer({self.to_list()}, capacity={self._capacity})"
    
    def __repr__(self):
        """Developer representation"""
        return f"CircularBuffer(capacity={self._capacity}, items={self.to_list()})"


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_queue():
    """Demonstrate queue operations"""
    print("=== QUEUE (FIFO) DEMONSTRATION ===")
    
    q = Queue()
    print(f"Created queue: {q}")
    
    # Add items
    items = ["first", "second", "third", "fourth"]
    for item in items:
        print(f"  {q.enqueue(item)}")
    
    print(f"Queue after enqueuing: {q}")
    print(f"Front item: {q.front()}")
    print(f"Rear item: {q.rear()}")
    print(f"Queue size: {len(q)}")
    
    # Remove items
    print(f"\nDequeuing items:")
    while not q.is_empty():
        item = q.dequeue()
        print(f"  Dequeued: {item}, Remaining: {q}")
    
    # Demonstrate iterator
    q2 = Queue()
    for i in range(5):
        q2.enqueue(f"item_{i}")
    
    print(f"\nIterating through queue:")
    for item in q2:
        print(f"  {item}")


def demonstrate_stack():
    """Demonstrate stack operations"""
    print("\n=== STACK (LIFO) DEMONSTRATION ===")
    
    s = Stack()
    print(f"Created stack: {s}")
    
    # Add items
    items = ["bottom", "middle", "top"]
    for item in items:
        print(f"  {s.push(item)}")
    
    print(f"Stack after pushing: {s}")
    print(f"Top item: {s.peek()}")
    print(f"Stack size: {len(s)}")
    
    # Remove items
    print(f"\nPopping items:")
    while not s.is_empty():
        item = s.pop()
        print(f"  Popped: {item}, Remaining: {s}")
    
    # Demonstrate iterator (top to bottom)
    s2 = Stack()
    for i in range(5):
        s2.push(f"level_{i}")
    
    print(f"\nIterating through stack (top to bottom):")
    for item in s2:
        print(f"  {item}")


def demonstrate_deque():
    """Demonstrate deque operations"""
    print("\n=== DEQUE (DOUBLE-ENDED QUEUE) DEMONSTRATION ===")
    
    dq = Deque()
    print(f"Created deque: {dq}")
    
    # Add items to both ends
    print(f"Adding items to both ends:")
    print(f"  {dq.add_rear('center')}")
    print(f"  {dq.add_front('left')}")
    print(f"  {dq.add_rear('right')}")
    print(f"  {dq.add_front('far_left')}")
    
    print(f"Deque after additions: {dq}")
    
    # Remove items from both ends
    print(f"\nRemoving items from both ends:")
    print(f"  Removed from front: {dq.remove_front()}")
    print(f"  Removed from rear: {dq.remove_rear()}")
    print(f"  Deque after removals: {dq}")


def demonstrate_priority_queue():
    """Demonstrate priority queue operations"""
    print("\n=== PRIORITY QUEUE DEMONSTRATION ===")
    
    pq = PriorityQueue()
    print(f"Created priority queue: {pq}")
    
    # Add items with different priorities
    tasks = [
        ("Low priority task", 5),
        ("High priority task", 1),
        ("Medium priority task", 3),
        ("Urgent task", 0),
        ("Another medium task", 3)
    ]
    
    print(f"Adding tasks with priorities:")
    for task, priority in tasks:
        print(f"  {pq.enqueue(task, priority)}")
    
    print(f"Priority queue: {pq}")
    
    # Process tasks by priority
    print(f"\nProcessing tasks by priority:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"  Processing: {task}")


def demonstrate_circular_buffer():
    """Demonstrate circular buffer operations"""
    print("\n=== CIRCULAR BUFFER DEMONSTRATION ===")
    
    cb = CircularBuffer(3)  # Small buffer for demonstration
    print(f"Created circular buffer with capacity {cb.capacity()}: {cb}")
    
    # Fill the buffer
    print(f"Filling buffer:")
    for i in range(5):  # More items than capacity
        print(f"  {cb.enqueue(f'item_{i}')}")
        print(f"    Buffer: {cb}")
    
    # Show overwriting behavior
    print(f"\nBuffer after overwriting: {cb}")
    print(f"Current front item: {cb.front()}")
    
    # Empty the buffer
    print(f"\nEmptying buffer:")
    while not cb.is_empty():
        item = cb.dequeue()
        print(f"  Removed: {item}, Buffer: {cb}")


def container_comparison():
    """Compare different container behaviors"""
    print("\n=== CONTAINER COMPARISON ===")
    
    # Create all containers
    queue = Queue()
    stack = Stack()
    deque = Deque()
    
    # Add same items to all
    items = ['A', 'B', 'C']
    
    print(f"Adding items {items} to all containers:")
    for item in items:
        queue.enqueue(item)
        stack.push(item)
        deque.add_rear(item)
    
    print(f"Queue: {queue}")
    print(f"Stack: {stack}")
    print(f"Deque: {deque}")
    
    # Remove one item from each
    print(f"\nRemoving one item from each:")
    print(f"Queue dequeue: {queue.dequeue()} -> {queue}")
    print(f"Stack pop: {stack.pop()} -> {stack}")
    print(f"Deque remove_front: {deque.remove_front()} -> {deque}")


def practical_examples():
    """Show practical use cases for each container"""
    print("\n=== PRACTICAL USE CASES ===")
    
    # Queue: Print job queue
    print("1. Print Job Queue (FIFO):")
    print_queue = Queue()
    jobs = ["Document1.pdf", "Photo.jpg", "Report.docx"]
    
    for job in jobs:
        print_queue.enqueue(job)
        print(f"   Queued print job: {job}")
    
    print(f"   Processing jobs in order:")
    while not print_queue.is_empty():
        job = print_queue.dequeue()
        print(f"   Printing: {job}")
    
    # Stack: Undo operations
    print(f"\n2. Undo Operations (LIFO):")
    undo_stack = Stack()
    operations = ["Type 'Hello'", "Type ' World'", "Bold text", "Change color"]
    
    for op in operations:
        undo_stack.push(op)
        print(f"   Performed: {op}")
    
    print(f"   Undoing operations:")
    for _ in range(2):  # Undo last 2 operations
        if not undo_stack.is_empty():
            op = undo_stack.pop()
            print(f"   Undoing: {op}")
    
    # Priority Queue: Task scheduling
    print(f"\n3. Task Scheduling (Priority Queue):")
    scheduler = PriorityQueue()
    
    tasks = [
        ("Backup database", 2),
        ("Critical security update", 0),
        ("Generate monthly report", 3),
        ("Fix login bug", 1),
        ("Update documentation", 4)
    ]
    
    for task, priority in tasks:
        scheduler.enqueue(task, priority)
        print(f"   Scheduled: {task} (priority {priority})")
    
    print(f"   Executing tasks by priority:")
    while not scheduler.is_empty():
        task = scheduler.dequeue()
        print(f"   Executing: {task}")


def main():
    """Run all container class demonstrations"""
    print("📦 CONTAINER CLASSES - CSC 242 Week 2")
    print("=" * 60)
    
    demonstrate_queue()
    demonstrate_stack()
    demonstrate_deque()
    demonstrate_priority_queue()
    demonstrate_circular_buffer()
    container_comparison()
    practical_examples()
    
    print(f"\n" + "=" * 60)
    print("✅ All container class demonstrations complete!")
    
    print(f"\n💡 Key Concepts Demonstrated:")
    print(f"   1. Queue (FIFO) - First In, First Out")
    print(f"   2. Stack (LIFO) - Last In, First Out")
    print(f"   3. Deque - Double-ended queue operations")
    print(f"   4. Priority Queue - Items processed by priority")
    print(f"   5. Circular Buffer - Fixed-size with overwriting")
    print(f"   6. Iterator protocol implementation")
    print(f"   7. Container protocol (__len__, __contains__)")


if __name__ == "__main__":
    main()
