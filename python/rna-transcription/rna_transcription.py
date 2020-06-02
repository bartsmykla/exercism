def to_rna(dna_strand):
    complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return ''.join(complements.get(char, char) for char in dna_strand)
