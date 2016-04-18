def get_nuc_options(position):
   options = set()

   try:
       options.add(sequence_a[position])
   except IndexError:
       pass #There's no a at this position.  W/e

   try:
       options.add(sequence_b[position])
   except IndexError:
       pass #There's no b at this position.  W/e

   if len(options) < 1:
       raise IndexError("Neither sequence has a nucleotide for position {}".format(position))

   return options