Slcross: Cross-Component System-Level Cache Side-Channel Attacks on Apple M2 SoC
Authors：
[Yakun Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8889207067985664579)，[Guanlong Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4629460944675265668)，[Yusi Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=2051197210712559994)，[Yinqian Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=15825066542836906541)

## 中文标题

Slcross：针对 Apple M2 SoC 的跨组件系统级缓存侧信道攻击

## 英文摘要

Cross-component cache side-channel attacks exploit shared cache resources across different processing units to infer sensitive information, posing a significant threat to modern heterogeneous computing systems. However, the effectiveness of fine-grained, access-driven cache attacks across components on Apple silicon remains unexplored. In this paper, we demonstrate that cross-component cache attacks can leak GPU sensitive information from the CPU via the System-Level Cache (SLC) on the Apple M2 SoC. We first reverse-engineer the key SLC mechanisms required to enable cache attacks. Leveraging this knowledge, we then introduce a GPU-to-CPU covert channel and an attack targeting the Large Language Model (LLM) embedding table during local LLM inference. Our evaluations validate the feasibility of the fast covert channel and the GPU-side LLM input token leakage based on the SLC.

## 中文摘要

跨组件缓存侧信道攻击利用不同处理单元之间共享的缓存资源推断敏感信息，对现代异构计算系统构成重大威胁。然而，在 Apple 芯片上跨组件实施细粒度、访问驱动的缓存攻击的有效性尚未得到探索。本文证明，跨组件缓存攻击可通过 Apple M2 SoC 上的系统级缓存（SLC）从 CPU 泄露 GPU 的敏感信息。我们首先逆向工程了实施缓存攻击所需的关键 SLC 机制。基于这些认识，我们随后提出一个 GPU 到 CPU 的隐蔽信道，以及一个针对本地 LLM 推理过程中大语言模型（LLM）嵌入表的攻击。我们的评估验证了该高速隐蔽信道的可行性，以及基于 SLC 的 GPU 侧 LLM 输入 token 泄露。
