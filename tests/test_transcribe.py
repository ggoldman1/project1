# write tests for transcribes
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    assert transcribe("ACTG") == "UGAC"
    assert transcribe("AAAAAAA") == "UUUUUUU"
    assert transcribe("gtca") == "CAGU"
    assert transcribe("ACTGAACCC") == "UGACUUGGG"

    with pytest.raises(ValueError):
        transcribe("ABCD")
        transcribe("")


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    assert reverse_transcribe("ACTG") == "CAGU"
    assert reverse_transcribe("AAAAAA") == "UUUUUU"
    assert reverse_transcribe("gtca") == "UGAC"
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU"
    
    with pytest.raises(ValueError):
        transcribe("ABCD")
        transcribe("")

