class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lt, rt = i+1, len(nums)-1
            while lt<rt:
                sum1 = nums[i]+nums[lt]+nums[rt]
                if sum1 < 0:
                    lt += 1
                elif sum > 0:
                    rt -= 1
                else:
                    answer.append([nums[i], nums[lt], nums[rt]])

                    while lt < rt and nums[lt] == nums[lt+1]:
                        lt += 1
                    while lt < rt and nums[rt] == nums[rt-1]:
                        rt -= 1
                    lt += 1
                    rt -= 1

        return answer

# brute(time out)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         nums.sort()
#
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)-1):
#                 if j > i+1 and nums[j] == nums[j - 1]:
#                     continue
#                 for k in range(j+1, len(nums)):
#                     if k > j + 1 and nums[k] == nums[k - 1]:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         answer.append((nums[i], nums[j], nums[k]))
#
#         return answer