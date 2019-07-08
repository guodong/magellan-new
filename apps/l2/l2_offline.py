import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from magellan import *
import json
from zoe1 import for_Dong #this function ruturn a dict{switchid{inner_portid:outportset}}

set('macTable', json.dumps({'00:00:00:00:00:00': '1'}))
