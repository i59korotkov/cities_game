class Game:
    def __init__(self, cities_list: list) -> None:
        self.cities_list = [city.lower() for city in cities_list]
        self.players = []
        self.history = [None]
        self.active = False
    
    def city_is_valid(self, prev_city: str, city: str) -> bool:
        city = city.lower().strip()

        if city not in self.cities_list:
            return False
        
        if prev_city is None:
            return True
        
        prev_city = prev_city.lower().strip()
        if city[0] != prev_city[-1]:
            return False

        return True

    def add_player(self, player_name: str):
        if player_name in self.players:
            raise ValueError('Player is already added')
        
        self.players.append(player_name)

    def add_city(self, player_name: str, city: str) -> bool:
        if len(self.players) == 0:
            raise ValueError('There is no players')
        
        if player_name != self.players[0]:
            raise ValueError('It is another player\'s move')
        
        if city in self.history:
            return False
        
        if self.city_is_valid(self.history[-1], city):
            self.history.append(city)
            self.players.append(self.players.pop(0))
            return True
        else:
            return False

    def start(self) -> str:
        self.active = True

        while self.active:
            if not self.add_city(self.players[0], input(f'{self.players[0]}\'s move: ')):
                self.players.remove(self.players[0])

                if len(self.players) == 1:
                    self.active = False
                    return self.players[0]
