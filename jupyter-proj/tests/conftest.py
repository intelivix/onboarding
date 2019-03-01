from pathlib import Path
import sys

package_path = str(Path(__file__).parent.parent)
sys.path.insert(0, package_path)
