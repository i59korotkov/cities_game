import pandas as pd
from game import Game

if __name__ == '__main__':
    cities = pd.read_csv('cities.csv')['city'].to_list()
    game = Game(cities)

    players_num = int(input('Input players count: '))
    for i in range(players_num):
        game.add_player(input(f'Player {i+1} name: '))

    winner = game.start()

    print(f'Winner: {winner}')
