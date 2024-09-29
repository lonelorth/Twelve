from tests_12_3 import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

if __name__ == '__main__':
    unittest.main()