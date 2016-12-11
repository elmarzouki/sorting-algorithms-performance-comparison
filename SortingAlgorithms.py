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
import random


class SortingAlgorithms:
    # Time Complexity of Bubble Sort:
    #  Best: O(n^2), Average: O(n^2), Worst: O(n^2)
    def BubbleSort(self, Numbers):
        for i in range(len(Numbers)):
            for j in range(len(Numbers)-1, i, -1):
                if (Numbers[j] < Numbers[j-1]):
                    Numbers[j], Numbers[j - 1] = Numbers[j - 1], Numbers[j]

    # Time Complexity of Selection Sort:
    #  Best: O(n^2), Average: O(n^2), Worst: O(n^2)
    def SelectionSort(self, Numbers):
        for i in range(len(Numbers)):
            Min = i
            for j in range(i+1, len(Numbers)):
                if Numbers[j] < Numbers[Min]:
                    Min = j
            Numbers[i], Numbers[Min] = Numbers[Min], Numbers[i]

    #  Time Complexity of Insertion Sort:
    #  Best: O(n), Average: O(n^2), Worst: O(n^2)
    def InsertionSort(self, Numbers):
        for i in range(len(Numbers)):
            Temp = Numbers[i]
            j = i
            while j > 0 and Temp < Numbers[j-1]:
                Numbers[j] = Numbers[j-1]
                j -= 1
                Numbers[j] = Temp

    # Time Complexity of Shell Sort:
    # Best: O(n), Average: O(n),Worst: O(n^2)
    def ShellSort(self, Numbers):
        Gap = len(Numbers)//2
        while Gap:
            for i in range(len(Numbers)):
                j = i
                Temp = Numbers[i]
                while j >= Gap and Numbers[j-Gap] > Temp:
                    Numbers[j] = Numbers[j-Gap]
                    j -= Gap
                Numbers[j] = Temp
            Gap = Gap // 2 if Gap // 2 else (0 if Gap == 1 else 1)

    # Time Complexity of Merge Sort: O(nlog(n))
    def MergeSort(self, Numbers):
        if len(Numbers) > 1:
            Center = len(Numbers)//2
            LeftHandSide = Numbers[:Center]
            RightHandSide = Numbers[Center:]
            self.MergeSort(LeftHandSide)
            self.MergeSort(RightHandSide)
            i = 0
            j = 0
            k = 0
            while i < len(LeftHandSide) and j < len(RightHandSide):
                if LeftHandSide[i] < RightHandSide[j]:
                    Numbers[k] = LeftHandSide[i]
                    i = i + 1
                else:
                    Numbers[k] = RightHandSide[j]
                    j = j + 1
                k = k + 1
            while i < len(LeftHandSide):
                Numbers[k] = LeftHandSide[i]
                i = i + 1
                k = k + 1
            while j < len(RightHandSide):
                Numbers[k] = RightHandSide[j]
                j = j + 1
                k = k + 1

    # Time Complexity of Quick Sort:
    #  Best: O(nlog(n)), Average: O(nlog(n)), Worst: O(n^2)
    def Partition(self, Values, LeftHandSide, RightHandSide):
        def partition(Values, LeftHandSide, RightHandSide, PivotIndex):
            pivot = Values[PivotIndex]
            Values[RightHandSide], Values[PivotIndex] = Values[PivotIndex], Values[RightHandSide]
            storeidx = LeftHandSide
            for idx in range(LeftHandSide, RightHandSide):
                if Values[idx] < pivot:
                    Values[idx], Values[storeidx] = Values[storeidx], Values[idx]
                    storeidx += 1
            Values[storeidx], Values[RightHandSide] = Values[RightHandSide], Values[storeidx]
            return storeidx
        if RightHandSide > LeftHandSide:
            PivotIndex = random.randint(LeftHandSide, RightHandSide)
            PivotIndex = partition(Values, LeftHandSide, RightHandSide, PivotIndex)
            self.Partition(Values, LeftHandSide, PivotIndex)
            self.Partition(Values, PivotIndex + 1, RightHandSide)
        return Values

    def QuickSort(self, Numbers):
        return self.Partition(Numbers, 0, len(Numbers) - 1)
