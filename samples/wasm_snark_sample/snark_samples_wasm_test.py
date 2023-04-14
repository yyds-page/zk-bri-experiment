import os
import json

# https://github.com/tokamak-network/python-snarks
from python_snarks import Groth, Calculator, gen_proof, is_valid


def test_groth():
    ## 1. setup zkp
    print("1. setting up...")
    gr = Groth(os.path.dirname(os.path.realpath(__file__)) + "/circuit/circuit.r1cs")
    gr.setup_zk()
    print("#" * 80)
    print(gr.setup)
    print("#" * 80)

    ## 2. proving
    print("2. proving...")
    wasm_path = os.path.dirname(os.path.realpath(__file__)) + "/circuit/circuit.wasm"
    c = Calculator(wasm_path)
    witness = c.calculate({"a": 33, "b": 34})
    print("witness: ", witness)
    proof, publicSignals = gen_proof(gr.setup["vk_proof"], witness)
    print("#" * 80)
    print(json.dumps(proof, indent=2, sort_keys=True, ensure_ascii=False))
    print("#" * 80)
    print(json.dumps(publicSignals, indent=2, sort_keys=True, ensure_ascii=False))
    print("#" * 80)

    ## 3. verifying
    print("3. verifying...")
    result = is_valid(gr.setup["vk_verifier"], proof, publicSignals)
    print(result)
    assert result == True


# output:
'''
1. setting up...
2. proving...
################################################################################
{'pi_a': [2297671688756096938930180953052840154426585508580546346743301258257508112996, 8115599812822278380233444425303391504337299205229962465186427318106720164784, 1], 'pi_b': ['[652928444852682118033310541658670969872136485943388930543987368020620865789, 16091349323353807154651270941445618069196260022265112126073865423076432787416]', '[1326886876728050985004942889031062374740331911462367097858429705705210225051, 15174495765455353658578529116049374814710976601211139208280407504603625507254]', '[1, 0]'], 'pi_c': [4382845374868120991782753756688507895718275124700062144804408620149669197226, 12100536544512566303162673501264155650427132334975538678253547055242373457441, 1], 'protocol': 'groth'}
################################################################################
[17986729205814946410284549601323002655531532322879282343898458869611517778710]
################################################################################
3. verifying...
True
'''

if __name__ == '__main__':
    test_groth()
