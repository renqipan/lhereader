# lhereader
A Python module to read LHE (Les Houches Event) file and access the event information in an object oriented way.
Requires ROOT (root.cern.ch) and pyroot as external dependencies.

Sample code to use this module -

from lhereader import readLHEF
from ROOT import TCanvas, TH1F

data=readLHEF('unweighted_events.lhe')
parts=data.getParticlesByIDs([5,-5]) # collect all botom and anti-bottom quarks
c=TCanvas()
hist=TH1F("pt", "Pt of b/#bar{b}",100,0,1000)
for p in parts:
  hist.Fill(p.pt)
hist.Draw()
c.SaveAs("pt_b_bbar.png")
