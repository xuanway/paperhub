SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference
Authors：
[Shanghao Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=36810721806718787901)，[Renze Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=75592520693113494461)，[Size Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=826066383180774724)，[Yuanqiang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=02117766804852467511)，[Yun (Eric) Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=124143)，[Hailong Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3511559864376114608)

## 中文标题

SPADE：面向视频扩散模型快速推理的输入自适应稀疏注意力引擎

## 英文摘要

Video diffusion transformers (vDiTs) generate high quality but pay quadratic self-attention cost, making inference prohibitive at video-token scales. The challenge is input-adaptive sparsity: selecting critical Q/K/V tokens with negligible overhead and executing them for end-to-end gains. We present SPADE, a training-free sparse-attention engine of three parts: (i) vDiT-SSR, spec defining 3D blocking candidates and formalizing dynamic masks via Summarizer/Estimator expressions; (ii) runtime scheme generation using SICS and a head-wise policy; and (iii) an executor with low-overhead index search, flash block-sparse attention, and kernel grouping. Across Hunyuan-Video, Wan 2.1/2.2 (T2V/I2V), SPADE raises sparsity and speed and preserves quality, accelerating attention 2.26×–3.40× and end-to-end 1.49×–1.80×. Our code is open-sourced at https://github.com/6somehow/DAC-SPADE.

## 中文摘要

视频扩散 Transformer（vDiT）能生成高质量内容，但需付出二次方自注意力代价，使得在视频 token 规模下推理代价过高。其挑战在于输入自适应稀疏性：以可忽略的开销选出关键 Q/K/V token，并在其上执行以获取端到端收益。我们提出 SPADE，一个无需训练的稀疏注意力引擎，包含三部分：(i) vDiT-SSR，一种规范，定义三维分块候选并通过 Summarizer/Estimator 表达式形式化动态 mask；(ii) 使用 SICS 和按头策略的运行时方案生成；以及 (iii) 具备低开销索引搜索、flash 块稀疏注意力与 kernel 分组的执行器。在 Hunyuan-Video、Wan 2.1/2.2（T2V/I2V）上，SPADE 同时提升了稀疏度与速度并保持质量，注意力加速 2.26×–3.40×，端到端加速 1.49×–1.80×。我们的代码已开源于 https://github.com/6somehow/DAC-SPADE。

## 英文关键词

video diffusion transformers, sparse attention

## 中文关键词

视频扩散 Transformer、稀疏注意力
