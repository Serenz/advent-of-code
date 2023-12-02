"""
    Source of the challege:
    https://adventofcode.com/2023/day/2

    Second part of the challenge:
    https://adventofcode.com/2023/day/2#part2
"""

OK = {
    'red': 12,
    'green': 13,
    'blue': 14
}


if __name__ == '__main__':
    with open('day2_input.txt', 'r') as f:
        games = f.readlines()
    result = 0
    for game in games:
        num, hands = game.replace('\n', '').split(': ')
        num = int(num.split(' ')[1])
        # hands = game.split(': ')[1].split('; ')
        hands = hands.split('; ')
        flag = True
        for hand in hands:
            picks = hand.split(', ')
            if flag:
                for pick in picks:
                    val, color = pick.split(' ')
                    if int(val) > OK[color]:
                        flag = False
                        break
        if flag:
            result += num
    print(result)