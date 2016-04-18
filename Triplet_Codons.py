import os
test_sequence = 'aTGAGTAAAGGAGAAGaacttttcactggagttgtcccaattcttgttgaattagatggtgatgttaatgggcacaaattttctgtcagtggagagggtgaaggtgatgcaacatacggaaaacttacccttaaatttatttgcactactggaaaactacctgttccgtggccaacacttgtcactactttctctaagggtgttcaatgcttttcccgttatccggatcacatgaaacgGcatgactttttcAAAagCgccatgcccgaaggttatgtacaggaacgcactatatctttcaaagatgacgggaactacaagacgcgtgctgaagtcaagtttgaaggtgatacccttgttaatcgtatcgagttaaaaggtattgattttaaagaagatggaaacattctcggacacaaactggagtacaactataactcacacaatgtatacatcacggcagacaaacaaaagaatggaatcaaagctaacttcaaaattcgccacaacattgaagatggctccgttcaactagcagaccattatcaacaaaatactccaattggcgatggccctgtccttttaccagacaaccattacctgtccacacaatctgccctttcgaaagatcccaacgaaaagcgtgaccacatggtccttcttgagtttgtaactgctgctgggattacacatggcatggatgagctctacaaacaccaccaccaccaccac'
print('Usage, triplets(Input DNA sequence, "name of gene")')


def triplets(Gene_Sequence, Gene_Name):
	s = Gene_Sequence.upper()

	s[::3]
	z = zip(s[::3], s[1::3], s[2::3])
	triples =[]
	for t in z:

		triples.append(''.join(t))
	triples_string = ' '.join(triples)
	print(triples_string)

	write_to_file(triples_string, Gene_Name + '.txt')

def write_to_file(s, filename = 'out.txt'):
	with open(filename, 'w') as outfile:
		outfile.write(s) 
	curdir = os.path.dirname(os.path.realpath(__file__))
	print('output written to ' + os.sep.join((curdir, filename)) )

