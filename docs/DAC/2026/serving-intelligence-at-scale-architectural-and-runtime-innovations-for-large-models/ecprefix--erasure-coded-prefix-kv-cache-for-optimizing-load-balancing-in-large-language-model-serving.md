Ecprefix: Erasure-Coded Prefix KV Cache for Optimizing Load Balancing in Large Language Model Serving
Authors：
[Feifan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1201436490916472565)，[Yuchong Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7589487054955796938)，[Mingqi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=51140929853057039761)，[Lin Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9994832929020643842)，[Chenxuan Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3243447701029812561)，[Zhenghao Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=00709471565442802821)，[Dan Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=342343)

## 中文标题

ECPrefix：用于优化大语言模型服务负载均衡的纠删码前缀 KV 缓存

## 英文摘要

Prefix KV cache is widely used to accelerate LLM serving by trading more storage for less computation, and state-of-the-art methods often replicate hotspot caches for load balancing. However, we observe that the few nodes that have cache replicas still lead to severe load imbalance. This paper presents ECPrefix : a new prefix KV cache framework based on erasure coding (instead of replication), which distributes encoded blocks of hot prefix caches (organized as profile-guided objects) across nodes, along with adaptive striping and pipelined reading optimizations. Evaluation shows that ECPrefix reduces TTFT by up to 52.3% over existing systems.

## 中文摘要

前缀 KV 缓存通过以更多存储换取更少计算，被广泛用于加速 LLM 服务，而先进方法通常复制热点缓存以实现负载均衡。然而我们观察到，即便只有少数节点持有缓存副本，仍会导致严重的负载不均衡。本文提出 ECPrefix：一种基于纠删码（而非副本复制）的新型前缀 KV 缓存框架，它将热点前缀缓存的编码块（组织为 profile 引导的对象）分布到各节点之上，并配合自适应条带化与流水化读取优化。评估表明，ECPrefix 相比现有系统将 TTFT 最多降低 52.3%。

## 英文关键词

Load Balance, Erasure Coding, LLM Serving

## 中文关键词

负载均衡、纠删码、LLM 服务
