import pytest
from stats_tagger import parse_event, get_event, get_outcome, get_player_no

# Test input values for test_parse_input
test_inputs = ["s22", "sw15", "tisu4",
               "ko22won", "ss23", "sw15",
               "se", "ss", "kos",
               "kow", "kowon", "kolost",
               "kol", "kog", "f16",
               "fg15", "f"]

# Expected output values for test_parse_input
expected_output = [
    ['shot', None, "22"],
    ['shot', 'wide', '15'],
    ['tackle', None, '4'],
    ['kickout', None, None],
    ['shot', None ,'23'],
    ['shot', 'wide', '15'],
    ['shot', None, None],
    ['shot', None, None],
    ['kickout', None, None],
    ['kickout', None, None],
    ['kickout', 'won', None],
    ['kickout', 'lost', None],
    ['kickout', None, None],
    ['kickout', None, None],
    ['foul', None, '16'],
    ['foul', None, '15'],
    ['foul', None, None]
]
def test_parse_input():
    for index, input in enumerate(test_inputs):
        assert parse_event(input) == expected_output[index]

def test_get_event():
    assert get_event("sg69696969") == ("sg", "start game", "69696969") # Chat GPT used to find errors with changing lists to tuples
    assert get_event("f14") == ("f", "foul", "14")