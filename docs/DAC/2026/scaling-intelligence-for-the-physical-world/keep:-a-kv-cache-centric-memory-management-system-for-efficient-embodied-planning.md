KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning
Authors：
[Zebin Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=17827585784550662921)，[Tong Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=21842765951470382951)，[Baotong Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4309282772923259713)，[Shaoshan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=013643)，[Bo Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1437181486312215528)，[Meng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=414843)

## 中文标题

KEEP：面向高效具身规划的以 KV Cache 为中心的内存管理系统

## 英文摘要

Memory-augmented Large Language Models (LLMs) have demonstrated remarkable capability for complex and long-horizon embodied planning. By keeping track of past experiences and environmental states, memory enables LLMs to maintain a global view, thereby avoiding repetitive exploration. However, existing approaches often store the memory as raw text, leading to excessively long prompts and high prefill latency. While it is possible to store and reuse the KV caches, the efficiency benefits are greatly undermined due to frequent KV cache updates. In this paper, we propose KEEP, a KV-cache-centric memory management system for efficient embodied planning. KEEP features 3 key innovations: (1) a Static-Dynamic Memory Construction algorithm that reduces KV cache recomputation by mixed-granularity memory group; (2) a Multi-hop Memory Re-computation algorithm that dynamically identifies important cross-attention among different memory groups and reconstructs memory interactions iteratively; (3) a Layer-balanced Memory Loading that eliminates unbalanced KV cache loading and cross-attention computation across different layers. Extensive experimental results have demonstrated that KEEP achieves 2.68× speedup with negligible accuracy loss compared with text-based memory methods on ALFRED dataset. Compared with the KV recomputation method CacheBlend (EuroSys’25), KEEP shows 4.13% success rate improvement and 1.90× time-to-first-token (TTFT) reduction. Our code is available on https://github.com/PKU-SEC-Lab/KEEP_Embodied_Memory.

## 中文摘要

具备记忆增强能力的大语言模型（LLM）在复杂长时程具身规划中展现出卓越能力。通过记录过往经验与环境状态，记忆使 LLM 得以保持全局视野，从而避免重复探索。然而，现有方法通常将记忆以原始文本形式存储，导致提示过长与很高的 prefill 延迟。虽然可以存储并复用 KV cache，但频繁的 KV cache 更新大幅削弱了效率收益。本文提出 KEEP，一种以 KV cache 为中心的具身规划内存管理系统。KEEP 具有三项关键创新：（1）静态—动态记忆构建算法，通过混合粒度记忆组减少 KV cache 重计算；（2）多跳记忆重计算算法，动态识别不同记忆组之间重要的交叉注意力，并迭代重建记忆交互；（3）层均衡记忆加载，消除不同层之间不均衡的 KV cache 加载与交叉注意力计算。大量实验结果表明，在 ALFRED 数据集上，与基于文本的记忆方法相比，KEEP 在精度损失可忽略的情况下实现 2.68× 加速。与 KV 重计算方法 CacheBlend（EuroSys'25）相比，KEEP 的成功率提升 4.13%，首 token 时间（TTFT）缩短 1.90×。我们的代码见 https://github.com/PKU-SEC-Lab/KEEP_Embodied_Memory。

## 英文关键词

Embodied Planning, Memory System, KV Cache Management, KV Recomputation

## 中文关键词

具身规划、内存系统、KV Cache 管理、KV 重计算
