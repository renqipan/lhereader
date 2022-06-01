# source $ROOTSYS/bin/thisroot.sh 

from lhereader import readLHEF
from ROOT import TFile,TTree
from math import sqrt,log
from array import array
fileName=['pp_ttbar_semi1.lhe','pp_ttbar_semi2.lhe']
data=readLHEF(fileName[0])
output="tree_"+fileName[0].replace("lhe",'root')
file=TFile(output,'recreate')
parts_top=data.getParticlesByIDs([6]) # collect top by hepid  
parts_antitop=data.getParticlesByIDs([-6]) # collect antitop by hepid

tree=TTree("mytree","mytree")

M_tt=array('f',[0])
delta_rapidity=array('f',[0])
tree.Branch("M_tt_gen",M_tt,'M_tt/F')
tree.Branch("delta_rapidity_gen",delta_rapidity,'delta_rapidity/F')

i=0
for top, antitop in zip(parts_top,parts_antitop):
	M_tt[0]=(top.p4+antitop.p4).M()
	delta_rapidity[0]=top.p4.Rapidity()-antitop.p4.Rapidity()
	#M_tt[0]=sqrt((top.energy+antitop.energy)**2-(top.px+antitop.px)**2-(top.py+antitop.py)**2-(top.pz+antitop.pz)**2)
	#delta_rapidity[0]=0.5*log((top.energy+top.pz)/(top.energy-top.pz))-0.5*log((antitop.energy+antitop.pz)/(antitop.energy-antitop.pz))

	tree.Fill()
		
	i=i+1
	if i%10000==0:
		print ("M_tt:", M_tt[0])
		print ("delta_rapidity", delta_rapidity[0])
	
		
file.Write()
file.Close()
print(output+' has been created.')

