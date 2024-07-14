class Solution:
    def countOfAtoms(self, formula: str) -> str:
        muls = []
        running_mul = 1

        stack = [1]

        idx = len(formula) - 1
        curr = ''
        while idx >= 0:
            if formula[idx].isdigit():
                curr += formula[idx]

            # If we encountered a letter, then the scanned
            # number was count and not multiplier. Discard it.
            elif formula[idx].isalpha():
                curr = ""

            # If we encounter a right parenthesis, then the
            # scanned number was a multiplier. Store it.
            elif formula[idx] == ")":
                curr_multiplier = int(curr[::-1]) if curr else 1
                running_mul *= curr_multiplier
                stack.append(curr_multiplier)
                curr = ""

            # If we encounter a left parenthesis, then the
            # most recent multiplier will cease to exist.
            elif formula[idx] == "(":
                running_mul //= stack.pop()
                curr = ""

            # For every idx, store the valid multiplier
            muls.append(running_mul)
            idx -= 1

        # Reverse the muls
        muls = muls[::-1]

        # Map to store the count of atoms
        final_map = defaultdict(int)

        # Traverse left to right in the formula
        idx = 0
        while idx < len(formula):
            # If UPPER CASE LETTER, extract the entire atom
            if formula[idx].isupper():
                curr_atom = formula[idx]
                curr_count = ""
                idx += 1
                while idx < len(formula) and formula[idx].islower():
                    curr_atom += formula[idx]
                    idx += 1

                # Extract the count
                while idx < len(formula) and formula[idx].isdigit():
                    curr_count += formula[idx]
                    idx += 1

                # Update the final map
                if curr_count:
                    final_map[curr_atom] += int(curr_count) * muls[idx - 1]
                else:
                    final_map[curr_atom] += 1 * muls[idx - 1]

            else:
                idx += 1

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans