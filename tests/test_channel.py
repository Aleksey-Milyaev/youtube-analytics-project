from src.channel import Channel

chanel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

assert chanel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'

def test_print_info():
    assert chanel.print_info() == None