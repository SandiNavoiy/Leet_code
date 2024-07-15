from bisect import bisect_left


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        arr =sorted(nums)
        answer = []
        for num in nums:
            i = bisect_left(arr,num)
            answer.append(i)
            del arr[i]
        return answer


nums = [5,2,6,1]
s = Solution()
print(s.countSmaller(nums))