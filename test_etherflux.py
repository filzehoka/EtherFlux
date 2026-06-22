# test_etherflux.py
"""
Tests for EtherFlux module.
"""

import unittest
from etherflux import EtherFlux

class TestEtherFlux(unittest.TestCase):
    """Test cases for EtherFlux class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherFlux()
        self.assertIsInstance(instance, EtherFlux)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherFlux()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
