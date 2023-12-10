import re
from typing import Match

face_val = '23456789TJQKA'
hand_type = ['hc', '1p', '2p', '3k', 'fh', '4k', '5k']


class Hand:
    def __init__(self, m: Match):
        self.hand = m.group(1)
        self.bid = int(m.group(2))
        self.type = self._type()

    def __str__(self):
        return f'hand={self.hand}, type={self.type} bid={self.bid}'

    def _type(self):
        hand_num = sorted(self.hand.count(c) for c in set(self.hand))
        if hand_num == [5]:
            return '5k'
        elif hand_num == [1, 4]:
            return '4k'
        elif hand_num == [2, 3]:
            return 'fh'
        elif hand_num == [1, 1, 3]:
            return '3k'
        elif hand_num == [1, 2, 2]:
            return '2p'
        elif hand_num == [1, 1, 1, 2]:
            return '1p'
        else:
            return 'hc'

    def __lt__(self, other):
        if hand_type.index(self.type) == hand_type.index(other.type):
            for cs, co in zip(self.hand, other.hand):
                if face_val.index(cs) != face_val.index(co):
                    return face_val.index(cs) < face_val.index(co)
        return hand_type.index(self.type) < hand_type.index(other.type)


with open('input', 'r') as file:
    hands = [Hand(m) for m in re.finditer(r'(\w+) (\d+)', file.read())]

if __name__ == '__main__':
    print(sum((i+1)*hand.bid for i, hand in enumerate(sorted(hands))))

