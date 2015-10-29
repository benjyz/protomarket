from scantx import *

issuetx = 'b25ba9cb3a02e24dc53f6672a25fdc047d243cc442dda5e25d5d1590d9a66969'
transfertx = '9a0466b49bc91007767caf478d9aa8e91ce04c9d0c0aae3023ed0f9bc7e567bb'

printtx(transfertx)

"""
# example tx with op_return
#tuples of (opcode, data, sop_idx) so that the different possible
#PUSHDATA encodings can be accurately distinguished

(106, None, 0)
(18, 'OA\x01\x00\x02\x80\xd6\xa3\xf8\x1b\xe0\x90\x82\xf7\xa4\xeb\x02\x00', 1)
(118, None, 0)
(169, None, 1)
(20, '\x08\xcf7lN\x8e\xd01&}\xf2\xe5\xfax\xdf\xe9XxP\x8b', 2)
(136, None, 23)
(172, None, 24)
(118, None, 0)
(169, None, 1)
(20, '4\rx\xfc\x9e\x8b7\x94)\x87\xc3/\xd0\x98\x8b\x907<L\xd1', 2)
(136, None, 23)
(172, None, 24)
(118, None, 0)
(169, None, 1)
(20, '4\rx\xfc\x9e\x8b7\x94)\x87\xc3/\xd0\x98\x8b\x907<L\xd1', 2)
(136, None, 23)
(172, None, 24)
"""
