STRAP-ViT: Segregated Tokens with Randomized - Transformations for Defense Against Adversarial Patches in ViTs
Authors：
[Nandish Chattopadhyay](https://63dac.conference-program.com/?post_type=page&p=15&uid=18255997981158768751)，[Anadi Goyal](https://63dac.conference-program.com/?post_type=page&p=15&uid=7047126149691868535)，[Chandan Karfa](https://63dac.conference-program.com/?post_type=page&p=15&uid=677343)，[Anupam Chattopadhyay](https://63dac.conference-program.com/?post_type=page&p=15&uid=022143)

## 中文标题

STRAP-ViT：基于随机复合变换的令牌隔离机制，用于防御 ViT 中的对抗补丁

## 英文摘要

Adversarial patches are physically realizable localized noise, which are able to hijack Vision Transformers (ViT) self-attention, pulling focus toward a small, high-contrast region and corrupting the class token to force confident misclassifications. In this paper, we claim that the tokens which correspond to the areas of the image that contain the adversarial noise, have different statistical properties when compared to the tokens which do not overlap with the adversarial perturbations. We use this insight to propose a mechanism, called STRAP-ViT, which uses Jensen-Shannon Divergence as a metric for segregating tokens that behave as anomalies in the Detection Phase, and then apply randomized composite transformations on them during the Mitigation Phase to make the adversarial noise ineffective. The minimum number of tokens to transform is a hyper-parameter for the defense mechanism and is chosen such that at least 50% of the patch is covered by the transformed tokens. STRAP-ViT fits as a non-trainable plug-and-play block within the ViT architectures, for inference purposes only, with a minimal computational cost and does not require any additional training cost/effort. STRAP-ViT has been tested on multiple pre-trained vision transformer architectures (ViT-base-16 [41] and DinoV2 [33]) and datasets (ImageNet [12] and CalTech-101 [27]), across multiple adversarial attacks (Adversarial Patch [3], LAVAN [24], GDPA [28] and RP2 [13]), and found to provide excellent robust accuracies lying within a 2 −3% range of the clean baselines, and outperform the state-of-the-art.

## 中文摘要

对抗补丁是可物理实现的局部噪声，能够劫持视觉 Transformer（ViT）的自注意力机制，将注意力拉向一个高对比度的小区域并污染类别令牌，从而强制产生高置信度的误分类。本文指出，与图像中包含对抗噪声的区域相对应的令牌，其统计特性与未与对抗扰动重叠的令牌存在差异。基于这一洞见，我们提出名为 STRAP-ViT 的机制：在检测阶段使用 Jensen-Shannon 散度作为度量，将表现为异常的令牌分离出来；随后在缓解阶段对其施加随机复合变换，使对抗噪声失效。需要变换的令牌最小数量是该防御机制的超参数，其选取准则是使被变换的令牌至少覆盖补丁面积的 50%。STRAP-ViT 可作为不可训练、即插即用的模块嵌入 ViT 架构之中，仅用于推理，计算开销极小，且无需任何额外训练成本或工作量。我们在多种预训练视觉 Transformer 架构（ViT-base-16 [41]与 DinoV2 [33]）和数据集（ImageNet [12]与 CalTech-101 [27]）上，针对多种对抗攻击（Adversarial Patch [3]、LAVAN [24]、GDPA [28]与 RP2 [13]）测试了 STRAP-ViT，发现其可提供优异的鲁棒精度，与干净基线相差在 2-3%范围内，并优于现有最先进方法。

## 英文关键词

Adversarial attacks, adversarial patches, defenses, ViT, Jensen-Shannon Divergence, Transformations

## 中文关键词

对抗攻击、对抗补丁、防御、ViT、Jensen-Shannon 散度、变换
