Thermal Stability Strategy for a 12nm/28nm Hybrid-Bonding Wafer-on-Wafer 3D-Integrated Eflash In-Memory Computing SoC
Authors：
[Guangyao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7778398097897781778)，[Saiya Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=870281263141727052)，[Yuexi Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=98467375582673789221)，[Jenny Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=00827293823556105611)，[Jing Kou](https://63dac.conference-program.com/?post_type=page&p=15&uid=97878627384712641711)，[Yizhe Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7811487006071414593)，[Jinhao Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=4533146396113527536)，[Yichen Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=694820160236160022)，[Yingming Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4807230755563606749)，[Wang Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=834143)

## 中文标题

面向 12nm/28nm 混合键合晶圆对晶圆三维集成 eFlash 存内计算 SoC 的热稳定性策略

## 英文摘要

3D In-memory Computing (IMC) chips, with high density and bandwidth, offer a promising solution for AI workloads but suffer from thermal instability, which degrades weight precision and system throughput. This work proposes a cross-layer thermal stability strategy (TSS) and validates it on a 3D eFlash analog IMC prototype with hybrid bonding, integrating a 12nm logic die and a 28nm eFlash die (36MB). TSS consists of: (1) a physics-guided thermal model achieving a kullback-leibler divergence of 0.088; (2) a temperature-insensitive differential programming (TIDP) scheme that stabilizes weights from –30°C to 60°C; and (3) an adaptive temperature calibration (ATC) algorithm that reduces output error standard deviation by 60.7%. With TSS, ResNet-18 and DCCRN maintain robust inference on the 3D eFlash IMC SoC across –15°C to 75°C with less than 10% degradation in end-to-end task accuracy. This is the first demonstration of thermally resilient analog IMC on a commercial-grade 3D SoC, paving the way for reliable AI deployment under dynamic thermal conditions.

## 中文摘要

三维存内计算（IMC）芯片具有高密度与高带宽，为 AI 负载提供了颇具前景的解决方案，但受热不稳定性困扰，会降低权重精度与系统吞吐率。本工作提出一种跨层热稳定性策略（TSS），并在采用混合键合、集成 12nm 逻辑裸片与 28nm eFlash 裸片（36MB）的三维 eFlash 模拟 IMC 原型上对其进行验证。TSS 包括：(1) 物理引导的热模型，其 KL 散度达到 0.088；(2) 温度不敏感的差分编程（TIDP）方案，可将权重在 –30°C 至 60°C 范围内保持稳定；(3) 自适应温度校准（ATC）算法，将输出误差标准差降低 60.7%。借助 TSS，ResNet-18 与 DCCRN 在该三维 eFlash IMC SoC 上于 –15°C 至 75°C 范围内保持稳健推理，端到端任务精度下降小于 10%。这是首次在商用级三维 SoC 上实现热韧性模拟 IMC 的演示，为动态热条件下的可靠 AI 部署铺平了道路。

## 英文关键词

3D in-memory computing; thermal stability strategy; thermal modeling; temperature-insensitive differential programming; adaptive temperature calibration

## 中文关键词

三维存内计算、热稳定性策略、热建模、温度不敏感差分编程、自适应温度校准
