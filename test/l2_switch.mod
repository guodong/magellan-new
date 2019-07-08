Interface: Model(
    unit: Number,
    slot: Number,
    port: Number,
    speed: Number
)

PortType: Enum(NORMAL, LAG)

Port: Model(
    name: String,
    type: PortType
)

NormalPort: Port(
    type: PortType.NORMAL,
    interface: Interface
)

LagPort: Port(
    type: PortType.LAG,
    interfaces: Set(Interface)
)

MacTable: Map(Bit(48), Model(
    port: Port,
    timestamp: Timestamp
))

Switch: Model(
    macTable: MacTable,
    macTableTimeout: Number,
    ports: Set(Port),
    timer: Timer,
    packet: Optional(Packet, Null).change(on_packet)
)

Network: NetworkModel(
    switches: Set(Switch),
    links: Set(Link)
)

def on_packet(packet):
    switch = packet.model.parent()
