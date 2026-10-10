# Problem2: Calculate Tax (https://leetcode.com/problems/calculate-amount-paid-in-taxes/)
# Time Complexity: O(n), where n is the number of brackets. We use each bracket at most once and the work inside the loop is constant.
# Space Complexity: O(1).We only use a few number variables. No extra list or structure grows with input.
# Approach:
# Think of each bracket as a bucket. Its size is (upper - lower) and it has a tax rate.
# Pour the income into the buckets in order. For each bucket, tax only the part of income that fits in it, add that tax to the total, and remove that part from income.
#   Stop when no income is left.

class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0.0       # total tax so far, float because the answer can have decimals
        lower = 0       # where the current bucket starts, the first one starts at 0
        index = 0       # which bracket we are on

        while income > 0:               # keep going while there is untaxed income
            br = brackets[index]        # pick the current bracket, like [3, 50]
            index += 1                  # move to the next bracket for the next loop

            upper = br[0]               # where this bucket ends
            percent = br[1]             # tax rate of this bucket, in percent

            # bucket size is (upper - lower), income is the money we still hold
            # min makes sure we never tax more money than we have left
            taxable = min(income, upper - lower)

            # use / (not //) so 50 becomes 0.5 and we keep the decimal part
            tax += taxable * (percent / 100.0)

            lower = upper               # next bucket starts where this one ended
            income -= taxable           # this money is taxed, remove it from income

        return tax                      # total tax for the full income