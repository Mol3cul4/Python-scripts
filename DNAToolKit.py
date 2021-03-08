#DNA Tollkit file
Nucleotides = ['A', 'G', 'C', 'T']

#Check sequence to make sure is a DNA sequence
def validateSeqDNA(dna_seq):
	tmpseq = dna_seq.upper()
	for nuc in tmpseq:
		if nuc not in Nucleotides:
			return False
	
	return tmpseq 



def countNucFrequency(seq):
	tmpFreqDict =  {'A': 0, 'G': 0, 'C': 0, 'T': 0}
	for nuc in seq:
		tmpFreqDict[nuc] += 1
	
	return tmpFreqDict

