def to_rna(dna_strand: str) -> str:
    mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'}
    return dna_strand.translate(mapping)
