with open('GFPs.csv', 'w') as outfile:
    for s in strings:
        outfile.write(" ".join(list(s)))
        outfile.write("\n")
