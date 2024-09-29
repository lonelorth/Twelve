import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = Runner.Runner("John")
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run1 = Runner.Runner("Igor")
        for i in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    def test_challenge(self):
        run2 = Runner.Runner("Rebek")
        run3 = Runner.Runner("Bijok")
        for i in range(10):
            run2.walk()
            run3.run()
        self.assertNotEqual(run2.distance, run3.distance)

if __name__ == "__main__":
    unittest.main()