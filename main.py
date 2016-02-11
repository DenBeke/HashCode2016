import sys

class Drone:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.counter = 0

class Warehouse:
	def __init__(self, x, y, items):
		self.x = x
		self.y = y
		self.items = items

class Order:
	def __init__(self, x, y, items):
		self.x = x
		self.y = y
		self.items = items


height, width, numDrones, numTurns, maxLoad = map(int, sys.stdin.readline().split())
numProductsTypes = sys.stdin.readline()

productTypes = []

for t in sys.stdin.readline().split():
	productTypes.append(int(t))

numWarehouses = int(sys.stdin.readline())



warehouses = []

for i in range(numWarehouses):
	x, y = map(int, sys.stdin.readline().split())
	items = map(int, sys.stdin.readline().split())
	warehouses.append(Warehouse(x, y, items))


numOrders = int(sys.stdin.readline())
orders = []

for i in range(numOrders):
	x, y = map(int, sys.stdin.readline().split())
	sys.stdin.readline()
	items = map(int, sys.stdin.readline().split())
	orders.append(Order(x, y, items))


print(height, width, numDrones, numTurns, maxLoad)
print(productTypes)
print(warehouses)
print(orders)

# Init drones
drones = [Drone(0,0) for _ in range(numDrones)]


def findImminentDrone():
	return min(drones, key = lambda drone: drone.counter)


#for order in orders:
	
print(findImminentDrone())

