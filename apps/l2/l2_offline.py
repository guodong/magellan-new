import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from magellan import *
import json
from zoe1.Magellan_STP_Zoe import for_Dong #this function ruturn a dict{switchid{inner_portid:outportset}}

set('macTable', json.dumps({'00:00:00:00:00:00': '1'}))
set('STP', json.dumps(for_Dong()[1]))
print(for_Dong())