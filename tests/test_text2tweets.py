#!/usr/bin/env python

"""Tests for `text2tweets` package."""

import pytest

#from click.testing import CliRunner

from text2tweets import char_per_word
from text2tweets import word_count 
from text2tweets import slices_idx
#from text2tweets import cli

TEST_TEXT = "tst1 "*70 + "tst2 "*70

def test_char_per_word():
    result = char_per_word(TEST_TEXT)
    assert result == [5]*140
    
def test_word_count():
    counts = [5]*140
    result = word_count(counts)
    wc = [5*i for i in range(1,29)]*5
    assert list(result) == wc

def test_slices_idx():
    counts = [5]*140
    accum = [5*i for i in range(1,29)]*5
    pairs = zip(counts, accum)

    result = slices_idx(pairs)
    tweets = [TEST_TEXT[s] for s in result]
    assert (set(tweets[0])=={"tst1 "})&(set(tweets[4])=={"tst2 "})&\
        (set(tweets[2])=={"tst1 ", "tst2 "})


#@pytest.fixture
#def response():
#    """Sample pytest fixture.
#
#    See more at: http://doc.pytest.org/en/latest/fixture.html
#    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


#def test_content(response):
#    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


#def test_command_line_interface():
#    """Test the CLI."""
#    runner = CliRunner()
#    result = runner.invoke(cli.main)
#    assert result.exit_code == 0
#    assert 'text2tweets.cli.main' in result.output
#    help_result = runner.invoke(cli.main, ['--help'])
#    assert help_result.exit_code == 0
#    assert '--help  Show this message and exit.' in help_result.output
