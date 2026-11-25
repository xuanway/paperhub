Mask-Guided Diffusion with Process-Aware Metric Optimization for Long-Tailed Wafer Defect Analysis
Authors：
[Yumeng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4120167747330178135)，[Qian Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=2774920537619914195)，[Xiaotian Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=25005485836236094381)，[Qi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=073843)，[Cheng Zhuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=204443)

## 中文标题

面向长尾晶圆缺陷分析的掩码引导扩散与工艺感知度量优化

## 英文摘要

In integrated circuit manufacturing, the detection of nanoscale wafer defects is critical for yield improvement and root-cause analysis. However, scanning electron microscopy (SEM) defect datasets in modern production lines are typically long-tailed, with pronounced intra-class diversity and subtle inter-class differences. Most existing methods do not take these properties into account, leading to low recall on tail defects and frequent confusion between categories. To address this, we propose DiffTail, a framework that combines mask-guided diffusion with process-aware metric optimization. The mask-guided diffusion uses defect masks together with SEM-specific prompts that encode defect knowledge to synthesize tail defects at specified locations and of specified types, while latent-space fusion with normal SEM images preserves process-consistent background textures. The process-aware metric optimization module groups class prototypes based on image features that are correlated with process steps. It then applies inter-cluster separation and margin-based constraints to easily confused class pairs, making visually similar defects easier to distinguish. Extensive experiments show that DiffTail improves tail-class detection and segmentation over state-of-the-art methods. To facilitate reproducibility, the dataset is available at https://github.com/YMLIU-BOOP/Anomaly-Dataset.

## 中文摘要

在集成电路制造中，纳米级晶圆缺陷的检测对于提升良率与根因分析至关重要。然而，现代产线中的扫描电子显微镜（SEM）缺陷数据集通常呈长尾分布，类内差异显著而类间差异细微。多数现有方法未考虑这些特性，导致尾部缺陷召回率偏低且类别之间频繁混淆。为此，我们提出 DiffTail，一个将掩码引导扩散与工艺感知度量优化相结合的框架。掩码引导扩散利用缺陷掩码以及编码缺陷知识的 SEM 专用提示，在指定位置合成指定类型的尾部缺陷，同时通过与正常 SEM 图像的隐空间融合保持与工艺一致的背景纹理。工艺感知度量优化模块依据与工艺步骤相关的图像特征对类别原型进行分组，然后对易混淆的类别对施加簇间分离与基于间隔的约束，使视觉相似的缺陷更易区分。大量实验表明，DiffTail 在尾部类别检测与分割上优于最先进方法。为便于复现，数据集可在 https://github.com/YMLIU-BOOP/Anomaly-Dataset 获取。
