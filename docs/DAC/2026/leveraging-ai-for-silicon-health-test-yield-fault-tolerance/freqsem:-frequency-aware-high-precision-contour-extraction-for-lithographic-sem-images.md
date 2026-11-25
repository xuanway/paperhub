FreqSEM: Frequency-Aware High-Precision Contour Extraction for Lithographic SEM Images
Authors：
[xiaoyan Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=45029206960967856181)，[Yumeng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4120167747330178135)，[Qian Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=2774920537619914195)，[Qi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=073843)，[Cheng Zhuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=204443)

## 中文标题

FreqSEM：面向光刻 SEM 图像的频率感知高精度轮廓提取

## 英文摘要

In semiconductor manufacturing, contour extraction from scanning electron microscope (SEM) images is essential for accurate lithographic metrology and process optimization. However, the low contrast, high noise, and complex structures of SEM images lead to blurred contours, making precise contour extraction extremely challenging. Existing methods struggle to capture detailed geometric features and fail to meet the high-precision requirements. In this paper, we propose FreqSEM, a frequency-aware contour extraction framework that achieves sub-nanometer-level precision, incorporating Fast Fourier Transform (FFT) for edge feature enhancement and Segment Anything Model 2 (SAM2) for edge localization. To exploit the characteristics of different frequency bands, we first apply FFT to extract the low-and mid-frequency components of the input image. Subsequently, the low-frequency component, which preserves the overall brightness distribution and large-scale structures, is used to generate SEM-adapted prompts for SAM2. Meanwhile, the mid-frequency component, which retains edges, textures, and other fine-scale details, is injected into the image encoder to enhance edge representation. In terms of the training strategy, to further enhance SAM2’s focus on edges, we design an edge-aware loss function with a weight map emphasizing boundaries and a Sobel gradient loss. With limited training data, our method achieves an EPE mean of only 0.334 nm and a standard deviation of 0.661 nm at the minimum line width of 81 nm, significantly outperforming existing approaches.

## 中文摘要

在半导体制造中，从扫描电子显微镜（SEM）图像中提取轮廓对于精确的光刻量测与工艺优化至关重要。然而，SEM 图像的低对比度、高噪声与复杂结构会导致轮廓模糊，使精确轮廓提取极具挑战性。现有方法难以捕捉细节几何特征，无法满足高精度要求。本文提出 FreqSEM，一个达到亚纳米级精度的频率感知轮廓提取框架，融合快速傅里叶变换（FFT）进行边缘特征增强，并采用 Segment Anything Model 2（SAM2）进行边缘定位。为利用不同频段的特性，我们首先对输入图像施加 FFT 以提取其低、中频分量。随后，保留整体亮度分布与大尺度结构的低频分量被用于生成适配 SEM 的提示以驱动 SAM2；而保留边缘、纹理等细尺度细节的中频分量则被注入图像编码器以增强边缘表征。在训练策略方面，为进一步增强 SAM2 对边缘的关注，我们设计了带有强调边界权重图与 Sobel 梯度损失的边缘感知损失函数。在有限训练数据下，我们的方法在 81 nm 最小线宽处实现了仅 0.334 nm 的 EPE 均值与 0.661 nm 的标准差，显著优于现有方法。
