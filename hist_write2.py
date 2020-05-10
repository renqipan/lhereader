from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TFile
from math import sqrt,log
fileName=['gammatogammaH.lhe','gammatogammaHminus.lhe','ZtogammaH.lhe','ZtogammaHminus.lhe']
for i in range(0,4): 
	data=readLHEF('../JHUGenerator/'+fileName[i])
	output=fileName[i].replace("lhe",'root')
	file=TFile(output,'recreate')
	parts_higgs=data.getParticlesByIDs([25]) # collect particles by hepid  
	parts_pho=data.getParticlesByIDs([22]) # collect particles by hepid  

	higgs_pt=TH1F("h_pt", "Pt of Higgs",100,0,1000)
	higgs_eta=TH1F("h_eta", "Eta of Higgs",100,-5,5)
	photon_pt=TH1F("ph_pt", "Pt of photon",100,0,1000)
	photon_eta=TH1F("ph_eta", "Eta of photon",100,-5,5)
	delta_phi=TH1F("delta_phi","delta phi between Higgs and photon",100,0,2*3.14)
	inv_mass=TH1F("M_gammah","invariant mass ",100,0,1000)
	delta_eta=TH1F("delta_eta","delta Eta between Higgs and photon",100,-5,5)
	gammah_rapidity=TH1F("gammah_rapidity","rapidity of gammaH system",100,-5,5)
	i=0
	for higgs, photon in zip(parts_higgs,parts_pho):
		higgs_pt.Fill(higgs.pt)
		higgs_eta.Fill(higgs.eta)
		photon_pt.Fill(photon.pt)
		photon_eta.Fill(photon.eta)
		deltaPhi=abs(higgs.phi-photon.phi ) #define delta phi
		delta_phi.Fill(deltaPhi)
		invariant_mass=sqrt((higgs.energy+photon.energy)**2-(higgs.px+photon.px)**2-(higgs.py+photon.py)**2-(higgs.pz+photon.pz)**2)
		inv_mass.Fill(invariant_mass)
		deltaEta=higgs.eta-photon.eta
		delta_eta.Fill(deltaEta)
		rapidity_gammah=0.5*log((higgs.energy+photon.energy+higgs.pz+photon.pz)/(higgs.energy+photon.energy-higgs.pz-photon.pz))
		gammah_rapidity.Fill(rapidity_gammah)
		i=i+1
		if i%10000==0:
			print "higgs mass:",higgs.mass
			print "photon phi",photon.phi
		
	file.Write()
	print(output+'has been created.')



                           
