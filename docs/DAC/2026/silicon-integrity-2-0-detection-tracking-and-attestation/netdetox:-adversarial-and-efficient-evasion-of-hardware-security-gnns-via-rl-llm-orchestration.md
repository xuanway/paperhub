Netdetox: Adversarial and Efficient Evasion of Hardware-Security GNNs via RL-LLM Orchestration
Authors：
[Zeng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2254448630884554168)，[Minghao Shao](https://63dac.conference-program.com/?post_type=page&p=15&uid=62524945777437575211)，[Akashdeep Saha](https://63dac.conference-program.com/?post_type=page&p=15&uid=027082211366625724)，[Ramesh Karri](https://63dac.conference-program.com/?post_type=page&p=15&uid=491143)，[Johann Knechtel](https://63dac.conference-program.com/?post_type=page&p=15&uid=51655288589515181611)，[Muhammad Shafique](https://63dac.conference-program.com/?post_type=page&p=15&uid=560343)，[Ozgur Sinanoglu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5647267599921234185)

## 中文标题

NetDeTox：经 RL-LLM 协同的对抗性高效硬件安全 GNN 规避

## 英文摘要

Graph neural networks (GNNs) have shown promise in hardware security by learning structural motifs from netlist graphs. However, this reliance on motifs makes GNNs vulnerable to adversarial netlist rewrites; even small-scale edits can mislead GNN predictions. Existing adversarial approaches, ranging from synthesis-recipe perturbations to gate transformations, come with high design overheads. We present NetDeTox, an automated end-to-end framework that orchestrates large language models (LLMs) with reinforcement learning (RL) in a systematic manner, enabling focused local rewriting. The RL agent identifies netlist components critical for GNN-based reasoning, while the LLM devises rewriting plans to diversify motifs that preserve functionality. Iterative feedback between the RL and LLM stages refines adversarial rewritings to limit overheads. Compared to the SOTA work AttackGNN, NetDeTox successfully degrades the effectiveness of all security schemes with fewer rewrites and substantially lower area overheads (reductions of 54.50% for GNN-RE, 25.44% for GNN4IP, and 41.04% for OMLA, respectively). For GNN4IP, ours can even optimize/reduce the original benchmarks’ area, in particular for larger circuits, demonstrating the practicality and scalability of NetDeTox.

## 中文摘要

图神经网络（GNN）通过从网表图中学习结构基元，在硬件安全领域展现出潜力。然而，这种对基元的依赖使 GNN 易受对抗性网表改写的影响；即便是小规模改动也可能误导 GNN 的预测。现有对抗方法从综合配方扰动到门级变换，均带来较高的设计开销。我们提出 NetDeTox，一个自动化的端到端框架，以系统化方式协同大语言模型（LLM）与强化学习（RL），实现聚焦的局部改写。RL 智能体识别对基于 GNN 的推理至关重要的网表组件，LLM 则制定改写方案以多样化保持功能的基元。RL 与 LLM 阶段之间的迭代反馈进一步精化对抗改写以限制开销。与 SOTA 工作 AttackGNN 相比，NetDeTox 以更少的改写次数成功削弱了所有安全方案的有效性，并大幅降低面积开销（GNN-RE 降低 54.50%、GNN4IP 降低 25.44%、OMLA 降低 41.04%）。对于 GNN4IP，我们的方法甚至能优化/减小原始基准的面积，在较大电路上尤为明显，体现了 NetDeTox 的实用性与可扩展性。
