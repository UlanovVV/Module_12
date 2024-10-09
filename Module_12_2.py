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
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    def test_1(self):
            first_run = Tournament(90, self.usain, self.nik)
            result = first_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

    def test_2(self):
            second_run = Tournament(90, self.andrey, self.nik)
            result = second_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

    def test_3(self):
            third_run = Tournament(90, self.andrey, self.usain, self.nik)
            result = third_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()