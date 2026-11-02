import gc
import time

class Demo:
    def __init__(self):
        self.ref = None

# Create circular references
def create_objects():
    a = Demo()
    b = Demo()

    a.ref = b
    b.ref = a

# Automatic garbage collection
print("Automatic Garbage Collection")

gc.enable()

for i in range(5):
    create_objects()

print("Garbage Collection Enabled:", gc.isenabled())

# Manual garbage collection
print("\nManual Garbage Collection")

gc.disable()
start = time.time()

collected = gc.collect()

end = time.time()

print("Objects Collected:", collected)
print("Time Taken:", end - start, "seconds")

# Enable garbage collection again
gc.enable()

print("Garbage Collection Enabled:", gc.isenabled())