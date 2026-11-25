Accelcim: Systematic Dataflow Exploration for SRAM Compute-in-Memory Accelerator
Authors：
[Chenhao Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=6114473025465496528)，[Yukun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0517269828742915713)，[An Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=93848846160645309421)，[Yuhui Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=19035657665257829471)，[Jinwei Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=2038380770735638427)，[Xiping Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=65596652255182769351)，[Yihan Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=37444029234770947011)，[Yuanpeng Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5107035644600839245)，[Tianyu Jia](https://63dac.conference-program.com/?post_type=page&p=15&uid=09291733440021619241)，[Wei Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=1838720167560119484)，[Qiang Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=938302086440658382)，[Xin Si](https://63dac.conference-program.com/?post_type=page&p=15&uid=06525473388796445)，[Jun Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=56313494407686411271)，[Guangyu Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=470243)

## 中文标题

AccelCIM：面向 SRAM 存内计算加速器的系统性数据流探索

## 英文摘要

SRAM-based compute-in-memory (CIM) offers high computational density and energy efficiency for deep neural network (DNN) accelerators, but its limited capacity causes on/off-chip data movement overhead for large DNN models. Existing CIM accelerator studies typically assume that DNN models fit entirely on-chip, leaving efficient dataflow design largely untapped. This paper introduces AccelCIM, a systematic dataflow exploration framework for SRAM CIM accelerator, which addresses two key limitations of prior work. (1) It formulates a systematic dataflow design space spanning CIM macro configurations and macro-array organizations. (2) It introduces rigorous design evaluation using cycle-accurate architectural simulation and post-layout PPA analysis. We conduct an extensive design space exploration and apply AccelCIM to representative LLM applications, providing practical insights for the principled design of CIM accelerators.

## 中文摘要

基于 SRAM 的存内计算（CIM）为深度神经网络（DNN）加速器提供了高计算密度与高能效，但其容量有限，对于大型 DNN 模型会带来片上/片外数据搬移开销。现有 CIM 加速器研究通常假设 DNN 模型可以完全放置于片上，使得高效的数据流设计在很大程度上未被充分挖掘。本文提出 AccelCIM，一个面向 SRAM CIM 加速器的系统性数据流探索框架，它针对先前工作的两个关键局限加以解决：（1）构建了涵盖 CIM 宏配置与宏阵列组织的系统性数据流设计空间；（2）引入了基于周期精确架构仿真与版图后 PPA 分析的严格设计评估。我们开展了广泛的设计空间探索，并将 AccelCIM 应用于典型的 LLM 应用，为 CIM 加速器的原理性设计提供了实用洞察。

## 英文关键词

Compute-in-Memory, Dataflow, Design Exploration

## 中文关键词

存内计算、数据流、设计空间探索
