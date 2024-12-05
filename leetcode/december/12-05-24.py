# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        visited = set()
        queue = []

        queue.append(start)

        while queue:
            current = queue.pop(0)

            if current == target:
                return True
            
            for position in range(1, len(current)):
                if current[position] == "L" and current[position - 1] == "_":
                    current = list(current)
                    current[position], current[position - 1] = current[position - 1], current[position]
                    current = "".join(current)

                    if current not in visited:
                        queue.append(current)
                        visited.add(current)
                    
                    current = list(current)
                    current[position], current[position - 1] = current[position - 1], current[position],
                    current = "".join(current)
                
                if position < len(current) - 1 and current[position] == "R" and current[position + 1] == "_":
                    current = list(current)
                    current[position], current[position + 1] = current[position + 1], current[position]
                    current = "".join(current)

                    if current not in visited:
                        queue.append(current)
                        visited.add(current)
                    
                    current = list(current)
                    current[position], current[position + 1] = current[position + 1], current[position],
                    current = "".join(current)
        return False
      
      
      
# CHAT GPT SOLUTION:

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Step 1: Check if removing "_" makes the strings identical
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        # Step 2: Validate positions of "L" and "R"
        j = 0  # Pointer for target
        for i, char in enumerate(start):
            if char == "_":
                continue
            # Move j to the next non-"_" character in target
            while target[j] == "_":
                j += 1
            # Check relative positions
            if (char == "L" and i < j) or (char == "R" and i > j):
                return False
            j += 1
        
        return True
