from lhereader import readLHEF
from ROOT import TFile,TTree
from math import sqrt,log
from array import array
fileName=['gammatogammaH.lhe','gammatogammaHminus.lhe','ZtogammaH.lhe','ZtogammaHminus.lhe']
for i in range(0,4): 
	data=readLHEF('../JHUGenerator/'+fileName[i])
	output="tree_"+fileName[i].replace("lhe",'root')
	file=TFile(output,'recreate')
	parts_higgs=data.getParticlesByIDs([25]) # collect higgs by hepid  
	parts_pho=data.getParticlesByIDs([22]) # collect photon by hepid  
	tree=TTree("mytree","mytree")

	photon_eta=array('f',[0])
	photon_pt=array('f',[0])
	higgs_eta=array('f',[0])
	higgs_pt=array('f',[0])
	delta_eta=array('f',[0])
	M_gammah=array('f',[0])

	higgs_px=array('f',[0])
	higgs_py=array('f',[0])
	higgs_pz=array('f',[0])
	higgs_energy=array('f',[0])
	photon_px=array('f',[0])
	photon_py=array('f',[0])
	photon_pz=array('f',[0])
	photon_energy=array('f',[0])

	tree.Branch("higgs_pt",higgs_pt,'higgs_pt/F')
	tree.Branch("higgs_eta",higgs_eta,'higgs_eta/F')
	tree.Branch("photon_pt",photon_pt,'photon_pt/F')
	tree.Branch("photon_eta",photon_eta,'photon_eta/F')
	tree.Branch("delta_eta",delta_eta,'delta_eta/F')
	tree.Branch("M_gammah",M_gammah,'M_gammah/F')

	tree.Branch("photon_px",photon_px,'photon_px/F')
	tree.Branch("photon_py",photon_py,'photon_py/F')
	tree.Branch("photon_pz",photon_pz,'photon_pz/F')
	tree.Branch("photon_energy",photon_energy,'photon_energy/F')
	tree.Branch("higgs_px",higgs_px,'higgs_px/F')
	tree.Branch("higgs_py",higgs_py,'higgs_py/F')
	tree.Branch("higgs_pz",higgs_pz,'higgs_pz/F')
	tree.Branch("higgs_energy",higgs_energy,'higgs_energy/F')
	i=0
	for higgs, photon in zip(parts_higgs,parts_pho):
		higgs_eta[0]=higgs.eta
		higgs_pt[0]=higgs.pt
		photon_eta[0]=photon.eta
		photon_pt[0]=photon.pt
		M_gammah[0]=sqrt((higgs.energy+photon.energy)**2-(higgs.px+photon.px)**2-(higgs.py+photon.py)**2-(higgs.pz+photon.pz)**2)
		delta_eta[0]=higgs.eta-photon.eta
		
		photon_px[0]=photon.px
		photon_py[0]=photon.py
		photon_pz[0]=photon.pz
		photon_energy[0]=photon.energy
		higgs_px[0]=higgs.px
		higgs_py[0]=higgs.py
		higgs_pz[0]=higgs.pz
		higgs_energy[0]=higgs.energy
		
		tree.Fill()
		
		i=i+1
		if i%10000==0:
			print "higgs mass:", higgs.mass
			print "photon phi", photon.phi
		
	file.Write()
	file.Close()
	print(output+' has been created.')

