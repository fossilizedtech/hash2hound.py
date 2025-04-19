import sys

'''
hash2hound.py

Author: FossilizedTech
Version: 0.1

Initial version TODO:
    Take 3 arguments
    1) users file
    2) cracked passwords
    3) output file
'''

def print_usage_message():
    print(" ")
    print(sys.argv[0])
    print("Usage: " + sys.argv[0] + " [DC_ACCOUNTS] [CRACKED_HASHES] [OUPUT_FILE]")
    print("File formats:")
    print("  [DC_ACCOUNTS] expected format is \"DOMAIN\\User:XXX:XXX:NTLM_Hash:::\"")
    print("  [CRACKED_HASHES] expected format is \"NTLM_Hash:Cracked_Plaintext_Password\"")
    print("  [OUPUT_FILE] format is \"DOMAIN\\User:NTLM_Hash:Plaintext_Password\"")
    print(" ")

# Check arguments
print_usage_message()

# Open files

# Iterate through users file looking for matches to cracked passwords

# Record to output file
