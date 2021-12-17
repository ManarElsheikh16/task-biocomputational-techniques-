#Human protein sequence
from pyopenms import *
from urllib.request import urlretrieve
gh = "https://www.uniprot.org/uniprot/P01241.fasta"
urlretrieve (gh , "human.fasta")

dig = ProteaseDigestion()
dig.getEnzymeName() # Trypsin
bsa = "".join([l.strip() for l in open("human.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)

result = [] 
dig.digest(bsa, result)
print(result[1].toString())
len(result) 


dig.setMissedCleavages(3)
dig.digest(bsa, result, 7, 60)
for s in result:
    print(s.toString())


dig.digest(bsa, result, 5, 40)
for s in result:
    print(s.toString())
###################################################################################
#YEAST protein sequence

from urllib.request import urlretrieve
from pyopenms import*
gh = "https://www.uniprot.org/uniprot/P46672.fasta"
urlretrieve (gh , "YEAST.fasta")

dig = ProteaseDigestion()
dig.getEnzymeName() # Trypsin
bsa = "".join([l.strip() for l in open("YEAST.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)

result = []
dig.digest(bsa, result)
print(result[9].toString())
print(len(result)) 


dig.digest(bsa, result, 7, 40)
for s in result:
    print(s.toString())
###################################################################################
#Proteolytic Digestion with Lys-C
names = []
ProteaseDB().getAllNames(names)
len(names) 
print(names)

e = ProteaseDB().getEnzyme('Lys-C')
e.getRegExDescription()

from urllib.request import urlretrieve
gh = "https://www.uniprot.org/uniprot/P01241.fasta"
urlretrieve (gh , "human.fasta")

dig = ProteaseDigestion()
dig.setEnzyme('Lys-C')
bsa = "".join([l.strip() for l in open("human.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[6].toString())
print(len(result))

gh = "https://www.uniprot.org/uniprot/P46672.fasta"
urlretrieve (gh , "YEAST.fasta")

dig = ProteaseDigestion()
dig.setEnzyme('Lys-C')
bsa = "".join([l.strip() for l in open("YEAST.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[4].toString())
print(len(result)) 