#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tqdm import tqdm
from RsaCtfTool.attacks.abstract_attack import AbstractAttack
from RsaCtfTool.lib.keys_wrapper import PrivateKey
from RsaCtfTool.lib.algos import wiener


class Attack(AbstractAttack):
    def __init__(self, timeout=60):
        super().__init__(timeout)
        self.speed = AbstractAttack.speed_enum["medium"]

    def attack(self, publickey, cipher=[], progress=True):
        """Wiener's attack"""
        pq = wiener(publickey.n, publickey.e, progress)
        if pq is None:
            self.logger.warning("[*] Cracking failed...")
        else:
            publickey.p, publickey.q = pq
            priv_key = PrivateKey(
                int(publickey.p),
                int(publickey.q),
                int(publickey.e),
                int(publickey.n),
            )
            return priv_key, None
        return None, None

    def test(self):
        from RsaCtfTool.lib.keys_wrapper import PublicKey

        key_data = """-----BEGIN PUBLIC KEY-----
MIIEIjANBgkqhkiG9w0BAQEFAAOCBA8AMIIECgKCAgEDMXAsX+AfJAHJ5E7Aunnk
/AwahJiyenQz9UOB9r6MuzOSRgIHFggsPr6Duj5q8v61RoMyrifh3VvMgtkgGrqB
wckMHt67sGYbigo4c5zLz9kz8DI4g7Y3n/pipdceQGt8O6YxTEnq8NcL5HIQ0iqL
quS+idjbYgy5dtAyoprDvHcTNOgEefVLB6OaZ5G7Q0txPWo/QoYSQEpVyzp4fl0T
4m6ui+uLUuT3JKg+sEIw+sF6ztfezgt+1E2mDs5d32fHJ92DpeigzyQwOFasQert
Acgld/3wdh4xv8w7USJ871nF3RVLqKYW7dwswb2G/QT6zSmnavZILLHNzs/u3z7J
iWM4SPbmYv16XbzVYDU01GPIeIQFPqVsKYSbw0+erEzqTnaioou9OuNS8bZfQQPz
fXJ20C7cFOw2FqVw+obmi6C4qvdXNXJIHN+CZWXwIx/I2ZSOBCCCGEQjinlPupZ0
p3uBpeYJY5IPu16CIM4asYm+DbM+2URKAR4fawnm6D3sZ6a8xn5ebO0keqKvEYnT
H1WtQzAvMZcar0zaotj5G6DbYlhFsMZxKZjhZVZDvaWscXem6lAU9zYVsllYuVmn
hVDrg3gXfDzyP5+IKxfyydcfzkEClfex3PpDnaCo4VSAF6iIsgKjxsUErKy3Q7XI
cZpptlNof+saJWgqWwV9dXkCggIBAsOYvjEh0hDi9U26aIoPFida3LsfLAM3ptUs
brD3yGBXM35RJacHrlwkkY44eny81QNRINCg6+pKSz60xdyT17qsvB4z4Q1zSxXx
hPqdAHB/nTREbAs4AlToNL0SCEc8G0aUdQ2+myunQVfuxTfVMnnyiUIy8la5i5Fq
ULeJXUBOSV+ERX/VmeX7O4TTLSlzvnnFSarIip58+4IIoSXD2m77ZvhPq8HZfaW9
xFw3we9zw/lQu6nLJrqgR6cmk9DD/dA4zzSLUyc3I33HpL1VM+R66cP+1uRj2Ytn
8Ku0ZWQ8PlwH15QNL/PqJoXhrFou4wCIAX99sVdhh0pnwKaHqJwSANOFi60ELkF0
/ATLPKWG124Kdkp24At4+jLJqirQSd13gpKYRdaCVo/1f3trt1xyXns6sD++onbl
I6TB4WAZuMKmzZthDfJCeWYeOhiOhDTewqi4KP227P/p+7sQKXyiI5mxIFnfRCtM
88K0xA+0yw7m1OVb69OwU5gN/uLdRIwrpA/K8zFFueD4X0Rj9MFA06hEt7rphK3a
Aqk1HXHWiF2tXr7lxpkQyRi15tyiig9CmCgPG4e1Pk95FRd6CR8i8s1q3DmtdqHb
FccBoenVqO5rZ5YwVEuhG+ofy1sEPNXO3ZPOO51DJgQO3mxmnceqLgF/Ktpzxyg+
sSSqyHKL
-----END PUBLIC KEY-----"""
        result = self.attack(PublicKey(key_data), progress=False)
        return result != (None, None)
