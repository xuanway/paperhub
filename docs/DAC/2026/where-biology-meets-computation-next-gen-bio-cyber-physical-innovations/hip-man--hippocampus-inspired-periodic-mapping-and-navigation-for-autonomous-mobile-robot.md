HIP-MaN: Hippocampus-Inspired Periodic Mapping and Navigation for Autonomous Mobile Robot
Authors：
[Daeyoung Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=157595283054564414)，[Seonghan Kwon](https://63dac.conference-program.com/?post_type=page&p=15&uid=9205090772781226859)，[Seongsik Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=05295185152892840371)，[Hyunjae Jang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4200720861666041555)，[Jaewook Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=8451865661056184345)，[YeonJoo Jeong](https://63dac.conference-program.com/?post_type=page&p=15&uid=70800702169565753511)，[Inho Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=6114291778741087719)，[Jong-Kook Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=0251850855643177198)，[Jongkil Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=5553568371565001434)

## 中文标题

HIP-MaN：受海马体启发的自主移动机器人周期性建图与导航

## 英文摘要

Real-time path planning is essential for autonomous mobile robots operating in complex and dynamic real-world environments. Conventional path planning algorithms are limited by the need to store the entire environment map in memory and to maintain either the cost values of explored nodes or their connectivity relationships. Consequently, both memory and computational loads increase rapidly with the scale and complexity of the environment. This overhead is particularly exacerbated when replanning is frequent due to unpredictable dynamic obstacles. In this paper, we propose the hippocampus-inspired periodic mapping and navigation (HIP-MaN) algorithm. This employs multi-periodic grid modules to encode unique spatial locations as phase combinations, effectively compressing the entire environment into a compact periodic representation. HIP-MaN directly computes the goal direction based solely on the phase differences between grid modules and generates detours only when a collision is predicted, minimizing replanning costs. In a 200×200 𝑚2 environment, HIP-MaN demonstrates near-optimal path planning quality, showing only a 5-22% increase over the optimal path length while achieving 3-50× and 5-349× faster path generation in static and dynamic environments, respectively.

## 中文摘要

实时路径规划对于在复杂且动态的真实环境中运行的自主移动机器人至关重要。传统路径规划算法受限于必须将整个环境地图存储在内存中，并维护已探索节点的代价值或其连通关系。因此，内存与计算负载会随环境的规模和复杂度迅速增长。当由于不可预测的动态障碍物而需要频繁重规划时，这一开销尤为严重。本文提出受海马体启发的周期性建图与导航（HIP-MaN）算法。该方法采用多周期网格模块将唯一空间位置编码为相位组合，从而有效地将整个环境压缩为紧凑的周期性表示。HIP-MaN 仅依据网格模块之间的相位差直接计算目标方向，并且仅在预测到碰撞时才生成绕行路径，从而最小化重规划开销。在 200×200 m² 的环境中，HIP-MaN 展现出接近最优的路径规划质量，相较最优路径长度仅增加 5–22%，同时在静态和动态环境中分别实现 3–50× 和 5–349× 更快的路径生成速度。

## 英文关键词

Autonomous navigation, hippocampus-inspired periodic encoding, path planning, vicarious trial and error

## 中文关键词

自主导航、受海马体启发的周期编码、路径规划、替代性试错
