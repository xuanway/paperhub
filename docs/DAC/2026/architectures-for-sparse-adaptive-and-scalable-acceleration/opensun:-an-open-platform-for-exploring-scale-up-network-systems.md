OpenSUN: An Open Platform for Exploring Scale-Up Network Systems
Authors：
[Yiqi Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=9806489438728888507)，[Bizhao Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=3875470805115007763)，[Tao Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=58689717072449667341)，[Ying Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=02843505364371864751)，[Xiaotong Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=15464909385915273721)，[Mingtao Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=34817855751728202141)，[Cheng Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=00307792951827075741)，[Guojie Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=876143)，[Guangyu Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=470243)，[Zhe Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=47672312475676865101)

## 中文标题

OpenSUN：探索 Scale-Up 网络系统的开放平台

## 英文摘要

The deceleration of Moore’s Law, combined with the rising computational demands of big-data applications and generative AI, is accelerating the development of scale-up systems. Unlike traditional scale-out architectures, scale-up systems typically extend shared memory across multiple nodes using high-bandwidth, load/store-based interconnects such as CXL, UALink, NVLink, and UnifiedBus. Designing and optimizing such interconnected systems poses a multi-faceted challenge spanning computer architecture, interconnect technology and software system. Although industry has introduced numerous commercial solutions, the academic community still lacks an open-source, hardware-based platform to support cross-stack research, such as exploring new protocols, topologies, I/O controller or switch architectures, and system-level software optimizations. To address such a huge gap, we introduce OpenSUN, a novel FPGA-based multi-node system that supports customizable architecture and software systems. Its baseline architecture integrates a full-stack design, encompassing I/O controllers, switches, protocol stacks, and software systems. These components are all accessible through user-friendly interfaces at each layer to enable agile prototyping of novel hardware and software designs. By providing this open, community-accessible platform, OpenSUN aims to foster exploration and innovation in next-generation scale-up interconnect systems.

## 中文摘要

摩尔定律的放缓，加之大数据应用与生成式 AI 不断攀升的计算需求，正在加速 scale-up 系统的发展。与传统的 scale-out 架构不同，scale-up 系统通常使用基于高带宽、load/store 语义的互连（如 CXL、UALink、NVLink 和 UnifiedBus）在多个节点之间扩展共享内存。设计与优化此类互连系统是一项涉及计算机体系结构、互连技术与软件系统的多方面挑战。尽管业界已推出众多商用方案，学术界仍缺乏一个开源、基于硬件的平台来支持跨栈研究，例如探索新的协议、拓扑、I/O 控制器或交换架构，以及系统级软件优化。为填补这一巨大空白，我们提出 OpenSUN，一个新颖的基于 FPGA 的多节点系统，支持可定制的体系结构与软件系统。其基线架构集成了全栈设计，涵盖 I/O 控制器、交换机、协议栈与软件系统。这些组件均可在各层通过用户友好的接口访问，从而支持新型软硬件设计的敏捷原型验证。通过提供这一开放的、社区可访问的平台，OpenSUN 旨在促进下一代 scale-up 互连系统的探索与创新。
