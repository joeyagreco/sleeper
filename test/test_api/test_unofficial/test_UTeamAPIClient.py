import unittest
from test.helper.helper_classes import MockResponse
from unittest import mock

from sleeper.api.unofficial import UTeamAPIClient
from sleeper.enum.nfl import NFLTeam
from sleeper.enum.Sport import Sport
from sleeper.model.nfl import NFLDepthChart


class TestUSTeamAPIClient(unittest.TestCase):
    @mock.patch("requests.get")
    def test_get_team_depth_chart_happy_path(self, mock_requests_get):
        mock_dict = {
            "WR3": ["1817", "8167"],
            "WR2": ["928", "7540", "8235"],
            "WR1": ["5185", "8121", "6223"],
            "TE": ["4602", "111", "7050"],
            "SS": ["2445", "5736", "6355"],
            "RT": ["5877", "8511"],
            "ROLB": ["5839", "8382"],
            "RILB": ["8266", "7782"],
            "RG": ["7702", "8460"],
            "RDE": ["3220", "8270"],
            "RCB": ["7628", "6333"],
            "RB": ["4199", "6828"],
            "QB": ["96", "6804"],
            "PK": ["59"],
            "NT": ["3186", "7818", "8344"],
            "NB": ["4136", "4223"],
            "LT": ["1521", "6008"],
            "LOLB": ["2343", "6965", "6981"],
            "LILB": ["3276", "7268"],
            "LG": ["6980", "8463"],
            "LDE": ["3295"],
            "LCB": ["4979", "7813"],
            "FS": ["6210", "8405"],
            "C": ["7645", "7132"],
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UTeamAPIClient.get_team_depth_chart(sport=Sport.NFL, team=NFLTeam.GB)

        self.assertIsInstance(response, NFLDepthChart)
        self.assertEqual(2, len(response.WR3))
        self.assertEqual("1817", response.WR3[0])
        self.assertEqual("8167", response.WR3[1])
        self.assertEqual(3, len(response.WR2))
        self.assertEqual("928", response.WR2[0])
        self.assertEqual("7540", response.WR2[1])
        self.assertEqual("8235", response.WR2[2])
        self.assertEqual(3, len(response.WR1))
        self.assertEqual("5185", response.WR1[0])
        self.assertEqual("8121", response.WR1[1])
        self.assertEqual("6223", response.WR1[2])
        self.assertEqual(3, len(response.TE))
        self.assertEqual("4602", response.TE[0])
        self.assertEqual("111", response.TE[1])
        self.assertEqual("7050", response.TE[2])
        self.assertEqual(3, len(response.SS))
        self.assertEqual("2445", response.SS[0])
        self.assertEqual("5736", response.SS[1])
        self.assertEqual("6355", response.SS[2])
        self.assertEqual(2, len(response.RT))
        self.assertEqual("5877", response.RT[0])
        self.assertEqual("8511", response.RT[1])
        self.assertEqual(2, len(response.ROLB))
        self.assertEqual("5839", response.ROLB[0])
        self.assertEqual("8382", response.ROLB[1])
        self.assertEqual(2, len(response.RILB))
        self.assertEqual("8266", response.RILB[0])
        self.assertEqual("7782", response.RILB[1])
        self.assertEqual(2, len(response.RG))
        self.assertEqual("7702", response.RG[0])
        self.assertEqual("8460", response.RG[1])
        self.assertEqual(2, len(response.RDE))
        self.assertEqual("3220", response.RDE[0])
        self.assertEqual("8270", response.RDE[1])
        self.assertEqual(2, len(response.RCB))
        self.assertEqual("7628", response.RCB[0])
        self.assertEqual("6333", response.RCB[1])
        self.assertEqual(2, len(response.RB))
        self.assertEqual("4199", response.RB[0])
        self.assertEqual("6828", response.RB[1])
        self.assertEqual(2, len(response.QB))
        self.assertEqual("96", response.QB[0])
        self.assertEqual("6804", response.QB[1])
        self.assertEqual(1, len(response.PK))
        self.assertEqual("59", response.PK[0])
        self.assertEqual(3, len(response.NT))
        self.assertEqual("3186", response.NT[0])
        self.assertEqual("7818", response.NT[1])
        self.assertEqual("8344", response.NT[2])
        self.assertEqual(2, len(response.NB))
        self.assertEqual("4136", response.NB[0])
        self.assertEqual("4223", response.NB[1])
        self.assertEqual(2, len(response.LT))
        self.assertEqual("1521", response.LT[0])
        self.assertEqual("6008", response.LT[1])
        self.assertEqual(3, len(response.LOLB))
        self.assertEqual("2343", response.LOLB[0])
        self.assertEqual("6965", response.LOLB[1])
        self.assertEqual("6981", response.LOLB[2])
        self.assertEqual(2, len(response.LILB))
        self.assertEqual("3276", response.LILB[0])
        self.assertEqual("7268", response.LILB[1])
        self.assertEqual(2, len(response.LG))
        self.assertEqual("6980", response.LG[0])
        self.assertEqual("8463", response.LG[1])
        self.assertEqual(1, len(response.LDE))
        self.assertEqual("3295", response.LDE[0])
        self.assertEqual(2, len(response.LCB))
        self.assertEqual("4979", response.LCB[0])
        self.assertEqual("7813", response.LCB[1])
        self.assertEqual(2, len(response.FS))
        self.assertEqual("6210", response.FS[0])
        self.assertEqual("8405", response.FS[1])
        self.assertEqual(2, len(response.C))
        self.assertEqual("7645", response.C[0])
        self.assertEqual("7132", response.C[1])
