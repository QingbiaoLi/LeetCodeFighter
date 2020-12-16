class Solution:
    def twoSum(self, nums, target):

        rev_table = dict()

        for i in range(len(nums)):
            second_addend = target - nums[i]
            print("second_addend:{}".format(second_addend))

            if second_addend in rev_table:

                print("second_addend in table \n return:{}".format([rev_table[second_addend], i]))
                return [rev_table[second_addend], i]
            else:

                rev_table[nums[i]] = i
                print("second_addend not in table \n  i-{}\t rever_table:{}".format(i, rev_table))


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 9
    # assert (Solution().twoSum(nums, target) == [0, 1])
    nums = [3, 2, 4]
    target = 6
    assert (Solution().twoSum(nums, target) == [1, 2])