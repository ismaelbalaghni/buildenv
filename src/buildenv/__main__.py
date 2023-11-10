from pathlib import Path

from buildenv.buildenv import BuildEnvManager

if __name__ == "__main__":  # pragma: no cover
    # Invoke build env manager on current project directory
    BuildEnvManager(Path.cwd()).setup()
