# bioinformatics.py

from Bio import SeqIO

class Bioinformatics:
    def __init__(self):
        pass

    def analyze_genome(self, fasta_file):
        """
        This function parses a FASTA file containing genomic sequences and extracts
        the ID and length of each sequence. It's useful in genome analysis workflows.
        
        Args:
            fasta_file (str): Path to the FASTA file containing genome sequences.
        
        Returns:
            List[Dict]: A list of dictionaries containing sequence data (ID, length, sequence).
        """
        sequence_data = []
        for record in SeqIO.parse(fasta_file, "fasta"):
            print(f"ID: {record.id}, Sequence Length: {len(record.seq)}")
            sequence_data.append({
                "id": record.id,
                "length": len(record.seq),
                "sequence": str(record.seq)
            })
        return sequence_data

