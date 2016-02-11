import sys

class Drone:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.counter = 0
		self.currentPayload = 0

	def addPayload(self, load):
		self.currentPayload += load

	def payloadLeft(self):
		return maxLoad - self.currentPayload

	def moveTo(self, x, y):
		self.x = x
		self.y = y

	def load(self, item):
		pass

	def deliver(self):
		pass

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
		self.currentItem = 0

	def __str__(self):
		out = "  " + str(self.x) + " " + str(self.y) + " " +  "items:"
		for item in self.items:
			out += " " + str(item)
		return out


	def getNextItem(self):
		if self.currentItem == len(self.items):
			return None
		return self.items[self.currentItem]

	def removeNextItem(self):
		self.currentItem += 1

	def hasItems(self):
		return self.currentItem < len(self.items)

def findWarehouse(typeName):
	for warehouse in warehouses:
		if warehouse.items[typeName] > 0:
			warehouse.items[typeName] -= 1
			return [warehouse.x, warehouse.y]

def findImminentDrone():
	return min(drones, key = lambda drone: drone.counter)


def processOrders(orders):
	for order in orders:
	    drone = findImminentDrone()
	    while order.hasItems() :
			item = order.getNextItem()
			while drone.payloadLeft() >= productTypes[item]:
				order.removeNextItem()
				warehouse = findWarehouse(item)
				drone.moveTo(warehouse[0], warehouse[1])
				drone.load(item)
				item = order.getNextItem()
				if item == None:
					break
			drone.moveTo(order.x, order.y)
			drone.deliver()




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


print("-----------INPUT----------")
print("H:", height, "W:", width)
print("Drones:", numDrones, "Turns:", numTurns, "Max load:", maxLoad)


print("Product types:", productTypes)

print("Warehouses:")
for warehouse in warehouses:
	print(warehouse)

print("Orders:")
for order in orders:
	print(order)

print("--------------------------\n")

# Init drones
drones = [Drone(0,0) for _ in range(numDrones)]

processOrders(orders)

