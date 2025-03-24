import os
import sys

# Absolute path to your project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from tracking_system.wsgi import application

app = application
