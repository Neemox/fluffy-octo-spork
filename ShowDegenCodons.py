import sys
from Degen_Nuc_Script import get_permutations
def showdegeneratecodons(codon):

	for pattern in get_permutations(codon):
		print(pattern)

if __name__ == ("__main__"):
	showdegeneratecodons(sys.argv[1])