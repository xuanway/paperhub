Shooting Falcon with One Fault: A Practical Rowhammer-Based Fault Attack Against Falcon
Authors：
[Zihao Xin](https://63dac.conference-program.com/?post_type=page&p=15&uid=98911800783631659131)，[Xin Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=70293107763631154671)，[Zhe Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=86360934642121017911)，[Qianmei Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3540320661579674722)，[Qingni Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=58702626402022338921)，[Ruyi Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=55736619784977183451)，[Yixin Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9272134477442062492)，[Wenqian Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=22214291323792706221)，[Zhihong Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=59414044041165404901)，[Lu Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=7906315718981526723)，[Fan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=314143)

## 中文标题

一错即中：针对 Falcon 的实用 Rowhammer 故障攻击

## 英文摘要

Falcon, a compact post-quantum digital signature scheme, has been selected by National Institute of Standards and Technology (NIST) for the standardization of post-quantum cryptography. While it effectively mitigates the emerging quantum threats, its susceptibly to fault attacks remains insufficiently understood. In this work, we present a novel Rowhammer-based fault attack against Falcon with only one single-bit flip, significantly reduces the number of required faulty signatures by 800× compared to the state-of-the-art attack. Our solution identifies a new vulnerable address offset in Falcon and optimizes the classical Hidden Parallelepiped Problem (HPP) attack. Our end-to-end attack on the Falcon-512 reference implementation successfully recovers the secret key with only 250 k faulty signatures.

## 中文摘要

Falcon 是一种紧凑的后量子数字签名方案，已被美国国家标准与技术研究院（NIST）选中用于后量子密码标准化工作。尽管它能有效缓解新兴的量子威胁，但其对故障攻击的易感性仍缺乏充分认识。本文提出一种新颖的基于 Rowhammer 的 Falcon 故障攻击，仅需单个比特翻转，与现有最先进的攻击相比将所需故障签名数量显著减少 800 倍。我们的方案在 Falcon 中识别出一个新的脆弱地址偏移，并优化了经典的隐藏平行多面体问题（HPP）攻击。我们对 Falcon-512 参考实现的端到端攻击仅用 25 万条故障签名即成功恢复出密钥。
