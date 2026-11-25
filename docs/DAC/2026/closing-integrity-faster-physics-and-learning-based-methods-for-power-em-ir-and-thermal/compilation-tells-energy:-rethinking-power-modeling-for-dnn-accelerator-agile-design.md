Compilation Tells Energy: Rethinking Power Modeling for DNN Accelerator Agile Design
Authors：
[Donger Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=9497603766328844512)，[Yihong Yi](https://63dac.conference-program.com/?post_type=page&p=15&uid=16823295126518831331)，[Xinheng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=7289402016402017285)，[Tianyi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=19552422455935491901)，[Jianwang Zhai](https://63dac.conference-program.com/?post_type=page&p=15&uid=36525870277041148421)，[Qi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=073843)，[Cheng Zhuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=204443)，[Hao Geng](https://63dac.conference-program.com/?post_type=page&p=15&uid=64456419866376934351)

## 中文标题

编译揭示能耗：面向 DNN 加速器敏捷设计的功耗建模再思考

## 英文摘要

RTL generators enable agile design of DNN accelerators, but the lack of early-stage power feedback forces designers to discover energy inefficiencies only after costly synthesis. Existing arch-level simulator-based approaches fall short for agile workflows: they require expertise and effort incompatible with rapid iteration. While machine learning struggles to capture software-hardware coupling, we reveal a key insight: compilation tells energy. Compiler toolchains in RTL generators already fuse workload and hardware characteristics—the coupling determining power. By extracting features from compiler IRs and multi-task learning, our methodology achieves practical accuracy through push-button workflows requiring no expertise. Validation on Gemmini and hls4ml demonstrates broad applicability, enabling true power-aware agile design.

## 中文摘要

RTL 生成器使 DNN 加速器的敏捷设计成为可能，但缺乏早期阶段的功耗反馈，迫使设计者只能在代价高昂的综合之后才发现能效低下的问题。现有的基于架构级模拟器的方法难以满足敏捷工作流的需求：它们所需的专业知识和投入与快速迭代不相容。机器学习难以刻画软硬件耦合，而我们揭示了一个关键洞见：编译揭示能耗。RTL 生成器中的编译器工具链已经融合了工作负载特征与硬件特征——正是这种耦合决定了功耗。通过从编译器 IR 中提取特征并结合多任务学习，我们的方法以无需专业知识的“一键式”工作流达到了实用精度。在 Gemmini 和 hls4ml 上的验证表明了其广泛的适用性，从而实现了真正的功耗感知敏捷设计。
