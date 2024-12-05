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
                
                if position < len(current) - 1 and current[position] == "R" and current[position - 1] == "_":
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