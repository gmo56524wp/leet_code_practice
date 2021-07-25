class Solution:
    def longestMountain(self, arr):
        mountain = 0
        left_foot = 0
        while left_foot + 2 < len(arr):  # makesure the mountain exist
            right_foot = left_foot + 1
            if arr[left_foot] < arr[right_foot]:  # makesure the left_foot is valid
                while right_foot + 1 < len(arr) and arr[right_foot] < arr[right_foot+1]:
                    right_foot += 1
                if right_foot + 1 < len(arr) and arr[right_foot] > arr[right_foot+1]:  # make sure the peek exist
                    while right_foot + 1 < len(arr) and arr[right_foot] > arr[right_foot+1]:
                        right_foot += 1
                    mountain = max(mountain, right_foot-left_foot+1)
            left_foot = right_foot
        return mountain