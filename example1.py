from lhereader import readLHEF  
from ROOT import TCanvas, TH1F  

#data=readLHEF('unweighted_events.lhe')  
data=readLHEF('gammatogammaH.lhe')  
parts=data.getParticlesByIDs([25]) # collect particles by hepid  
c=TCanvas()  
hist=TH1F("pt", "Pt of Higgs",100,0,1000)  
for p in parts:  
  hist.Fill(p.pt)  
hist.Draw()  
c.SaveAs("pt_higgs.png") 
