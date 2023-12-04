"""
    Source of the challege:
    https://adventofcode.com/2023/day/4

    Second part of the challenge:
    https://adventofcode.com/2023/day/4#part2
"""


if __name__ == '__main__':
    with open('day4_input.txt', 'r') as f:
        cards = f.readlines()
    games = [1]*len(cards)
    for card in cards:
        game = int(card.split(': ')[0].split()[1])
        winners, hand = card.split(': ')[1].split(' | ')
        winners = set(winners.split())
        hand = set(hand.split())
        if winners & hand:
            for _ in range(game, game+len(winners & hand)):
                if _ < len(games):
                    games[_] += games[game-1]
                else:
                    break                    
    result = sum(games)
    print(result)
    