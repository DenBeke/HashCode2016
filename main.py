import sys
import math
import os

commandList = []

def print_err(*args):
	sys.stderr.write(' '.join(map(str,args)) + '\n')

def euclid(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)


class Drone:
	def __init__(self, x, y, ID, numProductTypes):
		self.x = x
		self.y = y
		self.ID = ID
		self.counter = 0
		self.currentPayload = 0
		self.numProductTypes = numProductTypes
		self.items = [0 for _ in range(numProductTypes)]

	def addPayload(self, load):
		self.currentPayload += load

	def payloadLeft(self):
		return maxLoad - self.currentPayload

	def moveTo(self, x, y):
		self.counter += math.ceil(euclid(x, y, self.x, self.y))
		if self.counter >= numTurns:
			exit(0)
		self.x = x
		self.y = y


	def load(self, warehouseNo, typeName, itemNo, payload):
		self.counter += 1
		if self.counter >= numTurns:
			exit(0)
		self.addPayload(payload)
		self.items[typeName] += itemNo

		
		print(str(self.ID) + " L " + str(warehouseNo) + " " + str(typeName) + " " + str(itemNo))

	def deliver(self, orderNo):
		self.counter += 1
		if self.counter >= numTurns:
			exit(0)
		for i in range(len(self.items)):
			if self.items[i] > 0:
				print_err("output")
				print(str(self.ID) + " D " + str(orderNo) + " " + str(i) + " " + str(self.items[i]))
		self.currentPayload = 0
		self.items = [0 for _ in range(self.numProductTypes)]

	def __str__(self):
		return str(self.x) + " " + str(self.y)

class Warehouse:
	def __init__(self, x, y, items, ID):
		self.x = x
		self.y = y
		self.items = items
		self.ID = ID

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
			return warehouse

def findImminentDrone():
	return min(drones, key = lambda drone: drone.counter)


def processOrders(orders):
	for i in range(len(orders)):
		order = orders[i]
		drone = findImminentDrone()
		while order.hasItems() :
			item = order.getNextItem()
			itemNo = 0
			while drone.payloadLeft() >= productTypes[item]:
				print_err("payload")
				order.removeNextItem()
				warehouse = findWarehouse(item)
				drone.moveTo(warehouse.x, warehouse.y)
				drone.load(warehouse.ID, item, 1, productTypes[item])
				item = order.getNextItem()
				itemNo += 1
				if item == None:
					print_err("break")
					break
			drone.moveTo(order.x, order.y)
			drone.deliver(i)




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
	warehouses.append(Warehouse(x, y, items, i))


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
drones = [Drone(0,0, i, numProductsTypes) for i in range(numDrones)]

processOrders(orders)

