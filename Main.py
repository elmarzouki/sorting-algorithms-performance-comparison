"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this project is a performance comparison among bunch of sorting algorithms
it computes the time used in each algorithm to sort list of: Sorted numbers
and Unsorted numbers
input: the size of the numbers list
output: the time each algorithm take to sort the numbers in ms
"""
import Manage

Manage = Manage.Manage()

print("Number size must be more than 5000 to notice the difference among the algorithms! \n"
      "Output is measured in seconds")
while True:
    Manage.FillRandom(int(input("Numbers size: ")))
    Time = Manage.Sort()
    for Type, TypeValue in Time.items():
        print("--------------------\n"
              "-", Type, "-\n"
              "--------------------")
        for Sort, SortValue in TypeValue.items():
            print(Sort, " : ", SortValue)
