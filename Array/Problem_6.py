# Alice and Bob are playing a game that consists of n levels. Some of the levels in the game are impossible to clear while others can always be cleared. In particular, if possible[i] == 0, then the ith level is impossible to clear for both the players. A player gains 1 point on clearing a level and loses 1 point if the player fails to clear it.

# At the start of the game, Alice will play some levels in the given order starting from the 0th level, after which Bob will play for the rest of the levels.

# Alice wants to know the minimum number of levels she should play to gain more points than Bob, if both players play optimally to maximize their points.

# Return the minimum number of levels Alice should play to gain more points. If this is not possible, return -1.

# Note that each player must play at least 1 level.

 

# Example 1:

# Input: possible = [1,0,1,0]

# Output: 1

# Explanation:

# Let's look at all the levels that Alice can play up to:

# If Alice plays only level 0 and Bob plays the rest of the levels, Alice has 1 point, while Bob has -1 + 1 - 1 = -1 point.
# If Alice plays till level 1 and Bob plays the rest of the levels, Alice has 1 - 1 = 0 points, while Bob has 1 - 1 = 0 points.
# If Alice plays till level 2 and Bob plays the rest of the levels, Alice has 1 - 1 + 1 = 1 point, while Bob has -1 point.
# Alice must play a minimum of 1 level to gain more points.


# Approach: Convert all the levels in score and then take alice score as 0 and and bob score as total
# then traverse for each possitive point - increase alice score and decrease bob score. And then compare


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        p = [-1 if x == 0 else 1 for x in possible]

        left, right = 0, sum(p)
        for i in range(n-1):
            left += p[i]
            right -= p[i]
            if left > right:
                return i + 1
        return -1