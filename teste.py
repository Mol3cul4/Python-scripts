from Bio.Seq import Seq
from Bio import SeqIO

my_seq = Seq("ATGCCG")

seq_complementar = my_seq.complement()
seq_revcomp = my_seq.reverse_complement()
seq_rna = my_seq.transcribe()
dna_back = seq_rna.back_transcribe()

aa1 = seq_rna.translate()
aa2 = dna_back.translate()

print(aa1)
print(aa2)

for fasta in SeqIO.parse("seq.fasta", "fasta"):
	print(fasta.id)
	print(fasta.seq)