import re
import csv
 
print("Usage: site('RE sequence', 'excel filename'). Make sure the excel file has primer data starting in the first row and that the first column is a primer ID and the second column is the primer sequence. The file should be a .csv")
re_degenerates = re.compile(r"[wsmkrybdhvn]")
 
def get_patterns(filename):
    with open(filename) as f:
        #lines = f.readlines()[2:] # the first two lines aren't data
        lines = f.readlines()
        for record in csv.reader(lines):
            index = record[0] # the first column is the pattern id
            #pattern = record[1] #this *should look at the second column in the CSV
            pattern = "".join(record[1:]).lower() # the rest of the columns are nucleotides (This line was for separated nucleotides uin the CSV)
            print(record)
            yield index, pattern
        
 
def has_degenerate(pattern):
    return re_degenerates.search(pattern) is not None
 
 
def get_permutations(pattern):
    """ Return all of the possible interpretation/permutations of pattern
 
    pattern is a string that matches /[actgwsmkrybdhvn]+/
 
    Usage:
    >>> tuple(get_permutations("acww"))
    ('acaa', 'acat', 'acta', 'actt')
    """
    _degeneracy = {
        "w": ("a", "t"),
        "s": ("c", "g"),
        "m": ("a", "c"),
        "k": ("g", "t"),
        "r": ("a", "g"),
        "y": ("c", "t"),
        "b": ("c", "g", "t"),
        "d": ("a", "g", "t"),
        "h": ("a", "c", "t"),
        "v": ("a", "c", "g"),
        "n": ("a", "c", "g", "t"),
    }
 
    if has_degenerate(pattern):
        for nuc in pattern:
            if nuc in _degeneracy:
                for resolved_nuc in _degeneracy[nuc]:
                    new_pattern = pattern.replace(nuc, resolved_nuc, 1)
                    yield from get_permutations(new_pattern)
                break
    else:
        yield pattern
 
def find_sequence(sequence, degenerate_pattern):
    """ Return true if sequence is in any of the permutations of degenerate_pattern.
 
    sequence must consist only of real base pairs. (it must match /[actg]+/)
    """
    re_sequence = re.compile(sequence)
    for permutation in get_permutations(degenerate_pattern):
        match = re_sequence.search(permutation)
        if match:
            print("Matched sequence '{0}' in permutation '{1}' at position {2}".format(sequence, swaprange(permutation, *match.span()), match.span()))
    return False
 
def site(sequence, filename = 'data.csv'):
    for id, pattern in get_patterns(filename):
        print("Permuting pattern {0}".format(id))
        if not find_sequence(sequence, pattern):
            print("Found no matches")
        print()
 
#def print_this(sequence):
 #   """ test case trying to get definitions of functions into the script"""
  #  print(sequence)
    
def swaprange(s, left, right):
    return s[:left] + s[left:right].swapcase() + s[right:]