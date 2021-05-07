#Dictionary to save and return fasta sequences 
arquivo = open("seq.fasta")
lines = arquivo.readlines()

multifasta = {}

for i in lines:
	if(i[0] == '>'):
		seq_atual = i.strip()
		#multifasta[seq_atual] = ''
	else:
		multifasta[seq_atual] = i.strip()


for i in multifasta:
	print i
	print multifasta[i]