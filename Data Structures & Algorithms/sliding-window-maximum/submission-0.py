class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        if k <= 0:
            return []  # Or raise an exception, depending on desired behavior

        if k > len(nums):
            return [] # Or return [max(nums)] if the entire array is the window

        result = []
        dq = deque()  # Use a deque to store indices of potential maximums

        for i in range(len(nums)):
            # Remove elements from the front of the deque that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove elements from the back of the deque that are smaller than the current element
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)  # Add the current element's index to the deque

            # The maximum element in the current window is always at the front of the deque
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        
        