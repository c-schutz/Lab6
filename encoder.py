#Encoding file

#45678888

def encode(password):

    n_pass = ""
    num = None

    for value in password:
        num = int(value)
        num += 3
        print(num)
        n_pass += str(num)

    return n_pass
