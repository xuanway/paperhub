From Fluid Dynamics to Chip Design: PDE Foundation Model Address Data Bottleneck in 3D-ICs Thermal Simulation
Authors：
[Zhen Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1665508775823554847)，[Xin HaiYang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1076125801810378406)，[Dongming Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6661813875612599854)，[yangbo wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=8944433000540625249)，[Hong Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=92360278314328459161)，[yang wenkai](https://63dac.conference-program.com/?post_type=page&p=15&uid=7870441973048407941)，[yu zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=571443)，[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Ting-Jung Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=1498611451604654405)，[lei he](https://63dac.conference-program.com/?post_type=page&p=15&uid=38121001066196586511)

## 中文标题

从流体力学到芯片设计：PDE 基础模型破解 3D-IC 热仿真的数据瓶颈

## 英文摘要

Machine learning can reduce 3D-ICs thermal analysis runtime from hours to seconds, yet most existing ML-based thermal models train each chip independently from scratch, demanding large datasets while failing to exploit the shared mathematical structure between heat conduction and diffusion-type Partial Differential Equations (PDEs). We demonstrate that PDE Foundation Models pretrained on diverse PDE families enable effective transfer to 3D-ICs thermal simulation. Building on this insight, we develop PNO-Therm, a specialized model obtained through targeted fine-tuning, which surpasses the previous state-of-the-art method using less than 20% of the training data. At equal dataset sizes, our method achieves 6– 10× lower MAE, 3.5× reduced GPU memory consumption, and over 3× faster training while maintaining ∼940× speedup compared to FEM solvers. Validated across three representative 3D-ICs designs, PNO-Therm establishes that Pretrained PDE Foundation Models provide a scalable pathway for high-accuracy thermal modeling under limited data.

## 中文摘要

机器学习可将 3D-IC 热分析的运行时间从数小时缩短至数秒，但现有大多数基于机器学习的热模型都对每颗芯片从零开始独立训练，既需要大规模数据集，又未能利用热传导与扩散类偏微分方程（PDE）之间共享的数学结构。我们证明，在多种 PDE 族上预训练的 PDE 基础模型能够有效迁移至 3D-IC 热仿真。基于这一发现，我们开发了 PNO-Therm，一个经针对性微调得到的专用模型，它仅使用不到 20% 的训练数据便超越了此前的最优方法。在相同数据集规模下，我们的方法使 MAE 降低 6–10×、GPU 显存占用降低 3.5×、训练速度提升 3 倍以上，同时相比 FEM 求解器仍保持约 940× 的加速。经三个具有代表性的 3D-IC 设计验证，PNO-Therm 表明预训练 PDE 基础模型为有限数据条件下的高精度热建模提供了一条可扩展的路径。

## 英文关键词

3D-ICs Thermal Simulation, Pretrained PDE Foundation Model, Fine-tuning, Data efficiency

## 中文关键词

3D-IC 热仿真、预训练 PDE 基础模型、微调、数据效率
