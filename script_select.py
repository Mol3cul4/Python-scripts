import os
import sys
import csv
from Bio import SeqIO

#Create tmp files
#os.popen('cp $HOME/Teste/pasta_contigs/*.fa $HOME/Teste/')

tsv_file = open("virus.tsv") #Path for TSV table. Changes in 1 column.

read_tsv = csv.reader(tsv_file, delimiter = "\t")

lista_contigs = []
lista_samples = []

for row in read_tsv:
	lista_contigs.append(row[1])
	lista_samples.append(row[0])

zip_iterator = zip(lista_contigs, lista_samples)

a_dictionary = dict(zip_iterator)

#Directory with assembled contigs fasta
directory = "$HOME/Teste/pasta_contigs" # <-- change here

files_contigs = os.listdir(directory)

qtd_files_contigs = len(files_contigs)

for i in range(qtd_files_contigs):
	for j in a_dictionary:
		if a_dictionary[j] == files_contigs[i].split('.')[0]:
			for seq_record in SeqIO.parse(files_contigs[i], "fasta"):
				if seq_record.id == j:
					original_stdout = sys.stdout
					with open(files_contigs[i].split('.')[0]+"_"+seq_record.id+".fasta", 'w') as f:
						sys.stdout = f
						print(">"+files_contigs[i].split('.')[0]+" "+seq_record.id)
						print(seq_record.seq)
						sys.stdout = original_stdout

#Remove tmp files
os.popen('rm $HOME/Teste/*.fa') # <-- change here

#Moving results to a new directory
os.popen('mkdir $HOME/Teste/results/') # <-- change here
os.popen('mv $HOME/Teste/*.fasta $HOME/Teste/results/') # <-- change here
