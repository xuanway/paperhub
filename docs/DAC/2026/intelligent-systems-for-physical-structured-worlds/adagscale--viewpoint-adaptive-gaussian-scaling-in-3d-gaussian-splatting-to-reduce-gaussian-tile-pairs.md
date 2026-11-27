Adagscale: Viewpoint-Adaptive Gaussian Scaling in 3D Gaussian Splatting to Reduce Gaussian-Tile Pairs
Authors：
[Joongho Jo](https://63dac.conference-program.com/?post_type=page&p=15&uid=578343)，[Hyerin Lim](https://63dac.conference-program.com/?post_type=page&p=15&uid=831946190104466153)，[Hanjun Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=93450949180204140181)，[Jongsun Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=716143)

## 中文标题

AdaGScale：3D 高斯溅射中视角自适应的高斯缩放以减少高斯-瓦片对

## 英文摘要

Reducing the number of Gaussian-tile pairs is one of the most promising approaches to improve 3D Gaussian Splatting (3D-GS) rendering speed on GPUs. However, the importance difference existing among Gaussian-tile pairs has never been considered in the previous works. In this paper, we propose AdaGScale, a novel viewpoint-adaptive Gaussian scaling technique for reducing the number of Gaussian-tile pairs. AdaGScale is based on the observation that the peripheral tiles located far from Gaussian center contribute negligibly to pixel color accumulation. This suggests an opportunity for reducing the number of Gaussian-tile pairs based on color contribution. AdaGScale efficiently estimates the color contribution in the peripheral region of each Gaussian during a preprocessing stage and adaptively scales its size based on the peripheral score. As a result, Gaussians with lower importance intersect with fewer tiles during the intersection test, which improves rendering speed while maintaining image quality. The adjusted size is used only for tile intersection test, and the original size is retained during color accumulation to preserve visual fidelity. Experimental results show that AdaGScale achieves a geometric mean speedup of 13.8× over original 3D-GS on a GPU, with only about 0.5 dB degradation in PSNR on city-scale scenes.

## 中文摘要

减少高斯-瓦片对的数量是提升 GPU 上 3D 高斯溅射（3D-GS）渲染速度最有前景的途径之一。然而，先前工作从未考虑高斯-瓦片对之间存在的重要性差异。本文提出 AdaGScale，一种新颖的视角自适应高斯缩放技术，用于减少高斯-瓦片对的数量。AdaGScale 基于如下观察：位于远离高斯中心的边缘瓦片对像素颜色累积的贡献可以忽略。这表明存在依据颜色贡献减少高斯-瓦片对数量的机会。AdaGScale 在预处理阶段高效估计每个高斯外围区域的颜色贡献，并依据外围得分自适应地缩放其尺寸。由此，重要性较低的高斯在相交测试中与更少的瓦片相交，从而在保持图像质量的同时提升渲染速度。调整后的尺寸仅用于瓦片相交测试，在颜色累积阶段仍保留原始尺寸以维持视觉保真度。实验结果表明，AdaGScale 在 GPU 上相比原始 3D-GS 取得 13.8 倍的几何平均加速，在城市规模场景中 PSNR 仅下降约 0.5 dB。
