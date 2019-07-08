import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from magellan import *
import json

set('macTable', json.dumps({'00:00:00:00:00:00': '1'}))