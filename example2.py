from lhereader import readLHEF  
from ROOT import TCanvas, TH1F  
fileName=['ZtogammaH.lhe','ZtogammaHminus.lhe','gammatogammaH.lhe','gammatogammaHminus.lhe']
c=TCanvas()  
for i in range(0,4):
	data=readLHEF('../JHUGenerator/'+fileName[i])  
	parts=data.getParticlesByIDs([25]) # collect particles by hepid
	hist=TH1F("pt"+str(i), "Pt of Higgs",100,0,1000)  
	for p in parts:  
		hist.Fill(p.pt)  
  	if i==0:
		hist.Draw("hist")  
	else:
		hist.Draw("samehist")
c.SaveAs("pt_higgs.png") 
