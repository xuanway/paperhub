Cupilot: A Strategy-Coordinated Multi-Agent Framework for CUDA Kernel Evolution
Authors：
[Jinwu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=35369994320938147921)，[Qidie Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=50426431446985422921)，[Bin Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6949423476604160739)，[Lin Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=64072387661026692941)，[Xin Si](https://63dac.conference-program.com/?post_type=page&p=15&uid=06525473388796445)，[Yang Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2905300192189786719)，[Jun Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=094443)

## 中文标题

cuPilot：面向 CUDA 内核进化的策略协同多智能体框架

## 英文摘要

Optimizing CUDA kernels is a challenging and labor-intensive task, given the need for hardware-software co-design expertise and the proprietary nature of high-performance kernel libraries. While recent large language models (LLMs) combined with evolutionary algorithms show promise in automatic kernel optimization, existing approaches often fall short in performance due to their suboptimal agent designs and mismatched evolution representations. This work identifies these mismatches and proposes cuPilot, a strategy-coordinated multi-agent framework that introduces strategy as an intermediate semantic representation for kernel evolution. Key contributions include a strategy-coordinated evolution algorithm, roofline-guided prompting, and strategy-level population initialization. Experimental results show that the generated kernels by cuPilot achieve an average speed up of 3.09× over PyTorch on a benchmark of 100 kernels. On the GEMM tasks, cuPilot showcases sophisticated optimizations and achieves high utilization of critical hardware units. The generated kernels are open-sourced at https://github.com/champloo2878/cuPilot-Kernels.git.

## 中文摘要

优化 CUDA 内核是一项极具挑战且劳动密集的任务，既需要软硬件协同设计的专业知识，又受制于高性能内核库的专有性。近期将大语言模型（LLM）与进化算法相结合的方法在自动内核优化上展现出前景，但现有方法常因智能体设计欠佳与进化表示不匹配而性能不足。本文识别出这些不匹配问题，并提出 cuPilot，一种策略协同的多智能体框架，引入“策略”作为内核进化的中间语义表示。主要贡献包括策略协同进化算法、基于 roofline 的提示以及策略级种群初始化。实验结果表明，在包含 100 个内核的基准上，cuPilot 生成的内核相较 PyTorch 平均加速 3.09 倍。在 GEMM 任务上，cuPilot 展现出精巧的优化，并实现关键硬件单元的高利用率。所生成的内核已开源于 https://github.com/champloo2878/cuPilot-Kernels.git。

## 英文关键词

GPU Kernel, Multi-agent Framework, Evolution Algorithm

## 中文关键词

GPU 内核、多智能体框架、进化算法
