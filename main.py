# Created by breadA#3012

# Imports
import random
import os
import test.display

# For Linux
# os.system('clear')
print("Lemme gather some basic information about you:")

# Inputs
# Make sure these are lowercase
YES = "yes"
NO = "no"

# Main Outputs

name = input("What is you name? ")
if name == "breadA" or name == "Dhairy":
    print("Hello fellow owner")

a_student = input("Are you a student? ")
if a_student.strip().lower() == YES:
    print("OKAY!")
else:
    print("mm.. okay.. nice")