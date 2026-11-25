AMS Layout Automation Using Circuit-Level Analog Standard Cells and Self-Biasing Techniques in Digital PnR Tools.
Authors：
[Wonsik Oh](https://63dac.conference-program.com/?post_type=page&p=15&uid=783594172710404855)，[Luke Theogarajan](https://63dac.conference-program.com/?post_type=page&p=15&uid=4455885220050979894)

## 中文标题

基于电路级模拟标准单元与自偏置技术的数字 PnR 工具 AMS 版图自动化

## 英文摘要

This work presents a silicon-verified analog-mixed-signal (AMS) layout-automation framework that integrates a circuit-level analog standard-cell (CLAS) library and self-biasing circuits within a digital place-and-route (PnR) environment. Unlike prior transistor-level stem-cell approaches, the CLAS library standardizes matched circuit-level blocks such as self-biased amplifiers, current mirrors, and delay cells compatible with digital cell specifications. Functionally verified CMOS chips fabricated in 180-nm and 65-nm CMOS nodes demonstrate the power of fully automated, DRC/LVS-clean layouts generated in Cadence Innovus for three benchmarks: a programmable current source, an adaptive-bandwidth PLL, and a probabilistic computer. All benchmarks show strong pre-/postlayout and silicon correlation, with the PLL exhibiting 0.98–1.50 ps simulated and 4.1 ps measured jitter. Across all benchmarks, the framework achieves 96 % area utilization, 14.4–69.5 % decoupling-capacitor area density, and <1 min runtime for block-level circuits and <1 hr for system-level designs. These results demonstrate efficient, scalable, and silicon-consistent AMS layout automation using standard digital design infrastructure.

## 中文摘要

本文提出一个经硅验证的模拟混合信号（AMS）版图自动化框架，它在数字布局布线（PnR）环境中集成了电路级模拟标准单元（CLAS）库与自偏置电路。与此前晶体管级主干单元（stem-cell）方法不同，CLAS 库将自偏置放大器、电流镜和延迟单元等匹配的电路级模块标准化，并与数字单元规格兼容。在 180 nm 和 65 nm CMOS 工艺节点上制造并完成功能验证的 CMOS 芯片，展示了在 Cadence Innovus 中为三个基准电路自动生成 DRC/LVS 干净的版图的能力：可编程电流源、自适应带宽 PLL 以及概率计算机。所有基准均表现出良好的版图前后及硅片相关性，其中 PLL 的仿真抖动为 0.98–1.50 ps，实测抖动为 4.1 ps。在所有基准上，该框架实现了 96%的面积利用率、14.4–69.5%的去耦电容面积密度，块级电路运行时间小于 1 分钟，系统级设计小于 1 小时。这些结果证明了利用标准数字设计基础设施实现高效、可扩展且与硅一致的 AMS 版图自动化。

## 英文关键词

Analog mixed-signal circuit, analog standard cell library, layout automation, place and route, self-biasing, physical design

## 中文关键词

模拟混合信号电路、模拟标准单元库、版图自动化、布局布线、自偏置、物理设计
