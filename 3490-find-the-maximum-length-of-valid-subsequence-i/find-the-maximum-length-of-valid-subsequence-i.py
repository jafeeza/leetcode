class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Constrained 0-1 Knapsack problem.
        # Each element in nums can be chosen or not.
        # Let P(i) be the longest valid sequence length ending with nums[i], with even pairs; Q(i) be the longest valid sequence length ending with nums[i], with odd pairs.
        # P(i) = 1 + max(P(j) for (nums[j] + nums[i]) % 2 == 0)
        # Q(i) = 1 + max(Q(j) for (nums[j] + nums[i]) % 2 == 1)
        # The final answer is max(max(P(i), Q(i))).
        # Base case:
        # P(-1) = 0
        # Q(-1) = 0
        odd_prev_p = 0
        odd_prev_q = 0
        even_prev_p = 0
        even_prev_q = 0
        for num in nums:
            if num % 2 == 1:
                odd_prev_p += 1
                odd_prev_q = 1 + even_prev_q
            else:
                even_prev_p += 1
                even_prev_q = 1 + odd_prev_q
        return max(odd_prev_p, odd_prev_q, even_prev_p, even_prev_q)