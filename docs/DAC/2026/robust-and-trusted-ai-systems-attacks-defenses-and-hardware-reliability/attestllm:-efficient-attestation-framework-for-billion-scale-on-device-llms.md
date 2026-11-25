Attestllm: Efficient Attestation Framework for Billion-Scale On-Device LLMs
Authors：
[Ruisi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5159214018188392675)，[Yifei Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=80773485282589008811)，[Neusha Javidnia](https://63dac.conference-program.com/?post_type=page&p=15&uid=8427235080809287273)，[Mengxin Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=7043608771704783242)，[Farinaz Koushanfar](https://63dac.conference-program.com/?post_type=page&p=15&uid=0301512236982358263)

## 中文标题

AttestLLM：面向十亿级端侧 LLM 的高效认证框架

## 英文摘要

This paper presents AttestLLM, the first attestation framework to protect device vendors’ hardware-level intellectual property by ensuring that only authorized large language models (LLMs) can execute on target platforms. To overcome the scalability and efficiency limitations of prior work, AttestLLM leverages an algorithm/software/hardware co-design approach to embed robust watermarks onto the activation of LLM layers. In addition, it optimizes the attestation protocol within the trusted execution environment, providing efficient ownership verification without compromising inference throughput. Extensive evaluations on various on-device LLMs demonstrate AttestLLM’s attestation reliability, fidelity preservation, and efficiency. Furthermore, AttestLLM exhibits resilience against forgery, replacement, and TEE system attacks.

## 中文摘要

本文提出 AttestLLM，这是首个通过确保仅有经授权的大语言模型（LLM）才能在目标平台上执行、从而保护设备厂商硬件级知识产权的认证框架。为克服先前工作在可扩展性与效率方面的局限，AttestLLM 采用算法/软件/硬件协同设计方法，在 LLM 各层的激活值中嵌入鲁棒水印。此外，它在可信执行环境内优化认证协议，在不损害推理吞吐的前提下提供高效的所有权验证。在多种端侧 LLM 上的广泛评估表明，AttestLLM 具有认证可靠性、保真性保持能力与高效性。此外，AttestLLM 对伪造、替换以及 TEE 系统攻击均表现出韧性。
