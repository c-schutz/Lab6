def decoder(password):
    d_pass = ""
    for i in password:
        dec = int(i)
        dec -= 3
        d_pass += str(dec)
    return d_pass





