# Read events and create histogram of dimuon masses

from ROOT import TFile

file_data = TFile("/home/waugh/data/events.root")
tree_data = file_data.Get("events")
