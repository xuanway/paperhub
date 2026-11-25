DiffDEG: Diffusion-Enhanced Design Evolution Graph Representation Learning for Post-Layout Optimization
Authors：
[Jiajie Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0838899781460608536)，[Leilei Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=7543635217081755489)，[Ziyue Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=5610518292576155811)，[Yanlong Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3942193307632879032)，[Liangji Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3210164134302411508)，[Chenpu Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=35364257464496451741)，[Yunfan Zuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1606588320386281826)，[Lizheng Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=56305004533440999851)，[Hao Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=969143)，[Xingquan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=599243)，[Longxing Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=079143)

## 中文标题

DiffDEG：面向布局后优化的扩散增强设计演化图表征学习

## 英文摘要

Post-layout optimization is a critical step in modern chip design. However, existing Machine Learning (ML)-assisted methods struggle to capture the cross-stage reasoning dependencies that underlie the optimization challenges. While large language models (LLMs) excel at semantic reasoning, the lack of structural and physical awareness limits their effectiveness in post-layout optimization. To address these limitations, we propose DiffDEG, a diffusion-enhanced, reasoning-aware foundation model that bridges LLM-based semantic reasoning with circuit-level structural and physical representations. DiffDEG reformulates the conventional timing graph into a Design Evolution Graph (DEG), enabling cross-stage reasoning through text-annotated netlists. By leveraging directional diffusion and self-supervised pretraining, DiffDEG jointly interprets semantic, timing, and physical information, forming a unified representation adaptable to diverse optimization tasks. Experimental results show that DiffDEG consistently enhances optimization outcomes across multiple optimization paradigms, achieving an average 12.5% performance improvement and 4× speedup over commercial tools.

## 中文摘要

布局后优化是现代芯片设计中的关键步骤。然而，现有机器学习（ML）辅助方法难以刻画支撑这些优化难题的跨阶段推理依赖。尽管大语言模型（LLM）擅长语义推理，但其缺乏结构与物理感知，限制了其在布局后优化中的效果。为克服这些局限，我们提出 DiffDEG，一种扩散增强、具备推理感知的基础模型，将基于 LLM 的语义推理与电路级的结构与物理表征相桥接。DiffDEG 将传统时序图重构为设计演化图（DEG），通过带文本标注的网表实现跨阶段推理。借助方向性扩散与自监督预训练，DiffDEG 联合解读语义、时序与物理信息，形成可适配多种优化任务的统一表征。实验结果表明，DiffDEG 在多种优化范式下均能持续改善优化结果，相比商用工具平均实现 12.5% 的性能提升与 4 倍加速。
