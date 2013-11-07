from dimuon import *
from nose.tools import *

class DummyParticle:
    def __init__(self, qpt):
        self.qpt = qpt

def test_zero_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs) == 0

def test_one_particle():
    particles = [None]
    pairs = find_pairs(particles)
    assert_equal(len(pairs), 0)

def test_two_opposite():
    pos = DummyParticle(+1)
    neg = DummyParticle(-1)
    particles = [pos, neg]
    pairs = find_pairs(particles)
    assert_equal(len(pairs), 1)

def test_two_like_sign():
    pos1 = DummyParticle(+1)
    pos2 = DummyParticle(+1)
    particles = [pos1, pos2]
    pairs = find_pairs(particles)
    assert_equal(len(pairs), 0)
