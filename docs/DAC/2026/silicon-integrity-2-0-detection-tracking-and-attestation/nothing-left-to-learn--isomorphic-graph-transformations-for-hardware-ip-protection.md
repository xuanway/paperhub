Nothing Left to Learn: Isomorphic Graph Transformations for Hardware IP Protection
Authors：
[Shaza Elsharief](https://63dac.conference-program.com/?post_type=page&p=15&uid=30161788838807741611)，[Lilas Alrahis](https://63dac.conference-program.com/?post_type=page&p=15&uid=29421466544607140421)，[Johann Knechtel](https://63dac.conference-program.com/?post_type=page&p=15&uid=51655288589515181611)，[Ozgur Sinanoglu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5647267599921234185)

## 中文标题

无可学之迹：面向硬件 IP 保护的同构图变换

## 英文摘要

Logic locking protects hardware designs across the global semiconductor supply-chain. However, recent machine learning (ML)-based attacks, especially graph learning-based ones, have undermined its security by learning circuit structures and gate compositions to reveal locked connections/gates. Although recent locking methods use explainability tools and adversarial perturbations, they remain vulnerable to ML attacks under robust training. Therefore, there is still a need for truly learning-resilient locking solutions. We propose IsoLock, a locking scheme that performs interconnect obfuscation to secure the circuit’s structure and functionality. IsoLock models the gate-level netlist as a graph and introduces MUXes for locking (through rewiring selected interconnects), generating isomorphic structures. These structures are indistinguishable to ML models and other structural attacks, effectively blocking all learnable/predictable features and preventing key deciphering. For evaluation, first, we prove IsoLock’s security against modeling attacks. Second, we lock standard ISCAS-85 and ITC-99 benchmarks and evaluate them against state-of-the-art ML attacks (SCOPE and MuxLink) and structural attacks (Redundancy and SAAM), all of which can decipher only 0–6% of the correct key on average, confirming IsoLock’s resilience also in practice.

## 中文摘要

逻辑锁定可在全球半导体供应链中保护硬件设计。然而，近期基于机器学习（ML）的攻击，尤其是基于图学习的攻击，通过学习电路结构与门级构成来揭示被锁定的连线/门，已削弱了其安全性。尽管近期的锁定方法借助可解释性工具与对抗扰动，但在鲁棒训练条件下仍易受 ML 攻击。因此，仍需真正具备抗学习能力的锁定方案。我们提出 IsoLock，一种通过互连混淆来保护电路结构与功能的锁定方案。IsoLock 将门级网表建模为图，并引入 MUX 进行锁定（通过重连选定的互连），从而生成同构结构。这些结构对 ML 模型及其他结构攻击不可区分，可有效阻断所有可学习/可预测特征，防止密钥被破解。在评估方面，首先我们证明了 IsoLock 抵御建模攻击的安全性；其次，我们对标准 ISCAS-85 与 ITC-99 基准电路进行锁定，并针对先进的 ML 攻击（SCOPE 与 MuxLink）以及结构攻击（Redundancy 与 SAAM）进行评估，这些攻击平均仅能破解 0–6% 的正确密钥，证实了 IsoLock 在实际中同样具备韧性。
