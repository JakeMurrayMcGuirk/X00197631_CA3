import pytest
from app.stats_tagger import parse_event

# Create list of 3 events, 1000 times - simulating 3000 events
test_events = ["sg10", "sp7", "f14"] * 1000

# ChatGPT assistance with optimising code
def test_parse_event_performance(benchmark):
    # For each event in test_events, run parse_event on it
    benchmark(lambda: [parse_event(e) for e in test_events])
