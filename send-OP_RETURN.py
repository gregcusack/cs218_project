# send-OP_RETURN.py
#
# CLI wrapper for OP_RETURN.py to send bitcoin with OP_RETURN metadata
#
# Copyright (c) Coin Sciences Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys, string
from OP_RETURN import *

if len(sys.argv) < 4:
    sys.exit(
      '''Usage:
      python send-OP_RETURN.py <send-address> <send-amount> <metadata> <testnet (optional)>

      <send-address> is the peercoin address of the recipient
      <send-amount> is the amount to send (in units of PPC)
      <metadata> is a hex string or raw string containing the OP_RETURN metadata
                (auto-detection: treated as a hex string if it is a valid one)
      <testnet> should be 1 to use the peercoin testnet, otherwise it can be omitted

      Examples:
      python send-OP_RETURN.py PCrtba6CAGBB7ztsVGhrAnCs6hvt4t6Pep 0.001 'Hello, blockchain!'
      python send-OP_RETURN.py PCrtba6CAGBB7ztsVGhrAnCs6hvt4t6Pep 0.001 48656c6c6f2c20626c6f636b636861696e21
      python send-OP_RETURN.py mzEJxCrdva57shpv62udriBBgMECmaPce4 0.001 'Hello, testnet blockchain!' 1'''
    )

dummy, send_address, send_amount, metadata = sys.argv[0:4]

metadata_from_hex = OP_RETURN_hex_to_bin(metadata)
if metadata_from_hex is not None:
    metadata=metadata_from_hex

result = OP_RETURN_send(send_address, float(send_amount), metadata)

if 'error' in result:
    print('Error: '+result['error'])
