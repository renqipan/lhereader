from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TFile
from math import sqrt,log
fileName=['pp_ttbar.lhe','pp_ttbar_nlo.lhe']
for i in range(0,2): 
	data=readLHEF(fileName[i])
	output=fileName[i].replace("lhe",'root')
	file=TFile(output,'recreate')
	parts_top=data.getParticlesByIDs([6]) # collect particles by hepid  
	parts_antitop=data.getParticlesByIDs([-6]) # collect particles by hepid  

	top_pt=TH1F("top_pt", "Pt of top",100,0,1000)
	top_eta=TH1F("top_eta", "Eta of top",100,-5,5)
	antitop_pt=TH1F("antitop_pt", "Pt of antitop",100,0,1000)
	antitop_eta=TH1F("antitop_eta", "Eta of antitop",100,-5,5)
	delta_phi=TH1F("delta_phi","delta phi between top and antitop",100,0,2*3.14)
	inv_mass=TH1F("M_tt","invariant mass ",50,0,1000)
	delta_eta=TH1F("delta_eta","delta Eta between top and antitop",50,-5,5)
	delta_rapidity=TH1F("delta_rapidity","rapidity difference of top and antitop",50,-5,5)
	i=0
	for top, antitop in zip(parts_top,parts_antitop):
		top_pt.Fill(top.pt)
		top_eta.Fill(top.eta)
		antitop_pt.Fill(antitop.pt)
		antitop_eta.Fill(antitop.eta)
		deltaPhi=abs(top.phi-antitop.phi ) #define delta phi
		delta_phi.Fill(deltaPhi)
		invariant_mass=sqrt((top.energy+antitop.energy)**2-(top.px+antitop.px)**2-(top.py+antitop.py)**2-(top.pz+antitop.pz)**2)
		inv_mass.Fill(invariant_mass)
		deltaEta=top.eta-antitop.eta
		delta_eta.Fill(deltaEta)
		top_rapidity=0.5*log((top.energy+top.pz)/(top.energy-top.pz))
		antitop_rapidity=0.5*log((antitop.energy+antitop.pz)/(antitop.energy-antitop.pz))
		diff_rapidity=top_rapidity-antitop_rapidity
		delta_rapidity.Fill(diff_rapidity)
		i=i+1
		if i%1000==0:
			print "top mass:",top.mass
			print "antitop phi",antitop.phi
		
	file.Write()
	print(output+'has been created.')



                           
