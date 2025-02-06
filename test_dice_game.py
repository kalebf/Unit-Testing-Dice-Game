import pytest # type: ignore
from dice_game import roll_dice, check_guess

def test_roll_dice():
    # Roll dice multiple times to check if values are within the valid range
    for _ in range(100):
        result = roll_dice()
        assert 2 <= result <= 12, "Dice roll should be between 2 and 12"

#creates scenarios with proper response for each scenario
@pytest.mark.parametrize("actual_sum, user_guess, expected_output", [
    (7, 7, "Congratulatins! Your guess is correct (7)"),
    (8, 5, "Too low! Try agian."),
    (8, 10, "Too high! Try agian."),
])

#Checks that each scenario above has the proper response 
def test_check_guess(actual_sum, user_guess, expected_output, capsys):
    # Capture printed output during the function call
    check_guess(actual_sum, user_guess)
    captured = capsys.readouterr()
    assert expected_output in captured.out
