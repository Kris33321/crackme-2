from ctypes import c_uint32

state = [0x7314C98C, 0xB67CF39D, 0xAED52F4A]
rounds = 0x0D74

for _ in range(rounds):

    x = c_uint32((state[2] + 1124726242) ^ (state[0] ^ 0x4B0871CD)).value
    y = c_uint32(((state[0] ^ 0x4B0871CD) - 303758136) ^ (x >> 3)).value

    next_B = c_uint32(((state[1] ^ 0x94A3A219) - y) ^ 0).value
    next_A = c_uint32((x + 840651798) ^ next_B).value
    next_C = c_uint32(((y - 0) ^ x) - 471526675).value

    state = [next_A, next_B, next_C]

flag = f"{state[0]:08X}-{state[1]:08X}-{state[2]:08X}-{rounds:08X}"
print(flag)
