#!/usr/bin/env python

import pytest
from text2tweets.text2tweets import TextManipulation


def test_integration():
    txt = "input_text.txt"
    result = "output_text.txt"

    print(f"{'*'*10} Integration test start {'*'*10}")

    tm = TextManipulation(txt, result)
    chunks = tm.read_text()
    tweets = tm.process_text(chunks)
    tm.save_text(tweets)
    print(f"{'*'*10} Done {'*'*10}")

    assert True
