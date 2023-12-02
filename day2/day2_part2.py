"""
    Source of the challege:
    https://adventofcode.com/2023/day/2

    Second part of the challenge:
    https://adventofcode.com/2023/day/2#part2
"""


if __name__ == '__main__':
    with open('day2_input.txt', 'r') as f:
        games = f.readlines()
    result = 0
    for game in games:
        num, hands = game.replace('\n', '').split(': ')
        num = int(num.split(' ')[1])
        hands = hands.split('; ')
        mins = {}
        for hand in hands:
            picks = hand.split(', ')
            for pick in picks:
                val, color = pick.split(' ')
                mins[color] = max(mins.get(color, int(val)), int(val))
        t = 1
        for v in mins.values():
            t *= v
        result += t
    print(result)