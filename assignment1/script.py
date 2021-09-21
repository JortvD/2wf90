import asn1tools as asn
import json

import add
import euclid
import inverse
import karatsuba
import mod_add
import mod_multiply
import mod_subtract
import multiply
import reduce
import subtract

### AfS software assignment 1 - example code ###

# set file names
base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'test_exercises_students_answers'
ans_loc = base_location + 'my_answers'

# ###### Creating an exercise list file ######
#
# # How to create an exercise JSON file containing one addition exercise
# exercises = {'exercises' : []}                                     # initialize empty exercise list
# ex = {"add": {"radix": 16, "x": "82a4d3f8bfab54bb3011", "y": "cb95aa820d14888e48c3", "answer": ""}} # create add exercise
# exercises['exercises'].append(ex)                                  # add exercise to list
#
# # Encode exercise list and print to file
# my_file = open(exs_loc, 'wb+')                                     # write to binary file
# my_file.write(json.dumps(exercises).encode())                      # add encoded exercise list
# my_file.close()

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

    if operation == 'add':
        calc_params = add.calc(params)

    # if operation == 'mod-add':
    #     params = mod_add.calc(params);
    #
    # if operation == 'subtract':
    #     params = subtract.subtract();
    #
    # if operation == 'mod-subtract':
    #     params = mod_subtract.modSubtract();
    #
    # if operation == 'multiply':
    #     params = multiply.multiply();
    #
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
    print(params['answer'] + "=" + calc_params['answer'] + "?" + str(calc_params['answer'] is params['answer']))
    my_answers['exercises'].append({operation: params})

###### Creating an answers list file ######

# Save exercises with answers to file
my_file = open(ans_loc, 'wb+')  # write to binary file
my_file.write(json.dumps(my_answers).encode())  # add encoded exercise list
my_file.close()