Cacheparallel: Comprehensively Exploring Multi-Level Acceleration for Diffusion Models
Authors：
[Qianru Lyu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4918779907883247987)，[Di Niu](https://63dac.conference-program.com/?post_type=page&p=15&uid=86104163714849453971)，[Jinwei Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4744310526395150287)，[Jingfei Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=72023393765765321021)，[Xiangrui Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5315084195328980343)，[Sheng ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=601243)，[Dongsheng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=49830934506801520661)

## 中文标题

Cacheparallel：全面探索扩散模型的多级加速

## 英文摘要

Diffusion models, despite their exceptional generative capabilities, are bottlenecked by slow inference owing to their complex architectures and multi-step iterative processes. Although caching is a promising acceleration method, previous approaches suffer from a tight coupling with specific network structures and low computational density. Moreover, caching is challenging to integrate with other methods to further enhance performance due to non-orthogonality, as simple integration often leads only to model performance degradation. To address these challenges, we propose CacheParallel, a novel training-free scheme that optimizes both caching and parallelism at the intra-and inter-step levels to reduce the computational load and increase the computational density simultaneously. We first introduced the fusion node to abstract the network structures into generic pre-fusion and post-fusion computational streams. For the pre-fusion stream, we applied intra-step caching optimized by the proposed CPS algorithm. For the post-fusion stream, we exploit inter-step output correlations to enable parallel computing and boost computational density. To mitigate accumulated errors and non-orthogonality issues, an error correction mechanism was designed based on our observation of the inherent linear correlations of the models. Comparative experiments showed that we achieved significant performance improvements across various models, with the peak improvement surpassing 100%.

## 中文摘要

扩散模型尽管具备卓越的生成能力，却因其复杂架构与多步迭代过程而受限于缓慢的推理速度。缓存虽是颇具前景的加速方法，但已有方法存在与特定网络结构紧耦合、计算密度低的问题；此外，由于非正交性，缓存难以与其他方法结合以进一步提升性能，简单集成往往只导致模型性能下降。为应对这些挑战，我们提出 CacheParallel，一种新颖的免训练方案，在步内与步间两个层面同时优化缓存与并行，从而在降低计算量的同时提升计算密度。我们首先引入融合节点，将网络结构抽象为通用的融合前与融合后计算流。对融合前计算流，我们采用由所提 CPS 算法优化的步内缓存；对融合后计算流，我们利用步间输出相关性实现并行计算并提升计算密度。为缓解累积误差与非正交性问题，基于我们对模型内在线性相关性的观察，设计了误差校正机制。对比实验表明，我们在多种模型上取得显著性能提升，峰值提升超过 100%。

## 英文关键词

Diffusion Model, Inference Accelerating, Cache, Parallel

## 中文关键词

扩散模型、推理加速、缓存、并行
