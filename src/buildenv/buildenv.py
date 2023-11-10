from pathlib import Path


class BuildEnvManager:
    """
    **buildenv** tool manager entry point

    :param project_path: Path to the current project root folder
    """

    def __init__(self, project_path: Path):
        pass

    def setup(self):
        """
        Build environment setup.

        This will:
        * prepare extra venv shell scripts folder
        * invoke extra environment initializers defined by sub-classes
        """
        pass
