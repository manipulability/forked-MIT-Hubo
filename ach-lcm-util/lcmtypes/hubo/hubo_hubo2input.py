"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class hubo_hubo2input(object):
    __slots__ = ["timestamp", "motors"]

    def __init__(self):
        self.timestamp = 0
        self.motors = [ 0.0 for dim0 in range(42) ]

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(hubo_hubo2input._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        buf.write(struct.pack('>42d', *self.motors[:42]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != hubo_hubo2input._get_packed_fingerprint():
            raise ValueError("Decode error")
        return hubo_hubo2input._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = hubo_hubo2input()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        self.motors = struct.unpack('>42d', buf.read(336))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if hubo_hubo2input in parents: return 0
        tmphash = (0x191403211f3b4867) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if hubo_hubo2input._packed_fingerprint is None:
            hubo_hubo2input._packed_fingerprint = struct.pack(">Q", hubo_hubo2input._get_hash_recursive([]))
        return hubo_hubo2input._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

