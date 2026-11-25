LLM-Enhanced Two-Stage Signal Temporal Logic Automatic Transformation with Structured Intermediate Representation
Authors：
[Hongjing Qing](https://63dac.conference-program.com/?post_type=page&p=15&uid=8713874267809184738)，[Jie An](https://63dac.conference-program.com/?post_type=page&p=15&uid=31675868122548528801)，[Fanjiang Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4106362531205195845)

## 中文标题

LLM 增强的两阶段信号时序逻辑自动转换：基于结构化中间表示

## 英文摘要

Signal Temporal Logic (STL) is a formal specification language for describing real-time and real-valued properties of Cyber-Physical Systems (CPS). Accurate and automatic translation of CPS specifications in natural language (NL) into formal STL formulas is crucial. Traditional methods that rely on manual templates or deep-learning models are limited in their flexibility. Recently, Large Language Model (LLM)-based methods have partially addressed these issues, but have not considered the usefulness of the inherent structure of STL for both the translation itself and the result evaluation. To address these issues, we propose STLGen, a novel LLM-enhanced automatic transformation framework from NL to STL, containing a two-stage generation process with a structured natural language, named NL2, as the intermediate representation. In Stage 1, NL is converted into well-defined NL2 through structured prompt engineering. In Stage 2, NL2 is converted into STL formulas using a converter. Leveraging LLM-aided generation and closed-loop verification with matching algorithms, as well as fine-tune models in two stages with instruction fine-tuning and LoRA. Additionally, we introduce two evaluation metrics: the structure accuracy to assess STL syntax impact on logic and the STL-SCOTES to evaluate semantic consistency via STL trajectories. Experimental results demonstrate that our method outperforms state-of-the-art methods across the classic evaluation metrics and our proposed metrics.

## 中文摘要

信号时序逻辑（STL）是一种用于描述信息物理系统（CPS）实时与实值性质的形式化规约语言。将自然语言（NL）描述的 CPS 规约准确、自动地转换为形式化 STL 公式至关重要。依赖人工模板或深度学习模型的传统方法灵活性有限。近来，基于大语言模型（LLM）的方法部分缓解了这些问题，但未考虑 STL 固有结构对转换本身以及结果评估的有用性。为解决这些问题，我们提出 STLGen，一种新颖的 LLM 增强的从 NL 到 STL 的自动转换框架，其两阶段生成过程以结构化自然语言（称为 NL2）作为中间表示。在第一阶段，通过结构化提示工程将 NL 转换为定义良好的 NL2。在第二阶段，使用转换器将 NL2 转换为 STL 公式。该框架借助 LLM 辅助生成与匹配算法闭环验证，并通过指令微调和 LoRA 在两阶段中微调模型。此外，我们引入两个评估指标：结构准确率，用于评估 STL 语法对逻辑的影响；以及 STL-SCOTES，通过 STL 轨迹评估语义一致性。实验结果表明，我们的方法在经典评估指标和我们提出的指标上均优于最先进方法。
