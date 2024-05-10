import importlib.util
import os

class VersionUtil:
  def __init__(self):
    self.version = self._get_version_from_setup()

  def _get_version_from_setup(self):
    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to setup.py
    setup_file = os.path.join(parent_dir, "setup.py")

    # Use importlib to import the version information
    spec = importlib.util.spec_from_file_location("setup", setup_file)
    module = importlib.util.module_from_spec(spec)
    importlib.util.execute(module)

    return module.__version__
