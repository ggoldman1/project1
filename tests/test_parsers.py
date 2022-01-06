# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    fa = FastaParser("../data/test.fa")

    records = [r for r in fa]
    assert len(records) == 100, "did not read in correct number of records" # 100 records in total

    for r in records:
        assert len(r) == 2, "the record is the wrong length" # each record consists of header and sequence


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    fq = FastqParser("../data/test.fq")

    records = [r for r in fq]
    assert len(records) == 100, "did not read in correct number of records" # 100 records in total

    for r in records:
        assert len(r) == 3, "the record is the wrong length" # each record is header, sequence, and quality 
