n = int(input())
unique_compounds = set([])

for i in range(n):
    chemical_compounds = input().split()
    for compound in chemical_compounds:
        unique_compounds.add(compound)

print("\n".join(unique_compounds))

