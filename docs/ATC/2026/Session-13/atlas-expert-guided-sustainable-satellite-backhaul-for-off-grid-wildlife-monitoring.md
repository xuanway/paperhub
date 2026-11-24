# ATLAS: Expert-Guided Sustainable Satellite Backhaul for Off-Grid Wildlife Monitoring

**中文标题**：ATLAS：面向离网野生动物监测的专家引导可持续卫星回传

**所属 Session**：[Session 13: Mobile, Edge and Embedded systems](index.md) · [ATC 2026](../index.md)

**作者**：Hao Fang (Simon Fraser University), Miao Zhang (Simon Fraser University), Haoyuan Zhao (Simon Fraser University), Long Chen (Simon Fraser University), Yi Ching Chou (Simon Fraser University), Chi Xu (Simon Fraser University), Cheng Pan (Simon Fraser University), Jiangchuan Liu (Simon Fraser University)

## 英文摘要
Remote wildlife monitoring increasingly depends on high-fidelity cameras and sensors deployed far from grid power and terrestrial networks. Low Earth orbit satellite links can provide connectivity in these settings, but their high power draw and variable bandwidth, combined with intermittent on-site solar harvesting, make continuous backhaul infeasible. Current systems therefore filter at the edge, with motion triggers that waste limited energy and bandwidth on environmental artifacts, or fixed vision models that cannot follow evolving expert objectives. We present ATLAS, an expert-guided edge-to-cloud system that treats satellite backhaul as a scarce resource for off-grid wildlife monitoring. ATLAS uses foundation models to compile natural-language expert intent into semantic scoring logic, combines semantic relevance with environmental and energy state, and uses a constrained reinforcement-learning scheduler to decide which clips to upload and when. As a representative case study, we deployed ATLAS for over six months across 18 off-grid salmon-monitoring river sites. ATLAS achieves a mean clip-selection accuracy of 87.4%, exceeding mean baseline accuracy by 26.4 percentage points, while maintaining near-continuous operation through low-solar periods in which baselines incur 16.0% downtime.

## 中文摘要
远程野生动物监测日益依赖于部署在远离电网供电和地面网络之处的高保真摄像头与传感器。低地球轨道卫星链路可以在这些场景中提供连接，但其高功耗与带宽波动，加之现场太阳能采集的间歇性，使得持续回传不可行。因此现有系统在边缘侧进行过滤：由运动触发机制在环境伪影上浪费有限的能量与带宽，或使用无法跟随不断演化的专家目标的固定视觉模型。我们提出 ATLAS，一个专家引导的边缘到云系统，将卫星回传视为离网野生动物监测中的稀缺资源。ATLAS 使用基础模型将自然语言表达的专家意图编译为语义打分逻辑，把语义相关性与环境和能量状态相结合，并使用带约束的强化学习调度器决定上传哪些片段以及何时上传。作为一个代表性案例研究，我们在 18 个离网鲑鱼监测河流站点部署 ATLAS 超过六个月。ATLAS 取得 87.4% 的平均片段选择准确率，比基线平均准确率高 26.4 个百分点，同时在低日照时段仍维持近乎连续的运行，而基线在这些时段会产生 16.0% 的停机时间。

## 英文关键词
LEO satellite networks, foundation models, energy harvesting, edge computing, wildlife monitoring

## 中文关键词
LEO 卫星网络，基础模型，能量采集，边缘计算，野生动物监测

[返回 Session 13](index.md) · [返回 ATC 2026](../index.md)
