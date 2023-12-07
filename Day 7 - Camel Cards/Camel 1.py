import re
from typing import Match

face_val = '23456789TJQKA'
hand_type = ['hc', '1p', '2p', '3k', 'fh', '4k', '5k']


class Hand:
    def __init__(self, m: Match):
        self.hand = m.group(1)
        self.bid = int(m.group(2))
        self.type = self._type()
        self.value = self._value()

    def __str__(self):
        return f'hand={self.hand}, type={self.type} bid={self.bid}'

    def _type(self):
        hand_num = sorted(self.hand.count(c) for c in set(self.hand))
        if hand_num == [1, 1, 1, 1, 1]:
            h = 'hc'
        elif hand_num == [1, 1, 1, 2]:
            h = '1p'
        elif hand_num == [1, 2, 2]:
            h = '2p'
        elif hand_num == [1, 1, 3]:
            h = '3k'
        elif hand_num == [2, 3]:
            h = 'fh'
        elif hand_num == [1, 4]:
            h = '4k'
        else:
            h = '5k'
        return h

    def _value(self):
        return sum(13**face_val.index(f) for f in self.hand)

    def __lt__(self, other):
        if hand_type.index(self.type) == hand_type.index(other.type):
            return self.value < other.value
        return hand_type.index(self.type) < hand_type.index(other.type)


with open('input', 'r') as file:
    hands = [Hand(m) for m in re.finditer(r'(\w+) (\d+)', file.read())]

if __name__ == '__main__':
    print(sum((i+1)*hand.bid for i, hand in enumerate(sorted(hands))))

