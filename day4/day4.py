"""
    Source of the challege:
    https://adventofcode.com/2023/day/4

    Second part of the challenge:
    https://adventofcode.com/2023/day/4#part2
"""


if __name__ == '__main__':
    with open('day4_input.txt', 'r') as f:
        cards = f.readlines()
    result = 0
    for card in cards:
        winners, hand = card.split(': ')[1].split(' | ')
        winners = set(winners.split())
        hand = set(hand.split())
        if winners & hand:
            result += 2 ** (len(winners & hand)-1)
    print(result)
    