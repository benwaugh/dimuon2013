'''
Read events and create histogram of dimuon masses

So far just prints numbers of particles to screen.
'''

from ROOT import TFile, TH1F

def tree_from_file(filename):
    '''
    Return tree "events" from given file.
    '''
    global file_data
    file_data = TFile(filename)
    tree_data = file_data.Get("events")
    return tree_data

def dimuon_mass_histo(tree):
    hist = TH1F()
    return hist

if __name__ == '__main__':
    tree_data = tree_from_file("/home/waugh/data/events.root")   
    n_events = tree_data.GetEntries()
    for i_event in xrange(n_events):
        tree_data.GetEntry(i_event)
        n_particles = tree_data.nPart
        print n_particles
    hist = dimuon_mass_histo(tree_data)
    hist.Draw()
    raw_input("Press return to exit")
