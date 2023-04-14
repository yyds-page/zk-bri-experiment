from py_ecc import bn128
from gmpy2 import mpz, powmod, invert


def groth16_prove(prover_key, public_input, circuit_eval):
    # Unpack the prover key
    (alpha, beta, gamma, delta, abar, bbar, C, H) = prover_key

    # Calculate A and B
    A = bn128.multiply(bn128.G2, abar)
    B = bn128.multiply(beta, bbar)

    # Calculate the polynomial coefficients
    z = mpz(circuit_eval)
    l = [0] * 3
    l[0] = z - abar
    l[1] = powmod(z, 2, bn128.curve_order()) - 2 * powmod(z, 1, bn128.curve_order()) * abar + powmod(abar, 2,
                                                                                                     bn128.curve_order())
    l[2] = -z + abar

    # Calculate P and Q
    P = bn128.multiply(H, l[0]) + bn128.multiply(B, l[1]) + bn128.multiply(A, l[2])
    Q = bn128.multiply(G1, alpha) + bn128.multiply(B, z)

    # Calculate the challenge
    e = bn128.pairing(P, Q)

    # Calculate the proof
    s = (abar + e * bbar) % bn128.curve_order()
    t = (alpha + e * beta) % bn128.curve_order()
    u = (gamma + e * delta) % bn128.curve_order()

    return (s, t, u)


def groth16_verify(verifier_key, public_input, proof):
    # Unpack the verifier key
    (alpha, beta, gamma, delta, H) = verifier_key

    # Unpack the proof
    (s, t, u) = proof

    # Calculate A and B
    A = bn128.multiply(bn128.G2, s)
    B = bn128.multiply(beta, t)

    # Calculate P and Q
    P = bn128.multiply(H, u) + bn128.multiply(B, public_input)
    Q = bn128.multiply(G1, alpha) + bn128.multiply(B, s)

    # Calculate the challenge
    e = bn128.pairing(P, Q)

    # Verify the proof
    return powmod(bn128.pairing(A, Q) * bn128.pairing(H, B) * bn128.pairing(G1, delta), e,
                  bn128.curve_order()) == bn128.FQ12.one()
