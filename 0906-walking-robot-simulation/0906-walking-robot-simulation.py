class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = 0+0j
        d = 0+1j
        obstacles = set(x+y*1j for x, y in obstacles)
        farthest = 0

        for command in commands:
            match(command):
                case -2:
                    d *= 1j
                case -1:
                    d *= -1j
                case _:
                    for _ in range(command):
                        if (new_pos := pos+d) in obstacles:
                            break
                        pos = new_pos

            farthest = max(farthest, int(pos.real**2 + pos.imag**2))

        return farthest