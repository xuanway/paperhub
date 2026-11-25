PLONK-Hammer:breaking Input Privacy of PLONK Proving Systems via Rowhammer
Authors：
[Zhiwen Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0494552758214617881)，[Junkai Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=11894630984250521081)，[Xin Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=70293107763631154671)，[Qingni Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=58702626402022338921)，[Cong Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=8367420698947911679)，[Yuejian Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0248190209347998841)

## 中文标题

PLONK-Hammer：利用 Rowhammer 破坏 PLONK 证明系统的输入隐私

## 英文摘要

Zero-knowledge proofs, particularly succinct non-interactive variants (zk-SNARKs), are instrumental in verifiable computation without revealing privacy. Zk-SNARKs are provably secure against cryptographic attacks; however, whether these systems can resist fault injection attacks requires further investigation. Previous related work focused on QAP-based zk-SNARKs like Groth16. PLONK improves upon Groth16 with a universal and updatable trusted setup. In this work, we present PLONK-Hammer, which breaks input privacy of PLONK via Rowhammer. We inject faults into the secret inputs. Then we devise an algorithm to recover the secret using faulty proofs and polynomial commitment techniques. We evaluate PLONK-Hammer in gnark, successfully leak secrets by our attack.

## 中文摘要

零知识证明，尤其是简洁非交互式变体（zk-SNARK），是在不泄露隐私的前提下实现可验证计算的重要工具。zk-SNARK 在密码学攻击下具有可证明的安全性；然而这类系统能否抵御故障注入攻击仍有待研究。已有相关工作主要针对基于 QAP 的 zk-SNARK（如 Groth16）。PLONK 通过通用且可更新的可信设置对 Groth16 加以改进。本文提出 PLONK-Hammer，利用 Rowhammer 破坏 PLONK 的输入隐私。我们向秘密输入注入故障，进而设计一种算法，借助错误证明与多项式承诺技术恢复秘密。我们在 gnark 中对 PLONK-Hammer 进行评估，成功通过该攻击泄露秘密。
