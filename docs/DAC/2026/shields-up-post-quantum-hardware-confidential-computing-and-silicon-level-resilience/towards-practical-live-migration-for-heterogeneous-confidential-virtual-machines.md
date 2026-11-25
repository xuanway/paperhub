Towards Practical Live Migration for Heterogeneous Confidential Virtual Machines
Authors：
[Jianquan CAI](https://63dac.conference-program.com/?post_type=page&p=15&uid=19532314951064775171)，[Xiaoxi Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=6078355849994297817)，[Shuang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9700402201061314367)，[Shoumeng Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=79763157630468271281)，[Kehuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=04895512941310029651)，[Yinqian Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=15825066542836906541)

## 中文标题

迈向实用的异构机密虚拟机在线迁移

## 英文摘要

The security properties and practical efficiency of Trusted Execution Environments (TEEs) have made them play an increasingly critical role in cloud computing, e.g., Confidential Virtual Machines (CVMs). However, TEE implementations, closely tied to specific hardware, introduce compatibility challenges for upper cloud services. In this paper, we focus on Live Migration, which is widely used in Normal Virtual Machines (NVMs) by Cloud Service Providers (CSPs) to manage computing resources, e.g., upgrading the host system without taking services into downtime. Currently, TEE vendor solutions support CVM migration only within homogeneous TEE stacks, without consideration of heterogeneous environments, rendering heterogeneous migration difficult or even impossible. To narrow the gap, we propose a generic framework applicable to various x86 TEEs, providing insights into achieving heterogeneous migration. In addition, we implement a migration system based on this framework that manages to achieve migration between AMD SEV and Hygon CSV by introducing a trusted migration agent with a specific design. The key idea is to emulate the required migration commands of the TEE firmware and resolve compatibility issues through a helper agent. Our prototype offers security guarantees comparable to homogeneous CVM migration, with experiments demonstrating acceptable performance overhead.

## 中文摘要

可信执行环境（TEE）的安全属性与实用效率使其在云计算中扮演愈发关键的角色，例如机密虚拟机（CVM）。然而，TEE 实现与特定硬件紧密绑定，给上层云服务带来兼容性挑战。本文关注在线迁移——云服务提供商（CSP）在普通虚拟机（NVM）中广泛使用该技术来管理计算资源，例如在不中断服务的情况下升级宿主机系统。目前，TEE 厂商方案仅支持同构 TEE 栈内的 CVM 迁移，未考虑异构环境，使异构迁移困难甚至不可行。为缩小这一差距，我们提出一个适用于多种 x86 TEE 的通用框架，为实现异构迁移提供思路。此外，我们基于该框架实现了一个迁移系统，通过引入经过特定设计的可信迁移代理，实现了 AMD SEV 与海光 CSV 之间的迁移。其核心思想是模拟 TEE 固件所需的迁移命令，并借助辅助代理解决兼容性问题。我们的原型提供与同构 CVM 迁移相当的安全保障，实验表明其性能开销可接受。
