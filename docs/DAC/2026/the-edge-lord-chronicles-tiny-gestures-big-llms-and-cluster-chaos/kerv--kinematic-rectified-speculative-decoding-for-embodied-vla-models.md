KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models
Authors：
[Zihao Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=5160323734301538912)，[Zhihao Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=956831177380211651)，[Maoliang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=99462478165816169271)，[Jiayu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=30680544300438791241)，[Xinhao Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=2288497629644863163)，[Zhaobo Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6998399930772038116)，[Donggang Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=30558183040260105511)，[Hong Mei](https://63dac.conference-program.com/?post_type=page&p=15&uid=39034041531407466601)，[Xiang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=114843)

## 中文标题

KERV：面向具身 VLA 模型的运动学校正推测解码

## 英文摘要

Vision-Language-Action (VLA) models build a token-domain robot control paradigm, yet suffer from low speed. Speculative Decoding (SD) is an optimization strategy that can boost inference speed. Two key issues emerge when integrating VLA and SD: first, SD relies on re-inference to address token errors, which is computationally expensive; second, to mitigate token errors, the acceptance threshold in SD requires careful adjustment. Existing works fail to address the above two issues effectively. Meanwhile, as the bridge between AI and the physical world, existing embodied intelligence has overlooked the application of robotic kinematics. To address these issues, we innovatively combine token-domain VLA models with kinematic-domain prediction for SD, proposing a kinematic-rectified SD framework named KERV. We employ a kinematics-based Kalman Filter to predict actions and compensate for SD errors, avoiding costly re-inference. Moreover, we design a kinematics-based adjustment strategy to dynamically rectify the acceptance threshold, addressing the difficulty of threshold determination. Experimental results across diverse tasks and environments demonstrate that KERV achieves 27%∼37% acceleration with nearly no Success Rate loss.

## 中文摘要

视觉-语言-动作（VLA）模型构建了 token 域的机器人控制范式，但其速度较低。推测解码（SD）是一种能够提升推理速度的优化策略。在将 VLA 与 SD 结合时会出现两个关键问题：第一，SD 依赖重新推理来处理 token 错误，计算代价高昂；第二，为缓解 token 错误，SD 中的接受阈值需要谨慎调整。现有工作未能有效解决上述两个问题。同时，作为 AI 与物理世界之间的桥梁，现有具身智能忽视了机器人运动学的应用。为解决这些问题，我们创新性地将 token 域 VLA 模型与运动学域预测相结合用于 SD，提出了名为 KERV 的运动学校正 SD 框架。我们采用基于运动学的 Kalman 滤波来预测动作并补偿 SD 误差，从而避免代价高昂的重新推理。此外，我们设计了一种基于运动学的调整策略来动态校正接受阈值，解决了阈值难以确定的问题。在多种任务与环境上的实验结果表明，KERV 实现了 27%~37%的加速，且成功率几乎无损。
