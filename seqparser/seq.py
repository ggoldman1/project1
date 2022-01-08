# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # simple checks -- ennsure nonzero sequence, capitalize seq, ensure only A, C, G, T in seq.
    dna = {'A', 'C', 'G', 'T'}

    if len(seq) == 0:
        raise ValueError("You passed in an empty sequence.")

    seq = seq.upper()

    if not set(seq).issubset(dna): # if the sequence contains other characters
        raise ValueError("Your sequence can only contain A, C, G, and T, but you included a sequence with"
                         f" {set(seq) - dna}.")

    complement = {"A": "U", "T": "A", "C": "G", "G": "C"}
    
    return ''.join(complement[base] for base in seq)


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq)[::-1]
