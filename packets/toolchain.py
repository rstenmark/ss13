def dict_to_packet(d: dict) -> str:
    '''Converts a python dictionary to an arbitrary SS13 packet string'''
    ret = ''
    for k, v in d.items():
        ret += f'{k}={v}|n'
    return ret[:-2]

def save_pkt(packet, name) -> str:
    return f'echo {packet}^ /mnt/term{name}'

def broadcast(packet, frequency=1411) -> str:
    '''Wraps a packet in a echo pipe to /mnt/radio/[frequency]
    to broadcast it from the mainframe radio'''
    return f'echo {packet}^ /mnt/radio/{frequency}/p'
    
def pda_msg(message, sender_name, sender_assignment):
    return broadcast(
        dict_to_packet({
            "command": "text_message",
            "message": message,
            "sender_name": sender_name,
            "sender_assignment": sender_assignment
        }),
        frequency=1149)

def pnet_pwr_cntrl():
    pass

def dor_airlock_ctl(address_1: str, access_code: int, command: str):
    '''Generates a DOR_AIRLOCK control packet, broadacasted on 141.1'''
    ret = ''
    # Assure address is 8 chars long
    assert len(address_1) == 8
    # Assure command is valid
    assert command in set(
        ('open', 'close', 'lock', 'unlock', 'secure_open', 'secure_close'))
    return broadcast(
        dict_to_packet({
                'address_1': address_1,
                'access_code': access_code,
                'command': command
        }),
        frequency=1411)
