import pytest
from backend.twitter_monitor import TwitterMonitor

def test_twitter_monitor():
    monitor = TwitterMonitor("api_key", "api_secret", "access_token", "access_secret")
    assert monitor is not None