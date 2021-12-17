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


