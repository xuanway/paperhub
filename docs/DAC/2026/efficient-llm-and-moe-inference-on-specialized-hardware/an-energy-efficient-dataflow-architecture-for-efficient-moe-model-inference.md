An Energy-Efficient Dataflow Architecture for Efficient MoE Model Inference
Authors：
[Kexin Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=27424720768685963361)，[Qinggang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=40659363708189088741)，[Chuanhui Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=7504607848128423341)，[Shaoxian Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6956788222361518515)，[Wenkan Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9141800654478522694)，[Xiangzheng Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0822667844040910379)，[ruoshi li](https://63dac.conference-program.com/?post_type=page&p=15&uid=7880342379720871406)，[Bo Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=84853899950401413831)，[Long Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=976343)，[Xiaofei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=630243)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)

## 中文标题

一种面向高效 MoE 模型推理的节能数据流架构

## 英文摘要

The emerging Mixture-of-Experts (MoE) model sparsely activates a subset of experts for each token, causing each expert to process a varying number of tokens during inference. However, existing GPU-based MoE inference frameworks adopt a fixed tensor size for the inputs to each expert, requiring padding when an expert receives fewer tokens, which leads to substantial redundant computation and energy waste. In response, we propose FineMoE, a fine-grained dataflow accelerator for efficient MoE inference. We first present a token-stationary dataflow that uniformly abstracts the multiplication between an expert’s parameters and input tensors with varying token counts. Based on this dataflow, we design a reconfigurable systolic array and an adaptive memory subsystem to eliminate padding-incurred redundant computation. Evaluation demonstrates that our design outperforms two state-of-the-art GPU-based MoE inference frameworks, Hugging Face Transformers and vLLM, by 6.94× and 2.47× in terms of performance improvement, 14.37× and 7.74× in terms of energy savings, on average.

## 中文摘要

新兴的混合专家（MoE）模型为每个 token 稀疏激活一部分专家，使得各专家在推理过程中处理的 token 数量各不相同。然而，现有基于 GPU 的 MoE 推理框架将送入各专家的输入张量尺寸固定，当某专家收到的 token 较少时需要填充，从而造成大量冗余计算与能耗浪费。为此，我们提出 FineMoE，一种面向高效 MoE 推理的细粒度数据流加速器。我们首先提出 token 驻留数据流，将专家参数与 token 数各异的输入张量之间的乘法运算统一抽象。基于该数据流，我们设计了可重构脉动阵列与自适应存储子系统，以消除填充引入的冗余计算。评测表明，本设计平均优于两种最先进的基于 GPU 的 MoE 推理框架 Hugging Face Transformers 与 vLLM，性能分别提升 6.94× 和 2.47×，节能分别达到 14.37× 和 7.74×。
