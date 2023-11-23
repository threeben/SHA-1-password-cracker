import hashlib

top_10000_passwords = []


def crack_sha1_hash(hash, use_salts=False):
    # Read each password from 'top-10000-passwords.txt' and store it into
    # top_10000_passwords array
    with open('top-10000-passwords.txt', 'r') as passwords_file:
        Lines = passwords_file.readlines()
        for line in Lines:
            top_10000_passwords.append(line.strip())

    hashed_passwords = {}

    # Hash each password in top_10000_passwords array,
    # store hashed password as key and original password as value
    # into the hashed_passwords dictionary for hash lookup
    for password in top_10000_passwords:
        encoded_password = password.encode()

        if not use_salts:
            hashed_password = hashlib.sha1(encoded_password).hexdigest()
            hashed_passwords[hashed_password] = password
            continue

        # If use_salts is true, read each salt from 'known-salts.txt'
        with open('known-salts.txt', 'r') as salts_file:
            Lines = salts_file.readlines()

            for line in Lines:
                salt = line.strip()
                encoded_salt = salt.encode()
                # Prepend and append salt to password respectively
                encoded_passwords_with_salt = [
                    encoded_salt + encoded_password, encoded_password + encoded_salt]
                # Hash the prefixed/suffixed passwords and add the
                # hashed results to the dictionary
                for p in encoded_passwords_with_salt:
                    hashed_password = hashlib.sha1(p).hexdigest()
                    hashed_passwords[hashed_password] = password

    # Return the original password if hash is found in
    # the hash_passwords dictionary
    if hash in hashed_passwords:
        return hashed_passwords[hash]

    return 'PASSWORD NOT IN DATABASE'
