import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.UI.simple_ui import PrimeUI

if __name__ == "__main__":
   PrimeUI.run()

