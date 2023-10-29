class Solution:
    def checkRecord(self, s: str) -> bool:
        #Process the string linearly and count the days, reset the late counter accordingly and keep checking if the student is absent in total according to the conditions
        late_count = 0
        absent_count = 0
        for char in s:
            if char == 'L':
                late_count += 1
            else:
                if char == 'A':
                    absent_count += 1
                late_count = 0
            if absent_count >= 2 or late_count >= 3:
                return False
        return True
