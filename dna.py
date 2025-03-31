import random

# Nucleotides
Nucleotides = ["A", "T", "C", "G"]

# DNA to RNA Transcription
DNA_to_RNA = {"A": "U", "T": "A", "C": "G", "G": "C"}

# Reverse Complement
DNA_complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

# Function to validate DNA sequence
def validate_dna_sequence(seq):
    """Check if the sequence is a valid DNA sequence (contains only A, T, C, G)"""
    seq = seq.upper()
    for nucleotide in seq:
        if nucleotide not in Nucleotides:
            return False
    return True

# Function to generate random DNA sequence
def generate_random_dna(length):
    """Generate a random DNA sequence of given length"""
    return ''.join(random.choice(Nucleotides) for _ in range(length))

# Transcription: DNA -> RNA
def transcribe_dna_to_rna(seq):
    """Transcribe DNA sequence to RNA sequence"""
    return ''.join([DNA_to_RNA[nuc] for nuc in seq])

# Reverse Complement: DNA -> Reverse Complement DNA
def reverse_complement(seq):
    """Generate the reverse complement of a DNA sequence"""
    return ''.join([DNA_complement[nuc] for nuc in reversed(seq)])

# GC Content
def calculate_gc_content(seq):
    """Calculate the GC content (percentage of G and C nucleotides)"""
    gc_count = seq.count("G") + seq.count("C")
    return round(gc_count / len(seq) * 100, 2)

# Example Usage
if __name__ == "__main__":
    # Example DNA sequence
    dna_seq = "ATCGTACGTA"
    
    # Validate DNA sequence
    if validate_dna_sequence(dna_seq):
        print(f"DNA Sequence: {dna_seq}")
        
        # Transcription to RNA
        rna_seq = transcribe_dna_to_rna(dna_seq)
        print(f"RNA Transcription: {rna_seq}")
        
        # Reverse Complement
        rev_comp_seq = reverse_complement(dna_seq)
        print(f"Reverse Complement: {rev_comp_seq}")
        
        # GC Content
        gc_content = calculate_gc_content(dna_seq)
        print(f"GC Content: {gc_content}%")
        
        # Generate a random DNA sequence of length 15
        random_dna_seq = generate_random_dna(15)
        print(f"Random DNA Sequence: {random_dna_seq}")
    else:
        print("Invalid DNA sequence!")
