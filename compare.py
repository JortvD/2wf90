from mymodule import (multiply,
	      karatsuba,
          datatypes,
          profiler)
import random

ITERATIONS = 50
LENGTH = 500
BASE = 10

operations = {'add_karatsuba': 0, 'mul_karatsuba': 0, 'add_multiply': 0, 'mul_multiply': 0}

ops_counter = profiler.OperationStatistics.getInstance()

for i in range(0, ITERATIONS):
	print('i: ' + str(i))

	x = [1] if random.choice([True, False]) else [0]
	y = [1] if random.choice([True, False]) else [0]

	for n in range(0, LENGTH):
		x += [random.randint(0, BASE-1)]
		y += [random.randint(0, BASE-1)]

	xl = datatypes.LargeInteger(x, BASE)
	yl = datatypes.LargeInteger(y, BASE)

	karatsuba.karatsuba_recursive(xl, yl, BASE)
	stats = ops_counter.statistics

	operations['add_karatsuba'] += stats['Add']
	operations['mul_karatsuba'] += stats['Multiply']

	ops_counter.reset_statistics()

	multiply.multiply(xl, yl)
	stats = ops_counter.statistics

	operations['add_multiply'] += stats['Add']
	operations['mul_multiply'] += stats['Multiply']

	ops_counter.reset_statistics()

print('The average operations were:')
print('karatsuba - add: ' + str(operations['add_karatsuba']/ITERATIONS) + ', multiply: ' + str(operations['mul_karatsuba']/ITERATIONS))
print('multiply - add: ' + str(operations['add_multiply']/ITERATIONS) + ', multiply: ' + str(operations['mul_multiply']/ITERATIONS))