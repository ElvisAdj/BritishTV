"""test.py
"""

import unittest
from main import get_ports_and_protocols

class TestParser( unittest.TestCase ):

    def test_parse_for_random_pp_pairs( self ):
        self.assertEqual(
            str( get_ports_and_protocols( "ntp" ) ),
            "[{'udp': '123'}, {'tcp': '123'}]"
        )
        self.assertEqual(
            str( get_ports_and_protocols( "ftp" ) ),
            "[{'udp': '21'}, {'tcp': '21'}]"
        )

    # Your tests here...
    # def test_...( self ):

if __name__ == "__main__":
    unittest.main()
