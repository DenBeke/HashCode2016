import sys

def print_err(*args):
	sys.stderr.write(' '.join(map(str,args)) + '\n')

class Drone:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.counter = 0

	def __str__(self):
		return str(self.x) + " " + str(self.y)

class Warehouse:
	def __init__(self, x, y, items):
		self.x = x
		self.y = y
		self.items = items

	def __str__(self):
		out = "  " + str(self.x) + " " + str(self.y) + " " + "items:"
		for item in self.items:
			out += " " + str(item)
		return out

class Order:
	def __init__(self, x, y, items):
		self.x = x
		self.y = y
		self.items = items

	def __str__(self):
		out = "  " + str(self.x) + " " + str(self.y) + " " +  "items:"
		for item in self.items:
			out += " " + str(item)
		return out


height, width, numDrones, numTurns, maxLoad = map(int, sys.stdin.readline().split())
numProductsTypes = int(sys.stdin.readline())

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


print_err("-----------INPUT----------")
print_err("H:", height, "W:", width)
print_err("Drones:", numDrones, "Turns:", numTurns, "Max load:", maxLoad)


print_err("Product types:", productTypes)

print_err("Warehouses:")
for warehouse in warehouses:
	print_err(warehouse)

print_err("Orders:")
for order in orders:
	print_err(order)

print_err("--------------------------\n")

# Init drones
drones = [Drone(0,0) for _ in range(numDrones)]


def findImminentDrone():
	return min(drones, key = lambda drone: drone.counter)
