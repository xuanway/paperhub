A Remote Side-Channel Attack on Post-Quantum Key Encapsulation Mechanisms: A Case Study of ML-KEM on Intel x86
Authors：
[Mona Hashemi](https://63dac.conference-program.com/?post_type=page&p=15&uid=220349456623238504)，[Qianmei Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3540320661579674722)，[Fan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=314143)，[Shivam Bhasin](https://63dac.conference-program.com/?post_type=page&p=15&uid=277343)，[Trevor E. Carlson](https://63dac.conference-program.com/?post_type=page&p=15&uid=252143)

## 中文标题

后量子密钥封装机制的远程侧信道攻击：Intel x86 平台上 ML-KEM 的案例研究

## 英文摘要

As post-quantum cryptographic (PQC) schemes are standardized, evaluating their resilience to side-channel attacks (SCA) becomes critical. While most prior studies focus on physical SCAs, the practicality of remote SCAs on full implementations of standardized PQCs remains largely unexplored. In this paper, we present the first generic remote power SCA on the Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM), evaluated on a modern Intel x86 processor. Our result demonstrates that power traces can be exploited remotely as a plaintext-checking oracle, enabling secret key recovery despite the scheme’s theoretical IND-CCA security. Using ML-KEM as a case study, we show that complex microarchitectural mechanisms such as speculative execution and dynamic power management do not eliminate exploitable power leakage. We evaluated our attack on the PQClean implementation, achieving secret key recovery with a success rate up to 99.5%. These findings provide a realistic assessment of PQC leakage behavior on high-end processors and underscore the need for architecture-aware leakage models and co-designed hardware–software defenses to ensure secure PQC deployment in practice.

## 中文摘要

随着后量子密码（PQC）方案被标准化，评估其抵御侧信道攻击（SCA）的韧性变得至关重要。虽然大多数已有研究聚焦于物理 SCA，但针对标准化 PQC 完整实现的远程 SCA 的实用性在很大程度上仍未得到探索。本文提出首个针对基于模格的密钥封装机制（ML-KEM）的通用远程功耗 SCA，并在现代 Intel x86 处理器上进行评估。我们的结果表明，功耗迹可被远程用作明文检查预言机，尽管该方案在理论上具备 IND-CCA 安全性，仍能实现密钥恢复。以 ML-KEM 为案例，我们表明诸如推测执行和动态功耗管理等复杂微架构机制并不能消除可被利用的功耗泄露。我们在 PQClean 实现上评估了该攻击，密钥恢复成功率高达 99.5%。这些发现对 PQC 在高端处理器上的泄露行为给出了现实评估，并凸显了需要架构感知的泄露模型以及软硬件协同设计的防御措施，以确保 PQC 在实践中的安全部署。

## 英文关键词

Post-Quantum Cryptography, Side-Channel Attack, Power Analysis, Key Encapsulation Mechanism, Chosen-Ciphertext Attack

## 中文关键词

后量子密码、侧信道攻击、功耗分析、密钥封装机制、选择密文攻击
