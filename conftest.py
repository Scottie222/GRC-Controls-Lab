import sys
import os

# Add the root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Add the Scripts directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Scripts')))
