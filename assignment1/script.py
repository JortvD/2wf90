import asn1tools as asn
import json

import euclid
import inverse
import karatsuba
import mod_add
import mod_multiply
import mod_subtract
import reduce
import datatypes
import sys
# import subtract

### AfS software assignment 1 - example code ###

# set file names
base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'my_exercises'
#exs_loc = base_location + 'test_exercises_students_answers'
ans_loc = base_location + 'my_answers'
#ans_loc = base_location + 'test_exercises_students_answers'

# ###### Creating an exercise list file ######
#
# How to create an exercise JSON file containing one addition exercise
exercises = {'exercises' : []}                                     # initialize empty exercise list
ex = {"multiply": {"radix": 10, "x": "12", "y": "12", "answer": "24"}} # create add exercise
ex1 = {"add": {"radix": 10, "x": "-40", "y": "20", "answer": "-20"}} # create add exercise
ex2 = {"add": {"radix": 10, "x": "40", "y": "-20", "answer": "20"}} # create add exercise
ex3 = {"add": {"radix": 10, "x": "-40", "y": "-20", "answer": "-60"}} # create add exercise

ex4 = {"subtract": {"radix": 10, "x": "40", "y": "20", "answer": "-30"}} # create add exercise
ex5 = {"subtract": {"radix": 10, "x": "-40", "y": "20", "answer": "50"}} # create add exercise
ex6 = {"subtract": {"radix": 10, "x": "40", "y": "-20", "answer": "-30"}} # create add exercise
ex7 = {"subtract": {"radix": 10, "x": "-40", "y": "-20", "answer": "50"}} # create add exercise
exercises['exercises'].append(ex)                                  # add exercise to list
exercises['exercises'].append(ex1)
exercises['exercises'].append(ex2)
exercises['exercises'].append(ex3)

exercises['exercises'].append(ex4)                                  # add exercise to list
exercises['exercises'].append(ex5)
exercises['exercises'].append(ex6)
exercises['exercises'].append(ex7)

# Encode exercise list and print to file
my_file = open(exs_loc, 'wb+')                                     # write to binary file
my_file.write(json.dumps(exercises).encode())                      # add encoded exercise list
my_file.close()

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

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0]  # get operation type
    params = exercise[1]  # get parameters
    radix = params['radix']
    x = datatypes.LargeInteger(params['x'], radix=radix)
    y = datatypes.LargeInteger(params['y'], radix=radix)
    answer = None

    if operation == 'add':
        answer = x + y

    # if operation == 'mod-add':
    #     params = mod_add.calc(params);
    #
    if operation == 'subtract':
        answer = x - y
    #
    # if operation == 'mod-subtract':
    #     params = mod_subtract.modSubtract();
    #
    if operation == 'multiply':
        answer = x * y

    # if operation == 'mod-multiply':
    #     params = mod_multiply.modMultiply();
    #
    # if operation == 'karatsuba':
    #     params = karatsuba.calc(params);
    #
    # if operation == 'reduce':
    #     params = reduce.reduce();
    #
    # if operation == 'euclid':
    #     params = euclid.euclid();
    #
    # if operation == 'inverse':
    #     params = inverse.inverse();

    # Save answer
    #print(params['x'],params['y'])
    #print(operation+":"+params['answer'] + "=" + calc_params['answer'] + "?" + str(calc_params['answer'] == params['answer']))
    #if calc_params['answer'] != params['answer']:
    #    sys.exit(1)
    print(str(answer))
    # TODO
    #my_answers['exercises'].append({operation: calc_params})

###### Creating an answers list file ######

# Save exercises with answers to file
my_file = open(ans_loc, 'wb+')  # write to binary file
my_file.write(json.dumps(my_answers).encode())  # add encoded exercise list
my_file.close()
