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