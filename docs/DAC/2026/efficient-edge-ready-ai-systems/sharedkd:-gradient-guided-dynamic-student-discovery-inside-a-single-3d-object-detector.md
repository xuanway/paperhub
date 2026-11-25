Sharedkd: Gradient-Guided Dynamic Student Discovery Inside a Single 3D Object Detector
Authors：
[Hyunjoon Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=8091390619527679019)，[Sangho An](https://63dac.conference-program.com/?post_type=page&p=15&uid=34394772600522909711)，[HYUNSUNG PARK](https://63dac.conference-program.com/?post_type=page&p=15&uid=2473953122228304572)，[Jangho Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=2781186893125451369)

## 中文标题

SharedKD：单一 3D 目标检测器内部梯度引导的动态学生网络发现

## 英文摘要

While state-of-the-art 3D object detectors achieve high accuracy, their computational cost hinders deployment. Knowledge Distillation (KD) offers compression, but existing methods use separate teacher-student networks, incurring memory overhead with static teachers that cannot adapt to student progress. We introduce SharedKD, unifying pruning and distillation within a single network. The full network acts as a dynamic teacher while a pruned sub-network serves as student, eliminating separate teachers, reducing memory, and enabling co-evolution for effective knowledge transfer. On nuScenes, SharedKD achieves 2.55% higher NDS than prior state-of-the-art at 75% pruning ratio, demonstrating exceptional accuracy-efficiency balance.

## 中文摘要

尽管最先进的 3D 目标检测器取得了高精度，但其计算开销阻碍了部署。知识蒸馏（KD）提供了压缩手段，但现有方法使用独立的教师-学生网络，静态教师带来内存开销，且无法适应学生的进展。我们提出 SharedKD，在单一网络内统一剪枝与蒸馏。完整网络充当动态教师，而剪枝后的子网络充当学生，从而消除独立教师、降低内存，并实现协同演化以有效迁移知识。在 nuScenes 上，SharedKD 在 75% 剪枝率下相比此前最先进方法取得高出 2.55% 的 NDS，展现出卓越的精度-效率平衡。

## 英文关键词

3D Object Detection, Knowledge Distillation, Model Compression, Network Pruning

## 中文关键词

3D 目标检测、知识蒸馏、模型压缩、网络剪枝
