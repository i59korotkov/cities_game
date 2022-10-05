class Game:
    def __init__(self, cities_list: list) -> None:
        self.cities_list = [city.lower() for city in cities_list]
        self.players = []
        self.active = False
    
    def city_is_valid(self, prev_city: str, city: str) -> bool:
        prev_city = prev_city.lower().strip()
        city = city.lower().strip()

        if city not in self.cities_list:
            return False
        
        if city[0] != prev_city[-1]:
            return False

        return True

    def add_player(self, player_name: str):
        pass

    def add_city(self, player_name: str, city: str) -> bool:
        pass

    def start(self, player1_name: str, player2_name: str) -> str:
        pass

    
