import magellan as mg

g_mac_table = mg.Map(mg.Str, mg.Map(mg.Str, mg.Int))
g_stp = mg.Map(mg.Str, mg.Arr(mg.Int))

model MacTable {

}


def on_packet(pkt):
    g_mac_table[pkt.switch][pkt.eth.src] = pkt.in_port
    if pkt.eth.dst in g_mac_table[pkt.switch]:
        return g_mac_table[pkt.switch][pkt.eth.dst]
    else:
        return g_stp[pkt.switch]
    pass


def on_event(evt):
    pass


mg.on_packet(on_packet)
mg.on_event(on_event)


def abc():
    pass