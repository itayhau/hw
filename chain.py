
######### Implement chain of responsiblity pattern into this code:

import random
import statistics

class NumberArray:
   def __init__(self, size):
       # Initialize array with random numbers
       self._numbers = [random.randint(1, 100) for _ in range(size)]
       self._average = None
       self._std_deviation = None
   
   # Getters
   @property
   def numbers(self):
       return self._numbers
   
   @property
   def average(self):
       return self._average
   
   @property
   def std_deviation(self):
       return self._std_deviation
   
   # Setters
   @numbers.setter
   def numbers(self, new_numbers):
       self._numbers = new_numbers
   
   @average.setter
   def average(self, value):
       self._average = value
   
   @std_deviation.setter
   def std_deviation(self, value):
       self._std_deviation = value


def main():
   # Create the number array
   size = int(input("Enter the size of the array: "))
   number_array = NumberArray(size)
   
   print(f"Original array: {number_array.numbers}")
   
   # Sort the array?
   sort_choice = input("Sort the array? (yes/no): ").strip().lower()
   if sort_choice == "yes":
       sorted_numbers = sorted(number_array.numbers)
       number_array.numbers = sorted_numbers
       print(f"Sorted array: {number_array.numbers}")
   
   # Multiply array elements by a number?
   multiply_choice = input("Multiply array elements by a number? (yes/no): ").strip().lower()
   if multiply_choice == "yes":
       factor = int(input("Enter the multiplication factor: "))
       multiplied_numbers = [num * factor for num in number_array.numbers]
       number_array.numbers = multiplied_numbers
       print(f"Array after multiplication: {number_array.numbers}")
   
   # Calculate average?
   average_choice = input("Calculate average? (yes/no): ").strip().lower()
   if average_choice == "yes":
       calculated_average = sum(number_array.numbers) / len(number_array.numbers)
       number_array.average = calculated_average
       print(f"Average of numbers: {number_array.average}")
   
   # Calculate standard deviation?
   std_choice = input("Calculate standard deviation? (yes/no): ").strip().lower()
   if std_choice == "yes":
       if len(number_array.numbers) > 1:
           calculated_std = statistics.stdev(number_array.numbers)
           number_array.std_deviation = calculated_std
           print(f"Standard deviation: {number_array.std_deviation}")
       else:
           print("Cannot calculate standard deviation with less than 2 numbers")
   
   print(f"Final array: {number_array.numbers}")
   
   # Display stored statistics
   print("\nStored Statistics:")
   if number_array.average is not None:
       print(f"Average: {number_array.average}")
   if number_array.std_deviation is not None:
       print(f"Standard Deviation: {number_array.std_deviation}")


if __name__ == "__main__":
   main()
