Graph-Based Attack-Chain Traceback Across Multiple In-Vehicle Network Domains
Authors：
[Abla Smahi](https://63dac.conference-program.com/?post_type=page&p=15&uid=0523749451777209298)，[Xiaohang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=911243)，[Yu Xin](https://63dac.conference-program.com/?post_type=page&p=15&uid=84708059526833278811)，[Chang Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2395477379132724945)，[Amit Kumar Singh](https://63dac.conference-program.com/?post_type=page&p=15&uid=104143)，[Kaiwei Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9563002974758097059)，[Yingtao Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=510443)，[Kui Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=130443)

## 中文标题

面向多车载网络域的基于图的攻击链溯源

## 英文摘要

The expanding connectivity of modern vehicle networks has widened their attack surface. It creates critical vulnerabilities to multi-stage attacks where an initial compromise can lead to control over core vehicle functions. Addressing these vulnerabilities requires precise attack traceback to avoid costly security responses. While traceback is essential for this in traditional networks, its application to automotive systems faces fundamental barriers. International homologation standards (UN R155, ISO/SAE 21434) require network architectures to maintain certification compliance, rendering traditional traceback methods (e.g., packet marking) that modify communication stacks as legally and technically infeasible. Production vehicles further exacerbate this challenge with limited resources. We present the first practical solution to this impasse: a gateway-resident traceback system operating entirely within certification boundaries. Our key insight is to reconstruct attack chains solely from existing intrusion detection systems (IDSs) alerts across host, Ethernet, and Controller Area Network (CAN) domains by modeling these alerts as nodes in a temporal graph. Edges are admitted only after four plausibility checks—topological, temporal, semantic, and kinematic—ensuring all reconstructed chains are physically and functionally plausible. Our system achieves a 0.90 edge-level F1 score (64% higher than baselines) with a 0.086 false discovery rate, representing a 72% reduction, while using only 1.2% CPU and 26 MB of Memory usage on a production Leapmotor C10. In addition, we release the dataset for traceback.

## 中文摘要

现代车载网络的连接性不断扩展，其攻击面也随之扩大，由此产生了对多阶段攻击的关键脆弱性：初始的入侵可能最终演变为对车辆核心功能的控制。要应对这些脆弱性，需要精确的攻击溯源，以避免代价高昂的安全响应。尽管溯源在传统网络中至关重要，但将其应用于汽车系统却面临根本性障碍。国际型式认证标准（UN R155、ISO/SAE 21434）要求网络架构必须保持认证合规性，这使得修改通信协议栈的传统溯源方法（如数据包标记）在法律和技术上均不可行。量产车辆资源受限，进一步加剧了这一挑战。我们针对这一僵局提出了首个实用解决方案：一个完全运行在认证边界之内的驻留网关溯源系统。我们的核心洞察是：仅利用主机、Ethernet 和 Controller Area Network（CAN）域中已有的入侵检测系统（IDS）告警，将这些告警建模为时序图中的节点，从而重构攻击链。只有在通过拓扑、时序、语义和运动学这四项合理性检验之后才允许建立边，从而确保所有重构出的攻击链在物理与功能上均合理。我们的系统实现了 0.90 的边级 F1 分数（比基线高 64%），错误发现率为 0.086（降低 72%），而在量产 Leapmotor C10 上仅占用 1.2% 的 CPU 和 26 MB 内存。此外，我们公开了用于溯源的数据集。

## 英文关键词

In-vehicle networks (IVN), Attack traceback, Attack chains

## 中文关键词

车载网络（IVN）、攻击溯源、攻击链
