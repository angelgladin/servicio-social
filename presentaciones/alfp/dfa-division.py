class DFA(object):
    def __init__(self, k):
        self.k = k
        self.transition_table = self.__fill_transition_table()
    def __fill_transition_table(self):
        automata = [[0, 0] for _ in range(k)] # Representation of the automata in a matrix.
        for state in range(k):  # Computing each transition for every state.
            zero_trans = state << 1  # Next state for 0
            automata[state][0] = zero_trans \
                if zero_trans < self.k else zero_trans - self.k
            one_trans = (state << 1) + 1  # Next state for 1
            automata[state][1] = one_trans \
                if one_trans < self.k else one_trans - self.k
        return automata
    def is_divisible(self, n):
        state = 0  # Initial state
        # Obtain the mask of the most significative bit.
        mask = 1 << (n.bit_length() - 1)
        # Traverse the number in binary format, starting from the most significate bit
        # and in each step obtain the currentt state till there is no string to read.
        while mask != 0:
            current_bit = 1 if mask & n else 0
            state = self.transition_table[state][current_bit]
            mask >>= 1
        return (state == 0, state)
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    dfa = DFA(k)
    is_divisible, remainder = dfa.is_divisible(n)
    if is_divisible:
        print(f"{n} is divisible by {k}")
    else:
        print(f"{n} is not divisible by {k} and the remainder is {remainder}")
