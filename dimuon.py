# Read events and create histogram of dimuon masses

from ROOT import TFile

file_data = TFile("/home/waugh/data/events.root")
tree_data = file_data.Get("events")
n_events = tree_data.GetEntries()
for i_event in xrange(n_events):
    tree_data.GetEntry(i_event)
    n_particles = tree_data.nPart
    print n_particles
