Icarus's Wings: Disabling MoE Offloading Acceleration via a Universal Hidden Prefix Attack
Authors：
[Qichao Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=457576436105282113)，[Zecheng Hao](https://63dac.conference-program.com/?post_type=page&p=15&uid=67087717480541848271)，[Zihao Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=5160323734301538912)，[LING LIANG](https://63dac.conference-program.com/?post_type=page&p=15&uid=8940208517771403718)，[Xing Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=544143)，[Zhaofei Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2940631819639814086)，[Tiejun Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6129163442233776589)

## 中文标题

Icarus 之翼：利用通用隐藏前缀攻击使 MoE 卸载加速失效

## 英文摘要

Online LLM inference service demands low latency with tight memory. Mixture of Experts (MoE) meets memory constraints by activating a few Experts, computing active ones on GPUs, and offloading others to CPUs. For latency, acceleration systems utilize Expert caching and prefetching strategies, assuming Experts’ temporal locality and predictable prefetch. When these assumptions fail, wrong experts loads inflate latency, enabling Denial-of-Service (DoS). Existing LLM DoS attacks target extending LLMs’ generation length, with high attack costs, weak transferability, and lack MoE analysis. In this work, we expose this vulnerability in GPU-centric MoE offloading acceleration and present Icarus, a gradient-based universal attack injecting an adversarial prefix embedding to disable such acceleration. Icarus first incorporates Cache Temporal Locality Minimization (TLM) and Prefetch Expert Prediction Misleading (EPM) to model MoE decoding behavior systematically, then adversarially breaks acceleration. Next, a scheduler balances attack targets. Experiments show that, by applying a single prefix embedding before any user input, Icarus increases Expert replacements by 85.4%, and decreases prefetch accuracy by 12.5%, achieving an average 0.7× decoding slowdown under SOTA GPU-centric acceleration strategies across models and devices.

## 中文摘要

在线 LLM 推理服务要求在紧张的内存条件下实现低延迟。混合专家（MoE）通过激活少量专家、在 GPU 上计算被激活的专家并将其余专家卸载至 CPU 来满足内存约束。为降低延迟，各类加速系统采用专家缓存与预取策略，其前提是专家具备时间局部性且预取可预测。当这些假设不成立时，错误的专家加载会放大延迟，从而可实现拒绝服务（DoS）。现有 LLM DoS 攻击着眼于延长 LLM 的生成长度，攻击成本高、迁移性弱，且缺乏对 MoE 的分析。本文揭示以 GPU 为中心的 MoE 卸载加速中的这一漏洞，并提出 Icarus——一种基于梯度的通用攻击，通过注入对抗前缀嵌入使此类加速失效。Icarus 首先引入缓存时间局部性最小化（TLM）与预取专家预测误导（EPM），以系统化建模 MoE 解码行为，进而以对抗方式破坏加速；随后由调度器平衡各攻击目标。实验表明，仅在任意用户输入之前施加单个前缀嵌入，Icarus 即可使专家替换增加 85.4%、预取准确率下降 12.5%，在多种模型与设备上、面向当前最优的以 GPU 为中心的加速策略，实现平均 0.7 倍的解码减速。
