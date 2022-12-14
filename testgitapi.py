import unittest

from gitapi import githubapi

class Testgithubapi(unittest.TestCase):
    def testGit(self):
        self.assertEqual(githubapi('?'), False)
    def testGit2(self):
        self.assertEqual(githubapi('Monicaprojects21'), True)
    def testGit3(self):
        self.assertEqual(githubapi('HW04'), False)
    def testGit4(self):
            self.assertEqual(githubapi('00'), True)


if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()
    """
    Monica Malamputti
SSW-567
Fall 2022
HW 04a: Develop with the Perspective of the Tester in mind
"""