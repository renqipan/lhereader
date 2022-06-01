from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TFile
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
	i=0
	for p in parts_higgs:
		higgs_pt.Fill(p.pt)
		higgs_eta.Fill(p.eta)
		i=i+1
		if i%10000==0:
			print "pt:",p.pt
	for p in parts_pho:
		photon_pt.Fill(p.pt)
		photon_eta.Fill(p.eta)
	file.Write()
	print(output+'has been created.')



                           