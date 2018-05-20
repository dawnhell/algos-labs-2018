def main():
    p = 181
    q = 307
    n = p * q
    phi = (p - 1) * (q - 1)
    pk = 1693
    sk = multiplicative_inverse(pk, phi)

    print("Public key: ({}, {}); Secret key: ({}, {});".format(pk, n, sk, n))

    message = "Hello, this is a secret message! Don't read this!"
    encrypted = encrypt(pk, n, message)
    print (encrypted)
    decrypted = decrypt(sk, n, encrypted)
    print (decrypted)

    brute_force(pk, n, encrypted)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def binpow(a, n):
    res = 1
    while n:
        if n % 2 == 1:
            res *= a
        a *= a
        n /= 2
    return res


def encrypt(pk, n, message):
    return [binpow(ord(char), pk) % n for char in message]


def decrypt(sk, n, message):
    return ''.join([chr(binpow(char, sk) % n) for char in message])


def brute_force(pk, n, encrypted):
    p, q = 0, 0
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n / i
            break

    print("Found p: {}; found q: {}".format(p, q))
    phi = (p - 1) * (q - 1)
    new_sk = multiplicative_inverse(pk, phi)
    print("Encrypted message: {}".format(decrypt(new_sk, n, encrypted)))


main()
