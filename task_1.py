#Constants
import pyopenms
help(pyopenms.Constants)
print(pyopenms.Constants.AVOGADRO)
print("="*35)

#Elements
from pyopenms import *
edb=ElementDB()
print(edb.hasElement("O"))
print(edb.hasElement("S"))
Oxygen=edb.getElement("O")
print(Oxygen.getName())
print(Oxygen.getSymbol())
print(Oxygen.getMonoWeight())
print(Oxygen.getAverageWeight())
Sulfar=edb.getElement("S")
print(Sulfar.getName())
print(Sulfar.getSymbol())
print(Sulfar.getMonoWeight())
print(Sulfar.getAverageWeight())
isotopes_sulfar=Sulfar.getIsotopeDistribution()
print(isotopes_sulfar)
print("One mole of oxygen weighs",2*Oxygen.getAverageWeight(), "grams")
print("One mole of 16O2 weighs",2*Oxygen.getMonoWeight(), "grams")
print("="*35)

#Isotopes
from pyopenms import *
edb=ElementDB()
Oxygen_IsoDist={"mass":[],"abundance":[]}
Sulfar_IsoDist={"mass":[],"abundance":[]}
Oxygen=edb.getElement("O")
istopes=Oxygen.getIsotopeDistribution()
for iso in istopes.getContainer():
    print ("Oxygen isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")
    Oxygen_IsoDist["mass"].append(iso.getMZ())
    Oxygen_IsoDist["abundance"].append((iso.getIntensity() * 100))
Sulfar=edb.getElement("S")
istopes=Sulfar.getIsotopeDistribution()
for iso in istopes.getContainer():
    print ("Oxygen isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")
    Oxygen_IsoDist["mass"].append(iso.getMZ())
    Oxygen_IsoDist["abundance"].append((iso.getIntensity() * 100))
print("="*35)


#Mass Defect_1
from pyopenms import *
edb=ElementDB()
isotopes=edb.getElement("C").getIsotopeDistribution().getContainer()
Carbon_Isotope_Difference=isotopes[1].getMZ()-isotopes[0].getMZ()
isotopes=edb.getElement("N").getIsotopeDistribution().getContainer()
Nitrogen_Isotope_Difference=isotopes[1].getMZ()-isotopes[0].getMZ()
print("Mass difference between 12C and 13C:", Carbon_Isotope_Difference)
print("Mass difference between 14N and N15:", Nitrogen_Isotope_Difference)
print("Relative deviation:", 100*(Carbon_Isotope_Difference -
        Nitrogen_Isotope_Difference)/Carbon_Isotope_Difference, "%")
print("="*35)


#Mass Defect_2
from pyopenms import *
from pyopenms.Constants import *
Helium=ElementDB().getElement("He")
isotopes=Helium.getIsotopeDistribution()
mass_sum=2*PROTON_MASS_U+2*ELECTRON_MASS_U+2*NEUTRON_MASS_U
Helium4=isotopes.getContainer()[1].getMZ()
print("Sum of masses of 2 protons,neutrons and electrons:",mass_sum)
print ("Mass of He4:",Helium4)
print ("Difference between the two masses:",100*(mass_sum - Helium4)/mass_sum,"%")
print("="*35)


#Molecular Formulae
from pyopenms import *
Methanol=EmpiricalFormula("CH3OH")
Water=EmpiricalFormula("H2O")
Ethanol=EmpiricalFormula("CH2")+Methanol
print("Ethanol chemical formula:",Ethanol.toString())
print("Ethanol composition:",Ethanol.getElementalComposition())
print("Ethanol has",Ethanol.getElementalComposition()[b"H"],"hydrogen atoms")
print("="*35)


#Amino Acids
from pyopenms import *
lys=ResidueDB().getResidue("Lysine")
print(lys.getName())
print(lys.getThreeLetterCode())
print(lys.getOneLetterCode())
print(lys.getAverageWeight())
print(lys.getMonoWeight())
print(lys.getPka())
print(lys.getFormula().toString())
print("="*35)

#Amino Acid Modifications
from pyopenms import *
Ox=ModificationsDB().getModification("Oxidation")
print(Ox.getUniModAccession())
print(Ox.getUniModRecordId())
print(Ox.getDiffMonoMass())
print(Ox.getId())
print(Ox.getFullId())
print(Ox.getFullName())
print(Ox.getDiffFormula())
print("="*35)


#Ribonucleotides
from pyopenms import *
uridine=RibonucleotideDB().getRibonucleotide(b"U")
print(uridine.getName())
print(uridine.getCode())
print(uridine.getAvgMass())
print(uridine.getMonoMass())
print(uridine.getFormula().toString())
print(uridine.isModified())
methyladenosine=RibonucleotideDB().getRibonucleotide(b"m1A")
print(methyladenosine.getName())
print(methyladenosine.isModified())
print("="*35)


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