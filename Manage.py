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
import random, time
import SortingAlgorithms


Sort = SortingAlgorithms.SortingAlgorithms()
class Manage:
    # fill Numbers.txt with random numbers
    def FillRandom(self, Size):
        open("data/UnsortedNumbers.txt", 'w').close()
        with open("data/UnsortedNumbers.txt", "w") as handle:
            for i in range(Size):
                print(random.randint(1, 10000), file=handle)

    def ReadNumbers(self, File):
        Numbers = []
        with open("data/" + File) as Lines:
            for Line in Lines:
                Numbers.append(int(Line))
        return Numbers

    # calculate the execution time of function
    def ExecutionTime(self, fun, *args):
        StartTime = int(round(time.time() * 1000))
        fun(args[0])
        EndTime = int(round(time.time() * 1000))
        return (EndTime - StartTime)

    # apply the sorting algorithms on the random numbers we just generated in Numbers.txt
    def Sort(self):
        Numbers = []
        SortingTimes = {"UnsortedNumbers": {"BubbleSort": 0, "SelectionSort": 0, "InsertionSort": 0,
                        "ShellSort": 0, "MergeSort": 0, "QuickSort": 0},
                        "SortedNumbers": {"BubbleSort": 0, "SelectionSort": 0, "InsertionSort": 0,
                        "ShellSort": 0, "MergeSort": 0, "QuickSort": 0}}
        Numbers = self.ReadNumbers("UnsortedNumbers.txt")
        SortingTimes['UnsortedNumbers']['BubbleSort'] = str(self.ExecutionTime(Sort.BubbleSort, Numbers)) + ' ms'
        Numbers = self.ReadNumbers("UnsortedNumbers.txt")
        SortingTimes['UnsortedNumbers']['SelectionSort'] = str(self.ExecutionTime(Sort.SelectionSort, Numbers)) + ' ms'
        Numbers = self.ReadNumbers("UnsortedNumbers.txt")
        SortingTimes['UnsortedNumbers']['InsertionSort'] = str(self.ExecutionTime(Sort.InsertionSort, Numbers)) + ' ms'
        Numbers = self.ReadNumbers("UnsortedNumbers.txt")
        SortingTimes['UnsortedNumbers']['ShellSort'] = str(self.ExecutionTime(Sort.ShellSort, Numbers)) + ' ms'
        Numbers = self.ReadNumbers("UnsortedNumbers.txt")
        SortingTimes['UnsortedNumbers']['MergeSort'] = str(self.ExecutionTime(Sort.MergeSort, Numbers)) + ' ms'
        Numbers = self.ReadNumbers("UnsortedNumbers.txt")
        SortingTimes['UnsortedNumbers']['QuickSort'] = str(self.ExecutionTime(Sort.QuickSort, Numbers)) + ' ms'
        SortingTimes['SortedNumbers']['BubbleSort'] = str(self.ExecutionTime(Sort.BubbleSort, Numbers)) + ' ms'
        SortingTimes['SortedNumbers']['SelectionSort'] = str(self.ExecutionTime(Sort.SelectionSort, Numbers)) + ' ms'
        SortingTimes['SortedNumbers']['InsertionSort'] = str(self.ExecutionTime(Sort.InsertionSort, Numbers)) + ' ms'
        SortingTimes['SortedNumbers']['ShellSort'] = str(self.ExecutionTime(Sort.ShellSort, Numbers)) + ' ms'
        SortingTimes['SortedNumbers']['MergeSort'] = str(self.ExecutionTime(Sort.MergeSort, Numbers)) + ' ms'
        SortingTimes['SortedNumbers']['QuickSort'] = str(self.ExecutionTime(Sort.QuickSort, Numbers)) + ' ms'
        return SortingTimes