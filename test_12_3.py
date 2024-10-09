import runner
import runner_and_tournament
import unittest


def frozen_test(func):
    def decor(self):
        if self.is_frozen:
            print("Тесты в этом кейсе заморожены.")
            self.skipTest('Тесты заморожены')
        return func(self)
    return decor


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_test
    def test_walk(self,):
        run_1 = runner.Runner("Walker")
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @frozen_test
    def test_run(self):
        run_2 = runner.Runner("Runner")
        for i in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    @frozen_test
    def test_challenge(self):
        runner1 = runner.Runner("Runner1")
        runner2 = runner.Runner("Runner2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    @frozen_test
    def test_1(self):
            first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
            result = first_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

    @frozen_test
    def test_2(self):
            second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
            result = second_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

    @frozen_test
    def test_3(self):
            third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nik)
            result = third_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()