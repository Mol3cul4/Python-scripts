from DNAToolKit import *

import random

rndDNAStr = ''.join([random.choice(Nucleotides)
			for nuc in range(20)])

print(validateSeqDNA(rndDNAStr))
