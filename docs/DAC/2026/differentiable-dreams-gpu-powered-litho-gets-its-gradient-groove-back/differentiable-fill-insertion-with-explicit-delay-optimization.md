Differentiable Fill Insertion with Explicit Delay Optimization
Authors：
[Jinoh Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=10107211407801784451)，[Jinmo Ahn](https://63dac.conference-program.com/?post_type=page&p=15&uid=4361398012964788055)，[Jakang Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=5677653421837975373)，[Jaeseung Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=00189960716399667871)，[Seonghyeon Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=352843)，[Seokhyeong Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=775743)

## 中文标题

显式优化延迟的可微分填充插入

## 英文摘要

Fill insertion is an essential step in achieving planar topography during chip fabrication. Its primary objective is to ensure metal density uniformity, but it is also important to minimize signal delay. Existing algorithms reduce such delay implicitly by minimizing proxy objectives (e.g., fill amount, overlays between fills and wires, and capacitance) but there remains a misalignment between proxy reduction and actual delay improvement. To address this, we propose DiffFill, a novel differentiable framework for fill insertion that explicitly optimizes not only uniformity but also delay. At the heart of DiffFill is the CapFormer, a Transformer-based capacitance extractor. During each optimization step, CapFormer predicts the expected fill-induced capacitance for each wire based on the current fillable regions. These capacitance values are subsequently used to formulate a differentiable delay objective based on the Elmore delay model. With this approach, DiffFill achieves significant improvements of 8.9% and 8.8% in TNS and WNS, respectively, compared to state-of-the-art methods.

## 中文摘要

填充插入是芯片制造过程中实现平面形貌的关键步骤。其主要目标是保证金属密度均匀性，但最小化信号延迟同样重要。现有算法通过最小化代理目标（例如填充量、填充与布线之间的重叠以及电容）来间接降低此类延迟，但代理指标的下降与实际延迟改善之间仍存在错位。为解决这一问题，我们提出 DiffFill，一种新颖的可微分填充插入框架，它不仅显式优化均匀性，还显式优化延迟。DiffFill 的核心是 CapFormer，一个基于 Transformer 的电容提取器。在每次优化步骤中，CapFormer 根据当前可填充区域预测每条布线由填充引入的预期电容。这些电容值随后被用于构建基于 Elmore 延迟模型的可微分延迟目标。借助该方法，DiffFill 相比最先进方法在 TNS 和 WNS 上分别取得了 8.9% 和 8.8% 的显著提升。
