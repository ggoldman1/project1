# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # simple checks -- ennsure nonzero sequence, ensure only A, C, G, T in seq, capitalize seq.
    dna = {'A', 'C', 'G', 'T'}

    if len(seq) == 0:
        raise ValueError("You passed in an empty sequence.")

    if set(seq) > dna:
        raise ValueError("Your sequence can only contain A, C, G, and T, but you included a sequence with"
                         f" {set(seq) - dna}.")

    seq = seq.upper()
    
    return seq.replace('T', 'U')


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq)[::-1]
