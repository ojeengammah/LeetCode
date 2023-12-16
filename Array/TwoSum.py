class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of numbers we've seen so far
        num_indices = {}

        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_indices:
                # Return the indices of the two numbers that add up to the target
                return [num_indices[complement], i]

            # If the complement is not in the dictionary, add the current number and its index
            num_indices[num] = i

        # If no solution is found, return an empty list or handle it as needed
        return []
