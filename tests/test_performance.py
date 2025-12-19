import pytest
from app.stats_tagger import parse_event

test_events = ["sg10", "sp7", "f14"] * 1000  # simulate 3000 events

# ChatGPT assistance with optimising code
def test_parse_event_performance(benchmark):
    benchmark(lambda: [parse_event(e) for e in test_events])
