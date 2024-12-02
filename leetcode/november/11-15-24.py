# https://leetcode.com/problems/minimum-total-distance-traveled

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort by position
        robot.sort()
        factory.sort()

        # Flatten factory positions from capacity
        factory_positions = []
        for f in factory:
            for i in range(f[1]):
                factory_positions.append(f[0])

        total_robots = len(robot)
        total_factories = len(factory_positions)

        # Initialize DP with infinity
        dp = [[float('inf')] * (total_factories + 1) for _ in range(total_robots + 1)]


        # If no robots left, minimum distance is 0
        for j in range(total_factories + 1):
            dp[total_robots][j] = 0
        
        # Fill DP
        for i in range(total_robots - 1, -1, -1):
            for j in range(total_factories - 1, -1, -1):
                # Assign current robot to current factory
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]
                
                # Skip current factory for current robot
                skip = dp[i][j + 1]

                # Choose minimum of assigning or skipping
                dp[i][j] = min(assign, skip)
        
        # Minimum total diistance starting from first robot and first factory
        return dp[0][0]
      
      
# ------------------------------------------

# Recursive version (From editorial)

class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position
        robot.sort()
        factory.sort()

        # Flatten factory positions according to their capacities
        factory_positions = []
        for f in factory:
            for i in range(f[1]):
                factory_positions.append(f[0])

        # Recursively calculate minimum total distance
        return self._calculate_min_distance(0, 0, robot, factory_positions)

    def _calculate_min_distance(
        self, robot_idx, factory_idx, robot, factory_positions
    ):
        # All robots assigned
        if robot_idx == len(robot):
            return 0
        # No factories left to assign
        if factory_idx == len(factory_positions):
            return 1e12

        # Option 1: Assign current robot to current factory
        assign = abs(
            robot[robot_idx] - factory_positions[factory_idx]
        ) + self._calculate_min_distance(
            robot_idx + 1, factory_idx + 1, robot, factory_positions
        )

        # Option 2: Skip current factory for the current robot
        skip = self._calculate_min_distance(
            robot_idx, factory_idx + 1, robot, factory_positions
        )

        # Take the option with the minimum distance
        return min(assign, skip)