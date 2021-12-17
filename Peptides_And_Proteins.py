#Peptides and Proteins
#Amino Acid Sequences
from pyopenms import *
seq=AASequence.fromString("DFPIANGER")
prefix=seq.getPrefix(4)
suffix=seq.getSuffix(5)
concate=seq+seq
print("Sequence:", seq)
print("Prefix:", prefix)
print("Suffix:", suffix)
print("Concatenated:", concate)
mfull=seq.getMonoWeight()
mprecursor=seq.getMonoWeight(Residue.ResidueType.Full,2)
mz=seq.getMZ(2)
print("Monoisotopic mass of peptide [M] is", mfull)
print("Monoisotopic mass of peptide precursor [M+2H]2+ is", mprecursor)
print("Monoisotopic m/z of [M+2H]2+ is", mz)
print("="*35)


#The AASequence object also allows iterations directly in Python:
from pyopenms import *
seq=AASequence.fromString("DFPIANGER")
print("The peptide",str(seq),"consists of the following amino acids:")
for aa in seq:
    print(aa.getName(), ":", aa.getMonoWeight())
print("="*35)


#The N- and C-Terminus as well as the residues themself can be modified. The example below shows how to check fo such modifications.
from pyopenms import *
seq = AASequence.fromString("C[143]PKCK(Label:13C(6)15N(2))CR")
if seq.hasNTerminalModification():
    print("N-Term Modification: ",seq.getNTerminalModification().getFullId())
if seq.hasCTerminalModification():
    print("C-Term Modification: ",seq.getCTerminalModification().getFullId())
for aa in seq:
    if (aa.isModified()):
        print(aa.getName(), ":", aa.getMonoWeight(), ":", aa.getModificationName())
    else:
        print(aa.getName(), ":", aa.getMonoWeight())
print("="*35)


#Peptide Molecular formula
from pyopenms import *
seq=AASequence.fromString("DFPIANGER")
seq_formula=seq.getFormula()
print("Peptide",seq,"has molecular formula",seq_formula)
print("="*35)


#Isotope patterns
from pyopenms import *
coarse_isotopes=seq_formula.getIsotopeDistribution(CoarseIsotopePatternGenerator(6))
for iso in coarse_isotopes.getContainer():
    print ("Isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")

# print fine structure of isotope distribution
from pyopenms import *
fine_isotopes = seq_formula.getIsotopeDistribution(FineIsotopePatternGenerator(0.01))
for iso in fine_isotopes.getContainer():
    print ("Isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")



#Fragment ions
from pyopenms import *
suffix = seq.getSuffix(3)
print("="*35)
print("y3 ion sequence:",suffix)
y3_formula = suffix.getFormula(Residue.ResidueType.YIon, 2)
suffix.getMonoWeight(Residue.ResidueType.YIon, 2) / 2.0 
suffix.getMonoWeight(Residue.ResidueType.XIon, 2) / 2.0 
suffix.getMonoWeight(Residue.ResidueType.BIon, 2) / 2.0 
print("y3 mz:",suffix.getMonoWeight(Residue.ResidueType.YIon, 2) / 2.0 )
print("y3 molecular formula:",y3_formula)

#Modified Sequences
from pyopenms import *
seq=AASequence.fromString("PEPTIDESEKUEM(Oxidation)CER")
print(seq.toUnmodifiedString())
print(seq.toString())
print(seq.toUniModString())
print(seq.toBracketString())
print(seq.toBracketString(False))
print(AASequence.fromString("DFPIAM(UniMod:35)GER"))
print(AASequence.fromString("DFPIAM[+16]GER"))
print(AASequence.fromString("DFPIAM[+15.99]GER"))
print(AASequence.fromString("DFPIAM[147]GER"))
print(AASequence.fromString("DFPIAM[147.035405]GER"))
print("="*35)

#Proteins and FASTA files
from pyopenms import *
bsa=FASTAEntry() 
bsa.sequence="MKWVTFISLLLLFSSAYSRGVFRRDTHKSEIAHRFKDLGE"
bsa.description="BSA Bovine Albumin (partial sequence)"
bsa.identifier="BSA"
alb=FASTAEntry()
alb.sequence="MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGE"
alb.description="ALB Human Albumin (partial sequence)"
alb.identifier="ALB"
entries=[bsa, alb]
f=FASTAFile()
f.store("example.fasta", entries)
for e in entries:
      print (e.identifier, e.sequence,e.description)
print("="*35)

