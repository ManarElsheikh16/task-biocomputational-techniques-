import pyopenms
from pyopenms import *
import pyopenms as SQ

sum=0
seq=SQ.AASequence.fromString("VAKA")

for aa in seq:
    sum+=aa.getMonoWeight()
print(sum)
    
seqq=SQ.AASequence.fromString("VAKA")
total=seqq.getMonoWeight()
print(total)

#mass of VAKA !=mass of V + mass of A + mass of K + mass of A
#387.2481710527!=441.2798662441