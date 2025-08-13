# accounts = [[1, 5], [7, 3], [3, 5]]
# max_wealth = max(sum(customer) for customer in accounts)
# print(max_wealth)  # Output: 10


class Solution(object):
    def maximumWealth(self, accounts):
        maximum_wealth = 0
        for customer in accounts:
            total = 0
            for money in customer:
                total += money

            if total > maximum_wealth :
                maximum_wealth = total
        return maximum_wealth

sol = Solution()
print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))  # Output: 10
