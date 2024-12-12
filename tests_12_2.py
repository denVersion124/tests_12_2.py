import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner_usain = Runner ("Усэйн", 10)
        self.runner_andrey = Runner ("Андрей", 9)
        self.runner_nik = Runner ("Ник", 3)
    @classmethod
    def tearDownClass (cls):
        for key, value in sorted (cls.all_results.items ()):
            print (f"{key}: {value}")

    def test_tournament_usain_nik(self):
        tournament = Tournament (90, self.runner_usain, self.runner_nik)
        results = tournament.start ()
        TournamentTest.all_results[1] = {poz: runner.name for poz, runner in results.items()}

        self.assertTrue (results[max (results.keys ())].name == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament (90, self.runner_andrey, self.runner_nik)
        results = tournament.start ()
        TournamentTest.all_results[2] = {poz: runner.name for poz, runner in results.items()}

        self.assertTrue (results[max (results.keys ())].name == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament (90, self.runner_usain, self.runner_andrey, self.runner_nik)
        results = tournament.start ()
        TournamentTest.all_results[3] = {poz: runner.name for poz, runner in results.items()}

        self.assertTrue (results[max (results.keys ())].name == "Ник")


if __name__ == '__main__':
    unittest.main()