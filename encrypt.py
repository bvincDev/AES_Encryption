# encrypt.py

# S-box for SubBytes step (256-byte lookup table)
S_BOX = [
    # 256 values go here...
    
]

# Round constant for key expansion
R_CON = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    # ...
]

# --- Utility functions ---
def sub_bytes(state):
    """Substitute bytes using AES S-box."""
    # replace each byte with S_BOX[value]
    return [[S_BOX[byte] for byte in row] for row in state]

def shift_rows(state):
    """Cyclically shift rows of the state."""
    new_state = [row[:] for row in state]
    new_state[1] = new_state[1][1:] + new_state[1][:1]
    new_state[2] = new_state[2][2:] + new_state[2][:2]
    new_state[3] = new_state[3][3:] + new_state[3][:3]
    return new_state

def mix_columns(state):
    """Mix columns using Galois field multiplication."""
    # multiply columns by the AES matrix [2,3,1,1]
    # implement GF(2^8) multiplication manually
    pass

def add_round_key(state, round_key):
    """XOR the state with the round key."""
    return [[s ^ k for s, k in zip(row_s, row_k)] for row_s, row_k in zip(state, round_key)]

def key_expansion(key):
    """Generate round keys from original key."""
    # AES key expansion algorithm
    pass

def encrypt_block(plaintext_block, key):
    """Encrypt one 16-byte block."""
    state = bytes_to_matrix(plaintext_block)
    round_keys = key_expansion(key)

    # Initial round
    state = add_round_key(state, round_keys[0])

    # 9 main rounds
    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])

    # Final round
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])

    return matrix_to_bytes(state)

# --- Helpers to convert between bytes and matrices ---
def bytes_to_matrix(text):
    """Convert 16-byte array into 4x4 matrix."""
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix_to_bytes(matrix):
    """Convert 4x4 matrix back to bytes."""
    return bytes(sum(matrix, []))
