import xml.etree.ElementTree as ET
from ROOT import TLorentzVector

class Particle:
    def __init__(self,pdgid,status,spin,mother1,mother2,gmother1,gmother2,px=0,py=0,pz=0,energy=0,mass=0):
        self.pdgid=pdgid
        self.px=px
        self.py=py
        self.pz=pz
        self.energy=energy
        self.mass=mass
        self.spin=spin
        self.mother1=mother1
        self.mother2=mother2
        self.gmother1=gmother1
        self.gmother2=gmother2
        self.status=status    
    
    @property
    def p4(self):
        return TLorentzVector(self.px,self.py,self.pz,self.energy)
    
    @p4.setter
    def p4(self,value):
        self.px=value.Px()
        self.py=value.Py()
        self.pz=value.Pz()
        self.energy=value.E()
        self.mass=value.M()
    
    @property
    def p(self):
        return self.p4.P()
    
    @property
    def eta(self):
        return self.p4.Eta()
    
    @property
    def pt(self):
        return self.p4.Pt()
    
    @property
    def phi(self):
        return self.p4.Phi()

    @property
    def Costheta(self):
        return self.p4.CosTheta()
    
class Event:
    def __init__(self,num_particles):
        self.num_particles=num_particles
        self.particles=[]
    
    def __addParticle__(self,particle):
        self.particles.append(particle)
        
    def getParticlesByIDs(self,idlist):
        partlist=[]
        for pdgid in idlist:
            for p in self.particles:
                if p.pdgid==pdgid:
                    partlist.append(p)
        return partlist

class LHEFData:
    def __init__(self,version):
        self.version=version
        self.events=[]
    
    def __addEvent__(self,event):
        self.events.append(event)
        
    def getParticlesByIDs(self,idlist):
        partlist=[]
        for event in self.events:
            partlist.extend(event.getParticlesByIDs(idlist))
        return partlist
        

def readLHEF(name):
    tree = ET.parse(name)
    root=tree.getroot()
    lhefdata=LHEFData(float(root.attrib['version']))
    for child in root:
        if(child.tag=='event'):
            lines=child.text.strip().split('\n')
            event_header=lines[0].strip()
            num_part=int(event_header.split()[0].strip())
            e=Event(num_part)
            for i in range(1,num_part+1):
                part_data=lines[i].strip().split()
                mother1_index=int(part_data[2])
                mother2_index=int(part_data[3])
                if mother1_index==0:
                    mother1=0
                    mother2=0
                    gmother1=0
                    gmother2=0
                else:
                    mother1=lines[mother1_index].strip().split()[0]
                    mother2=lines[mother2_index].strip().split()[0]
                    grand1_index=int(lines[mother1_index].strip().split()[2])
                    grand2_index=int(lines[mother1_index].strip().split()[3])
                    if grand1_index==0:
                        gmother1=0
                        gmother2=0
                    else:
                        gmother1=lines[grand1_index].strip().split()[0]
                        gmother2=lines[grand2_index].strip().split()[0]

                p=Particle(int(part_data[0]),int(part_data[1]), float(part_data[12]),int(mother1),int(mother2),int(gmother1),int(gmother2), float(part_data[6]), float(part_data[7]), float(part_data[8]), float(part_data[9]), float(part_data[10]))
                e.__addParticle__(p)
            lhefdata.__addEvent__(e)
    
    return lhefdata
