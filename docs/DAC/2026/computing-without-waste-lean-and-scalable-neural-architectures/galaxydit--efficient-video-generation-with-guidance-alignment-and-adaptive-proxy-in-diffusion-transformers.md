Galaxydit: Efficient Video Generation with Guidance Alignment and Adaptive Proxy in Diffusion Transformers
Authors：
[Zhiye Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=4655305953950005008)，[Steve Dai](https://63dac.conference-program.com/?post_type=page&p=15&uid=7724038937413332611)，[Ben Keller](https://63dac.conference-program.com/?post_type=page&p=15&uid=049143)，[Brucek Khailany](https://63dac.conference-program.com/?post_type=page&p=15&uid=149143)

## 中文标题

GalaxyDiT：扩散 Transformer 中基于引导对齐与自适应代理的高效视频生成

## 英文摘要

Diffusion models have revolutionized video generation, becoming essential tools in creative content generation and physical simulation. Transformer-based architectures (DiTs) and classifier-free guidance (CFG) are two cornerstones of this success, enabling strong prompt adherence and realistic video quality. Despite their versatility and superior performance, these models require intensive computation. Each video generation requires dozens of iterative steps, and CFG doubles the required compute. This inefficiency hinders broader adoption in downstream applications. We introduce GalaxyDiT, a training-free method to accelerate video generation with guidance alignment and systematic proxy selection for reuse metrics. Through rank-order correlation analysis, our technique identifies the optimal proxy for each video model, across model families and parameter scales, thereby ensuring optimal computational reuse. We achieve 1.87× and 2.37× speedup on Wan2.1-1.3B and Wan2.1-14B with only 0.97% and 0.72% drops on the VBench-2.0 benchmark. At high speedup rates, our approach maintains superior fidelity to the base model, exceeding prior state-of-the-art approaches by 5 to 10 dB in peak signal-to-noise ratio (PSNR).

## 中文摘要

扩散模型革新了视频生成，已成为创意内容生成与物理仿真中的关键工具。基于 Transformer 的架构（DiT）与无分类器引导（CFG）是这一成功的两大基石，带来了强大的提示词遵循能力与逼真的视频质量。尽管通用性强且性能优越，这些模型仍需密集计算。每次视频生成需要数十次迭代步骤，而 CFG 使所需计算量翻倍。这种低效阻碍了其在下游应用中的广泛采用。我们提出 GalaxyDiT，一种免训练方法，通过引导对齐与面向复用度量的系统性代理选择来加速视频生成。通过秩相关分析，我们的技术为每个视频模型在跨模型家族与参数规模上识别出最优代理，从而确保最优的计算复用。我们在 Wan2.1-1.3B 与 Wan2.1-14B 上分别取得 1.87× 与 2.37× 的加速，在 VBench-2.0 基准上仅有 0.97% 与 0.72% 的下降。在高加速比下，我们的方法对基础模型保持更高的保真度，峰值信噪比（PSNR）超过先前最先进方法 5 至 10 dB。
