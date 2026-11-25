Early Design Stage Thermal Prediction and Optimization: Machine-Learning Driven Approach
Authors：
[Chanhee Jeon](https://63dac.conference-program.com/?post_type=page&p=15&uid=6218587149729931494)，[Munwon Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=93370297111047780931)，[Taewhan Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=152843)

## 中文标题

早期设计阶段的热预测与优化：机器学习驱动的方法

## 英文摘要

As semiconductor technologies continue to scale toward advanced nodes, the sharp increase in transistor density has led to a substantial rise in on-chip power density, making thermal effects a first-order design concern. Traditional thermal mitigation techniques (e.g., thermal-aware coarse-grained floorplanning, thermal-aware (post-route) cell adjustment, and structural cooling enhancements) suffer from thermal prediction inaccuracy or incur high fabrication cost, limiting their practical applicability to modern SoC designs. To overcome the limitation, in this work, we present an ML-based early-stage thermal prediction and mitigation framework that enables proactive thermal management in the course of physical design process. Precisely, our approach (1) predicts first the power density map which is the underlying source of thermodynamic behavior during the global placement stage using machine learning models, and then (2) accurately estimates the steady-state thermal map through a physics-guided thermal interpolation. The predicted temperature is subsequently leveraged by (3) an ML-model based optimization engine that adjusts the placement solution to minimize thermal hotspots without significant timing degradation. Experimental results demonstrate that our proposed model achieves 49.0% and 34.9% accuracy improvement in power density and thermal prediction, respectively, compared to tool estimation. When applied to thermal-aware placement optimization, the framework successfully reduces the maximum chip temperature by 9.97◦C while maintaining equivalent timing and area. These results confirm the effectiveness of our proposed early-stage thermal modeling and optimization framework in improving thermal reliability for modern power-hungry SoCs.

## 中文摘要

随着半导体工艺持续向先进节点演进，晶体管密度的急剧上升导致片上功耗密度大幅增加，使热效应成为首要的设计关注点。传统的热缓解技术（例如热感知的粗粒度布局规划、热感知的（布线后）单元调整以及结构散热增强）存在热预测不准确的问题，或者会带来高昂的制造成本，限制了其在现代 SoC 设计中的实际适用性。为克服这一局限，本文提出一个基于机器学习的早期阶段热预测与缓解框架，可在物理设计过程中实现主动的热管理。具体而言，我们的方法（1）首先利用机器学习模型在全局布局阶段预测功耗密度图，即热力学行为的根本来源；然后（2）通过物理引导的热插值精确估计稳态热图。随后，所预测的温度被（3）一个基于机器学习模型的优化引擎所利用，该引擎调整布局方案以最小化热点，同时不造成明显的时序退化。实验结果表明，与工具估计相比，我们提出的模型在功耗密度和热预测上的精度分别提升了 49.0% 和 34.9%。在应用于热感知布局优化时，该框架成功将芯片最高温度降低 9.97◦C，同时保持等效的时序与面积。这些结果证实了我们提出的早期阶段热建模与优化框架在提升现代高功耗 SoC 热可靠性方面的有效性。
