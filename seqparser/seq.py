# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    # simple checks -- ensure only A, C, G, T in seq, capitalize seq.
    dna = {'A', 'C', 'G', 'T'}
    if set(seq) >= dna:
        raise ValueError("Your sequence can only contain A, C, G, and T, but you included a sequence with"
                         f" {set(seq) - dna}.")
    seq = seq.upper()
    
    return seq.replace('T', 'U')


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    return transcribe(seq)[::-1]
