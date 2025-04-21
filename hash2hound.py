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
    print(" ")
    print("File formats:")
    print("  [DC_ACCOUNTS] expected format is \"DOMAIN\\User:XXX:XXX:NTLM_Hash:::\"")
    print("  [CRACKED_HASHES] expected format is \"NTLM_Hash:Cracked_Plaintext_Password\"")
    print("  [OUPUT_FILE] format is \"DOMAIN\\User:NTLM_Hash:Plaintext_Password\"")
    print(" ")

# TODO: Finish sanity_check
def sanity_check():
    if len(sys.argv) == 4:

        # Check general [DC_ACCOUNTS] format
        try:
            # Check [DC_ACCOUNTS] file for existance
            file = open(sys.argv[1], "r")

            # Add portion that checks formating of data
            file.close

            # Add portion that also checks [CRACKED_HASHES]
            
            print(" ")
            print("[+] Sanity check PASSED")
            print(" ")
            return True

        except FileNotFoundError:
            print(" ") 
            print("[Error] Unable to open \"" + sys.argv[1] + "\" or " + sys.argv[2] + "\".") 
            print("[-----] Check that the files exists and that you have permission to read them.")
            print(" ")
            return False

        # Check [CRACKED_HASHES] format

    else:
        print_usage_message()
        return False

def send_it():
    print("Sending it!")

    # Add function to review cracked pw for duplicates
    # and only process each hash once

    with open(sys.argv[1], "r") as user_accounts:
        with open(sys.argv[2], "r") as cracked_hashes:
            with open(sys.argv[3], "w") as output_file:
                accounts = user_accounts.readlines()
                hashes = cracked_hashes.readlines()
                
                # Start with hashes to reduce number of iterations in cases
                # where multiple users have the same password
                for i in range(len(hashes)):    
                    hashes_current_line = hashes[i].split(':')

                    for x in range(len(accounts)):
                        accounts_current_line = accounts[i].split(':')

                        if hashes_current_line[0].strip() == accounts_current_line[3].strip():
                            print(hashes_current_line[0])
                        


                print(" This is where the magic happens")


# Initialize, check arguments, etc
if sanity_check() == True:
    send_it()

# Open files

# Iterate through users file looking for matches to cracked passwords

# Record to output file
