Faster-MoA: Low-Latency Tree-Structured MoA Serving with Early Exit and Agent-Aware Prefill-Decode Overlap
Authors：
[Zijun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4634106116231297906)，[Yijiahao Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=5740536195665541507)，[Hanqiu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=3527589664040245099)，[Zishen Wan](https://63dac.conference-program.com/?post_type=page&p=15&uid=573443)，[Gongjin Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=5550829966453754601)，[Dongyang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=4660491945629584804)，[Shuyi Pei](https://63dac.conference-program.com/?post_type=page&p=15&uid=66768248524715451931)，[Cong "Callie" Hao](https://63dac.conference-program.com/?post_type=page&p=15&uid=516143)

## 中文标题

Faster-MoA：基于提前退出与智能体感知预填充-解码重叠的低延迟树结构 MoA 服务

## 英文摘要

Mixture-of-Agents (MoA) is a widely adopted multi-agent paradigm, but existing MoA systems face two major challenges: excessive agent-to-agent connectivity and poor hardware efficiency. To address these two issues, we propose Faster-MoA, a unified algorithm-system co-design for efficient MoA serving. Faster-MoA has three innovations. First, we replace the conventional all-to-all topology with a hierarchical tree structure that introduces structured sparsity in agent connections. Second, we develop a run-time dynamic agent early-exit mechanism that prunes unnecessary agent connections based on output semantic similarity and answer confidence. Third, we propose an agent-dependency-aware incremental prefilling mechanism that overlaps prefilling and decoding among agents with data dependencies to reduce inference latency. Together, these three innovations enable Faster-MoA to reduce end-to-end serving latency by up to 90% while achieving similar (only ±1% variation) or even higher task accuracy compared with MoA baselines using all-to-all agent connection. Our code is open-sourced at: https://github.com/sharc-lab/Faster-MoA.

## 中文摘要

混合智能体（MoA）是一种被广泛采用的多智能体范式，但现有 MoA 系统面临两大挑战：智能体间连接过多与硬件效率低下。为解决这两个问题，我们提出 Faster-MoA，一种面向高效 MoA 服务的统一算法-系统协同设计。Faster-MoA 包含三项创新。首先，我们用分层树结构替代传统的全互连拓扑，在智能体连接中引入结构化稀疏性。其次，我们开发了一种运行时动态智能体提前退出机制，基于输出语义相似度与答案置信度剪除不必要的智能体连接。第三，我们提出一种智能体依赖感知的增量预填充机制，在具有数据依赖的智能体之间重叠预填充与解码，以降低推理延迟。三项创新共同使 Faster-MoA 相较于采用全互连智能体连接的 MoA 基线，将端到端服务延迟降低最高 90%，同时达到相近（仅 ±1% 波动）甚至更高的任务准确率。我们的代码已开源于：https://github.com/sharc-lab/Faster-MoA。

## 英文关键词

Mixture-of-Agents (MoA), Multi-Agent Systems (MAS), Dynamic Early-Exit, Prefill-Decode Disaggregation (PD), LLM Serving

## 中文关键词

混合智能体（MoA）、多智能体系统（MAS）、动态提前退出、预填充-解码分离（PD）、LLM 服务
