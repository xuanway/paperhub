# NosRacer: Dynamic Detection of Race Conditions in On-Device Network Operating Systems

**中文标题**：NosRacer：端侧网络操作系统中竞态条件的动态检测

**所属 Session**：[Session 14: Networking I](index.md) · [ATC 2026](../index.md)

**作者**：Runze Wu (Nanjing University), Jingbo Zhai (Nanjing University), Shanming Ping (Huawei Technologies Co., Ltd), Lingzhi Ouyang (Huawei Technologies Co., Ltd), Hua Duan (Huawei Technologies Co., Ltd), Qin Zou (Huawei Technologies Co., Ltd), Chengcheng Huang (Huawei Technologies Co., Ltd), Bingshe Liu (Huawei Technologies Co., Ltd), Xudong Lang (Huawei Technologies Co., Ltd), Xiaoxing Ma (Nanjing University), Yu Huang (Nanjing University)

## 英文摘要
Commercial on-device network operating systems (NOSes) run the complex control planes of production routers and switches, where configuration update tasks are executed by multiple loosely coupled components through asynchronous message passing. Such executions are prone to race conditions: the same ordered input commands may produce different outcomes when messages are delivered in different orders. The race conditions are difficult to expose because they often manifest only as subtle, delayed malfunctions. Existing static analysis techniques lack scalability and precision for large-scale industrial NOSes, while dynamic ones incur substantial system-execution cost when attempting to cover the space of asynchronous message interleavings. To address the challenges above, we present NosRacer, a dynamic analysis framework for race condition detection in industrial-grade on-device NOSes. NosRacer uses a two-phase design. The concentration phase reduces analysis scope by leveraging the locality of configuration update tasks. Race condition detection is then limited to a small subset of involved components and crucial state variables, thereby reducing the detection cost. The perturbation phase proactively perturbs message asynchrony to increase the likelihood of executions with race-condition-exposing message interleavings. It keeps perturbation practical by grouping compatible perturbations for parallel execution and adaptively strengthening perturbations. We implement NosRacer in a commercial, actively developed NOS. NosRacer is integrated into the existing testing factory and used to detect race conditions in 5 key control-plane components. NosRacer achieves 66% precision and detects 21 race conditions confirmed by developers as severe bugs, while keeping the detection overhead below 10%.

## 中文摘要
商用端侧网络操作系统（NOS）运行着生产路由器与交换机的复杂控制平面，其中的配置更新任务由多个松耦合组件通过异步消息传递执行。这类执行容易出现竞态条件：相同的、有序的输入命令在消息以不同顺序投递时可能产生不同结果。竞态条件难以暴露，因为它们往往只表现为细微的、延迟出现的故障。现有静态分析技术对大规模工业级 NOS 缺乏可扩展性与精确性，而动态技术在试图覆盖异步消息交错空间时会产生巨大的系统执行开销。为应对上述挑战，我们提出 NosRacer，一个用于工业级端侧 NOS 中竞态条件检测的动态分析框架。NosRacer 采用两阶段设计。集中阶段利用配置更新任务的局部性来缩小分析范围，随后将竞态条件检测限制在少量相关组件和关键状态变量上，从而降低检测成本。扰动阶段主动扰动消息的异步性，以提高出现暴露竞态条件的消息交错的执行概率。它通过将相容的扰动分组并行执行、并自适应地加强扰动，使扰动保持实用。我们在一个商用且持续活跃开发的 NOS 中实现了 NosRacer。NosRacer 被集成到现有测试工厂中，用于检测 5 个关键控制平面组件中的竞态条件。NosRacer 达到 66% 的精确率，检测出 21 个被开发者确认为严重缺陷的竞态条件，同时将检测开销保持在 10% 以下。

## 英文关键词
on-device network operating systems, race conditions, dynamic analysis

## 中文关键词
端侧网络操作系统，竞态条件，动态分析

[返回 Session 14](index.md) · [返回 ATC 2026](../index.md)
