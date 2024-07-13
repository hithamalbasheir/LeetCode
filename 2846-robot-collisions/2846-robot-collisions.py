class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robot_to_health = { i : healths[i] for i in range(len(healths))}
        heap_phd = []
        for i in range(len(positions)):
            heapq.heappush(heap_phd, (positions[i], i))
        
        stack = []
        while heap_phd:
            p, robot_ind = heapq.heappop(heap_phd)
            if directions[robot_ind] == 'L':
                opp_dir = 'R'
                while stack and robot_to_health[robot_ind] > 0 and directions[stack[-1]] == opp_dir:
                    if robot_to_health[stack[-1]] > robot_to_health[robot_ind]:
                        robot_to_health[robot_ind] = 0
                        robot_to_health[stack[-1]]-=1
                        if robot_to_health[stack[-1]] <= 0:
                            stack.pop()
                    elif robot_to_health[stack[-1]] == robot_to_health[robot_ind]:
                        robot_to_health[robot_ind] = 0
                        robot_to_health[stack[-1]] = 0
                        stack.pop()
                    else:
                        robot_to_health[robot_ind]-=1
                        robot_to_health[stack[-1]] = 0
                        stack.pop()
            
            if robot_to_health[robot_ind] > 0:
                stack.append(robot_ind)
        
        output = []
        for ind in range(len(positions)):
            if robot_to_health[ind] > 0:
                output.append(robot_to_health[ind])
        
        return output