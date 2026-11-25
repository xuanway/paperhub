ESCAPE: Elegant Scan Chain Activity Probability Establishment for Programmable Low-Power LBIST
Authors：
[Hairui Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=43342064136762511481)，[Yumei Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=70494042798126043551)，[Xiaohui Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=9467035002627656062)，[Yaning Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=35117941100635791381)，[Yu Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=51037156837444102041)，[Zhouxing Su](https://63dac.conference-program.com/?post_type=page&p=15&uid=20159064953339855541)，[Zhipeng Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=4345225806492173643)，[Zezhong Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3655171435165547375)，[Xing Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5543975171238546414)

## 中文标题

ESCAPE：面向可编程低功耗 LBIST 的扫描链活动概率精巧构建

## 英文摘要

Logic built-in self-test (LBIST) suffers from excessive power consumption due to high toggling rates caused by pseudo-random patterns. This paper presents an Elegant Scan Chain Activity Probability Establishment (ESCAPE) architecture for programmable low power LBIST. The proposed approach enables fine-grained, differentiated control over scan chain activation probabilities under arbitrary user-specified power constraints, thereby improving fault coverage. In the designed low-power control circuit, a programmable probability generator periodically outputs a user-configurable sequence of probabilities to drive hold registers. A 2D AND-gate array formed by two groups of hold registers then produces a rich set of low-power control signals. By modulating the enable probability of the lockups situated before the phase shifter, this mechanism achieves precise per-chain power management. Experimental results on industrial-scale designs demonstrate that, under identical power constraints, the proposed method achieves more than 1% higher fault coverage compared to commercial tools and state-of-the-art approaches, while simultaneously reducing peak power consumption and incurring lower hardware overhead.

## 中文摘要

逻辑内建自测试（LBIST）因伪随机图样引起的高翻转率而存在功耗过高的问题。本文提出一种扫描链活动概率精巧构建（ESCAPE）架构，用于可编程低功耗 LBIST。所提方法能够在任意用户指定的功耗约束下，对扫描链激活概率实现细粒度、差异化的控制，从而提升故障覆盖率。在所设计的低功耗控制电路中，可编程概率生成器周期性地输出用户可配置的概率序列以驱动保持寄存器；随后由两组保持寄存器构成的二维 AND 门阵列产生丰富的低功耗控制信号。通过调制位于移相器之前的锁存器的使能概率，该机制实现了精确的逐链功耗管理。在工业规模设计上的实验结果表明，在相同功耗约束下，所提方法相较商业工具与最先进方法故障覆盖率高出 1% 以上，同时降低峰值功耗并具有更低的硬件开销。

## 英文关键词

LBIST, low-power test, scan chain control, ATPG, power optimization

## 中文关键词

LBIST、低功耗测试、扫描链控制、ATPG、功耗优化
