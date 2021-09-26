import asn1tools as asn
import json

from mymodule import (euclid,
          inverse,
          karatsuba,
          mod_add,
          mod_multiply,
          mod_subtract,
          reduce,
          datatypes,
          profiler)


# import subtract

### AfS software assignment 1 - example code ###

# set file names
base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'input.ops'
#exs_loc = base_location + 'test_exercises_students_answers'
ans_loc = base_location + 'output.ops'
#ans_loc = base_location + 'test_exercises_students_answers'

# ###### Creating an exercise list file ######
#
# How to create an exercise JSON file containing one addition exercise
#exercises = {'exercises' : []}                                     # initialize empty exercise list
#ex = {"multiply": {"radix": 10, "x": "12", "y": "12", "answer": "24"}} # create add exercise
#ex1 = {"add": {"radix": 10, "x": "-40", "y": "20", "answer": "-20"}} # create add exercise
#ex2 = {"add": {"radix": 10, "x": "40", "y": "-20", "answer": "20"}} # create add exercise
#ex3 = {"add": {"radix": 10, "x": "-40", "y": "-20", "answer": "-60"}} # create add exercise
#
#ex4 = {"subtract": {"radix": 10, "x": "40", "y": "20", "answer": "-30"}} # create add exercise
#ex5 = {"subtract": {"radix": 10, "x": "-40", "y": "20", "answer": "50"}} # create add exercise
#ex6 = {"subtract": {"radix": 10, "x": "40", "y": "-20", "answer": "-30"}} # create add exercise
#ex7 = {"subtract": {"radix": 10, "x": "-40", "y": "-20", "answer": "50"}} # create add exercise
#exercises['exercises'].append(ex)                                  # add exercise to list
#exercises['exercises'].append(ex1)
#exercises['exercises'].append(ex2)
#exercises['exercises'].append(ex3)
#
#exercises['exercises'].append(ex4)                                  # add exercise to list
#exercises['exercises'].append(ex5)
#exercises['exercises'].append(ex6)
#exercises['exercises'].append(ex7)

# Encode exercise list and print to file
#my_file = open(exs_loc, 'wb+')                                     # write to binary file
#my_file.write(json.dumps(exercises).encode())                      # add encoded exercise list
#my_file.close()

###### Using an exercise list file ######

# Compile specification
spec = asn.compile_files(ops_loc, codec="jer")

# Read exercise list
exercise_file = open(exs_loc, 'rb')  # open binary file
file_data = exercise_file.read()  # read byte array
my_exercises = spec.decode('Exercises', file_data)  # decode after specification
exercise_file.close()

# Create answer JSON
my_answers = {'exercises': []}

# Create the profiler that is used to count operations
ops_counter = profiler.OperationStatistics.getInstance()

X_OPS = [ 'add', 'mod-add', 'subtract', 'mod-subtract', 'multiply',
        'mod-multiply', 'karatsuba', 'reduce', 'euclid', 'inverse' ]
Y_OPS = [ 'add', 'mod-add', 'subtract', 'mod-subtract', 'multiply',
        'mod-multiply', 'karatsuba' ]
M_OPS = [ 'mod-add', 'mod-subtract', 'mod-multiply', 'reduce', 'inverse' ]
# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0]  # get operation type
    params = exercise[1]  # get parameters
    radix = params['radix']

    if operation in X_OPS:
        x = datatypes.LargeInteger(params['x'], radix=radix)

    if operation in Y_OPS:
        y = datatypes.LargeInteger(params['y'], radix=radix)

    if operation in M_OPS:
        m = datatypes.LargeInteger(params['m'], radix=radix)

    answer = None
    if operation == 'add':
        answer = x + y
    elif operation == 'mod-add':
        answer = mod_add.mod_add(x, y, m)
    elif operation == 'subtract':
        answer = x - y
    elif operation == 'mod-subtract':
        answer = mod_subtract.mod_subtract(x, y, m)
    elif operation == 'multiply':
        answer = x * y
    elif operation == 'mod-multiply':
        answer = mod_multiply.mod_multiply(x, y, m)
    elif operation == 'karatsuba':
        answer = karatsuba.karatsuba_recursive(x, y, radix)
    elif operation == 'reduce':
        answer = reduce.reduce(x, m)
    elif operation == 'euclid':
        ans_d, ans_a, ans_b = euclid.euclid(x, y)
    elif operation == 'inverse':
        answer = inverse.inverse(x, m)
    else:
        print('Unknown operation:', operation)

    calc_params = params
    try:
        if operation == 'euclid':
            calc_params['answ-d'] = str(ans_d)
            calc_params['answ-a'] = str(ans_a)
            calc_params['answ-b'] = str(ans_b)
        else:
            calc_params['answer'] = str(answer)
    except ValueError as e:
        print("Could not obtain answer for the question below:",str(e))
        print(params)
        continue

    if operation == 'karatsuba' or operation == 'multiply':
        stats = ops_counter.statistics

        try:
            mul_count = stats['Multiply']
        except KeyError:
            mul_count = 0

        try:
            add_count = stats['Add']
        except KeyError:
            add_count = 0

        calc_params['count-mul'] = mul_count
        calc_params['count-add'] = add_count

    # Save answer
    my_answers['exercises'].append({operation: calc_params})

    print("Operation statistics for:", operation)
    ops_counter.show_statistics()
    # Reset the counters
    ops_counter.reset_statistics()

###### Creating an answers list file ######

# Save exercises with answers to file
my_file = open(ans_loc, 'wb+')  # write to binary file
my_file.write(json.dumps(my_answers).encode())  # add encoded exercise list
my_file.close()
