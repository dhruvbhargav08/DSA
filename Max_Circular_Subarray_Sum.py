# This is from Geeks for Geeks.Question link at last
# Given an array arr[] of N integers arranged in a circular fashion.
# Your task is to find the maximum contiguous subarray sum
# User function Template for python3

# Complete this function
# Function to find maximum circular subarray sum.

def normal_sum(arr, n):
    temp_sum = 0
    max_sum = float('-inf')
    for i in range(n):
        temp_sum += arr[i]
        if temp_sum >= max_sum:
            max_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    return max_sum


def circularSubarraySum(arr, n):
    ##Your code here
    array_sum = sum(arr)
    temp_summ = 0
    max_normal_sum = normal_sum(arr, n)
    if max_normal_sum < 0:
        return max_normal_sum
    for i in range(n):
        arr[i] = -arr[i]
    min_normal_sum = normal_sum(arr, n)
    circular_sum = array_sum + min_normal_sum
    return max(max_normal_sum, circular_sum)


# {
# Driver Code Starts
# Initial Template for Python 3


import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr, n))

        T -= 1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/0
