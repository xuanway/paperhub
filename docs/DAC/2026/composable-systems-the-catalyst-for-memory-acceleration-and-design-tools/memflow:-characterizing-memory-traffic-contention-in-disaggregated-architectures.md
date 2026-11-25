Memflow: Characterizing Memory Traffic Contention in Disaggregated Architectures
Authors：
[Fujun He](https://63dac.conference-program.com/?post_type=page&p=15&uid=0533006987615085745)，[Tuo Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5468383550448145079)，[Huaxiang Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=8060410844110870894)，[Baolong Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=18392680468725586911)，[Zhihe Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1412637541034357209)，[Yishan Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=30635705768326433131)，[Xiabing Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=44953363894510535551)，[Linyi Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=63652316055897147601)，[Chuyue Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=00069764806423170071)，[Pingyi Huo](https://63dac.conference-program.com/?post_type=page&p=15&uid=42676508051899925821)，[Bin Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=647475770233978714)，[Yiming Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=89939299677020015631)，[Pengfei Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=63121042994144866101)，[Yunfei Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=13359701841362520231)

## 中文标题

MemFlow：解耦架构中内存流量竞争的刻画

## 英文摘要

Scale-up networks support memory semantics between pooled, disaggregated processor and memories; meanwhile, it triggers complex any-processor-to-any-memory accesses and creates intricate contention of micro-architectural components. Nevertheless, existing simulators fail to adequately characterize the interference due to oversimplified memory access paths. This paper presents the MemFlow simulator. MemFlow features a modular, fine-grained hardware abstraction of disaggregated memory systems, provides a flow-centric simulation scheme to trace the complete memory access path from load-store queues through cache hierarchies to memory controllers, evaluates micro-architectural contention with detail and fidelity, and enables automatic design space exploration to mitigate contention-induced performance degradation.

## 中文摘要

Scale-up 网络在池化的解耦处理器与内存之间支持内存语义；同时，它引发了复杂的任意处理器到任意内存的访问，并在微架构组件之间产生错综复杂的竞争。然而，现有模拟器由于对内存访问路径的过度简化，无法充分刻画这种干扰。本文提出 MemFlow 模拟器。MemFlow 具备面向解耦内存系统的模块化细粒度硬件抽象，提供以流为中心的仿真方案，可追踪从加载-存储队列经由缓存层次直至内存控制器的完整内存访问路径，细致而保真地评估微架构竞争，并支持自动设计空间探索，以缓解竞争引起的性能下降。

## 英文关键词

Scale-up fabric, disaggregated memory, system simulation, resource contention, traffic interference

## 中文关键词

Scale-up Fabric、解耦内存、系统仿真、资源竞争、流量干扰
