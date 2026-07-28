# pylint: disable=missing-module-docstring
import pytest
import src.hang

# def test_exit_check():
#     """Test that passing 'exit' raises SystemExit."""
#     with pytest.raises(SystemExit):
#         exit_check("exit")


@pytest.mark.parametrize(
    'input_string, expected',
    [
        ('g', False),
        ('6', True),
        ("`", False)
    ]
)

def test_is_number(input_string, expected):
    """Testing if the user inputs a number"""
    assert src.hang.is_number(input_string) == expected

@pytest.mark.parametrize(
    'input_n , squared',
    [
        (3,9),
        (2,4),
        (5,20)
    ]
)

def test_trying_something(input_n, squared):
    "Trying something"
    assert src.hang.trying_something(input_n) == squared
