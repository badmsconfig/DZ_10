import pytest
from loto_m3 import Card, Player, BingoGame

@pytest.fixture
def card():
    return Card()

def test_generate_card_row_count(card):
    card.generate_card()
    assert len(card.card) == card.rows

def test_generate_card_col_count(card):
    card.generate_card()
    for row in card.card:
        assert len(row) == card.cols

def test_mark_number(card):
    number = card.card[1][3]
    card.mark_number(number)
    assert card.card[1][3] == "X"

def test_is_winner(card):
    assert not card.is_winner()
    for row in card.card:
        for i in range(9):
            row[i] = "X"
    assert card.is_winner()

def test_player_is_winner(card):
    player = Player("Test Player")
    assert not player.is_winner()
    for row in player.card.card:
        for i in range(9):
            row[i] = "X"
    assert player.is_winner()

def test_bingo_game_add_player():
    game = BingoGame()
    player = Player("Test Player")
    game.add_player(player)
    assert player in game.players

if __name__ == "__main__":
    pytest.main(["-v", "test_bingo.py", "--cov=loto_m3"])

