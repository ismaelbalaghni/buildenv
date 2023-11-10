from pytest_multilog import TestHelper

from buildenv.__main__ import BuildEnvManager


class TestBuildEnvManager(TestHelper):
    def test_foo(self):
        # Just a fake test invoking setup
        m = BuildEnvManager(self.test_folder)
        m.setup()
