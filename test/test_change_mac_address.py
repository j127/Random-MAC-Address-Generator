import app.change_mac_address as c


def test_dec_to_hex():
    assert c.dec_to_hex(0) == '0'
    assert c.dec_to_hex(1) == '1'
    assert c.dec_to_hex(3) == '3'
    assert c.dec_to_hex(10) == 'a'
    assert c.dec_to_hex(11) == 'b'
    assert c.dec_to_hex(12) == 'c'
    assert c.dec_to_hex(15) == 'f'

