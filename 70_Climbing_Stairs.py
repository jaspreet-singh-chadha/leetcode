class Solution:
    results_map = {}

    def climbStairs(self, n: int) -> int:
        return self.calculate_ways_to_climb_stairs(n, self.results_map)

    # We try to find ways till -1 and -2 stairs as we assume that these are the only two unique ways in which the
    # final jump can end
    # The -1 ways will always end in 1 step jump and -2 ways will always end in 2 stairs jump
    # Hence all ways should be included by using this approach
    def calculate_ways_to_climb_stairs(self, n: int, results_map) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Use Dynamic Programming (DP) through memoization
        if (n - 1) in results_map.keys():
            ways_till_last_stair = results_map[n - 1]
        else:
            ways_till_last_stair = self.climbStairs(n - 1)
            results_map[n - 1] = ways_till_last_stair

        if (n - 2) in results_map.keys():
            ways_till_second_last_stair = results_map[n - 2]
        else:
            ways_till_second_last_stair = self.climbStairs(n - 2)
            results_map[n - 2] = ways_till_second_last_stair

        return ways_till_last_stair + ways_till_second_last_stair


if __name__ == '__main__':
    print(Solution().climbStairs(10))
