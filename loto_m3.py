import random

class Card:
    def __init__(self):
        self.rows = 3
        self.cols = 9
        self.card = self.generate_card()

    def generate_card(self):
        card = []
        while True:
            row = random.sample(range(1, 91), 5)
            row.sort()
            while len(row) < self.cols:
                row.append(" ")
            if row not in card:  # Проверяем, что строка не дублируется
                card.append(row)
            if len(card) == self.rows:
                break
        return card

    def display(self):
        for row in self.card:
            print(" ".join(map(str, row)))

    def mark_number(self, number):
        for row in self.card:
            if number in row:
                row[row.index(number)] = "X"

    def is_winner(self):
        for row in self.card:
            if " " in row:
                return False
        return True

class BingoGame:
    def __init__(self):
        self.players = []
        self.current_player = None
        self.bag = list(range(1, 91))

    def add_player(self, player):
        self.players.append(player)

    def next_turn(self):
        if not self.bag:
            print("Игра окончена! Все бочонки выбраны.")
            return True  # Добавляем переменную game_over и возвращаем True, чтобы обозначить конец игры

        number = random.choice(self.bag)
        self.bag.remove(number)
        print(f"Новый бочонок: {number} (осталось {len(self.bag)})")
        for player in self.players:
            player.display_card()
            if player.is_user_flag:
                choice = input("Зачеркнуть цифру? (y/n): ")
                if choice.lower() == 'y':
                    player.take_turn(number)
            else:
                if number in [num for row in player.card.card for num in row]:
                    player.take_turn(number)

    def play(self):
        game_over = False  # Инициализируем переменную game_over
        while not game_over:  # Пока game_over равно False, продолжаем игру
            game_over = self.next_turn()  # Проверяем, окончена ли игра после каждого хода
        for player in self.players:
            if player.is_winner():
                print(f"Игрок {player.name} выиграл!")

class Player:
    def __init__(self, name, is_user_flag=True):
        self.name = name
        self.is_user_flag = is_user_flag
        self.card = Card()

    def display_card(self):
        print(f"------ Карточка {self.name} -----")
        self.card.display()
        print("--------------------------")

    def take_turn(self, number):
        if number in [num for row in self.card.card for num in row]:
            self.card.mark_number(number)
        else:
            print(f"Цифры {number} нет на карточке {self.name}. Вы проиграли!")
            exit()

    def is_winner(self):
        return self.card.is_winner()

if __name__ == "__main__":
    print("Выберите тип первого игрока:")
    print("1. Человек")
    print("2. Компьютер")
    choice = input("Введите номер: ")
    if choice == "1":
        player1 = Player("пользователь", is_user_flag=True)
    else:
        player1 = Player("компьютер", is_user_flag=False)

    print("Выберите тип второго игрока:")
    print("1. Человек")
    print("2. Компьютер")
    choice = input("Введите номер: ")
    if choice == "1":
        player2 = Player("пользователь", is_user_flag=True)
    else:
        player2 = Player("компьютер", is_user_flag=False)

    game = BingoGame()
    game.add_player(player1)
    game.add_player(player2)

    game.play()

