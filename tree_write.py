from lhereader import readLHEF
from ROOT import TFile,TTree
from math import sqrt,log
from array import array
fileName=['pp_ttbar.lhe','pp_ttbar_nlo.lhe']
for i in range(0,2): 
	data=readLHEF(fileName[i])
	output="tree_"+fileName[i].replace("lhe",'root')
	file=TFile(output,'recreate')
	parts_top=data.getParticlesByIDs([6]) # collect top by hepid  
	parts_antitop=data.getParticlesByIDs([-6]) # collect antitop by hepid  
	tree=TTree("mytree","mytree")

	antitop_eta=array('f',[0])
	antitop_pt=array('f',[0])
	top_eta=array('f',[0])
	top_pt=array('f',[0])
	delta_eta=array('f',[0])
	M_tt=array('f',[0])

	top_px=array('f',[0])
	top_py=array('f',[0])
	top_pz=array('f',[0])
	top_energy=array('f',[0])
	antitop_px=array('f',[0])
	antitop_py=array('f',[0])
	antitop_pz=array('f',[0])
	antitop_energy=array('f',[0])
	delta_rapidity=array('f',[0])

	tree.Branch("top_pt",top_pt,'top_pt/F')
	tree.Branch("top_eta",top_eta,'top_eta/F')
	tree.Branch("antitop_pt",antitop_pt,'antitop_pt/F')
	tree.Branch("antitop_eta",antitop_eta,'antitop_eta/F')
	tree.Branch("delta_eta",delta_eta,'delta_eta/F')
	tree.Branch("M_tt",M_tt,'M_tt/F')

	tree.Branch("antitop_px",antitop_px,'antitop_px/F')
	tree.Branch("antitop_py",antitop_py,'antitop_py/F')
	tree.Branch("antitop_pz",antitop_pz,'antitop_pz/F')
	tree.Branch("antitop_energy",antitop_energy,'antitop_energy/F')
	tree.Branch("top_px",top_px,'top_px/F')
	tree.Branch("top_py",top_py,'top_py/F')
	tree.Branch("top_pz",top_pz,'top_pz/F')
	tree.Branch("top_energy",top_energy,'top_energy/F')
	tree.Branch("delta_rapidity",delta_rapidity,'delta_rapidity/F')
	i=0
	for top, antitop in zip(parts_top,parts_antitop):
		top_eta[0]=top.eta
		top_pt[0]=top.pt
		antitop_eta[0]=antitop.eta
		antitop_pt[0]=antitop.pt
		M_tt[0]=sqrt((top.energy+antitop.energy)**2-(top.px+antitop.px)**2-(top.py+antitop.py)**2-(top.pz+antitop.pz)**2)
		delta_eta[0]=top.eta-antitop.eta
		
		antitop_px[0]=antitop.px
		antitop_py[0]=antitop.py
		antitop_pz[0]=antitop.pz
		antitop_energy[0]=antitop.energy
		top_px[0]=top.px
		top_py[0]=top.py
		top_pz[0]=top.pz
		top_energy[0]=top.energy
		delta_rapidity[0]=0.5*log((top.energy+top.pz)/(top.energy-top.pz))-0.5*log((antitop.energy+antitop.pz)/(antitop.energy-antitop.pz))
		tree.Fill()
		
		i=i+1
		if i%10000==0:
			print "top mass:", top.mass
			print "antitop phi", antitop.phi
		
	file.Write()
	file.Close()
	print(output+' has been created.')

