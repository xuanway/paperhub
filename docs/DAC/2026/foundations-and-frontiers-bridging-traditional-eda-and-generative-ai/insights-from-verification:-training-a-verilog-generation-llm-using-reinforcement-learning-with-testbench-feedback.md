Insights from Verification: Training a Verilog Generation LLM Using Reinforcement Learning with Testbench Feedback
Authors：
[Ning Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0664891654584882089)，[Bingkun Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6337424854460121618)，[Jie Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=38479733992353397501)，[Yuchen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4116076772303443402)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)

## 中文标题

来自验证的洞见：利用带测试平台反馈的强化学习训练 Verilog 生成 LLM

## 英文摘要

Large language models (LLMs) have achieved strong results in software programming tasks, which motivates their application to hardware design, especially in generating Verilog code from natural language specifications. Existing methods mainly use instruction tuning, which optimizes token-level probability and does not match the need for functional correctness in Verilog generation. To address this, we use reinforcement learning (RL) with feedback from verification tools, so that the training objective directly reflects functional correctness. RL training with verification feedback is limited by the lack of functional verification code, or testbenches. To solve this, we propose an automatic testbench generation framework that addresses the problems of hallucination and low coverage in LLM-generated testbench by decomposing the task and using additional information from electronic design automation tools. We then train Verilog generation LLMs using reinforcement learning with testbench feedback, achieving state-of-the-art performance. Our method gives consistent gains across different base models and open-source Verilog generation LLMs, showing its generalizability. All datasets, codes, and models are released to support further research in this area. Code: https://github.com/CatIIIIIIII/VeriPrefer, Datasets & Models: https://huggingface.co/collections/LLM-EDA/ veriprefer-680638c8322b87d6d0efc208

## 中文摘要

大语言模型（LLM）在软件编程任务上已取得显著成果，这推动其应用于硬件设计，尤其是从自然语言规约生成 Verilog 代码。现有方法主要采用指令微调，它优化的是 token 级概率，与 Verilog 生成对功能正确性的需求并不匹配。为此，我们采用以验证工具反馈为依据的强化学习（RL），使训练目标直接反映功能正确性。然而，基于验证反馈的 RL 训练受制于功能验证代码（即测试平台，testbench）的匮乏。为解决这一问题，我们提出一种自动测试平台生成框架：通过任务分解并利用电子设计自动化工具提供的额外信息，缓解 LLM 生成测试平台中的幻觉与覆盖率偏低问题。随后，我们使用带测试平台反馈的强化学习训练 Verilog 生成 LLM，取得了最先进的性能。我们的方法在不同基座模型与开源 Verilog 生成 LLM 上均带来一致的提升，体现了其泛化能力。所有数据集、代码与模型均已公开，以支持该领域的后续研究。代码：https://github.com/CatIIIIIIII/VeriPrefer，数据集与模型：https://huggingface.co/collections/LLM-EDA/ veriprefer-680638c8322b87d6d0efc208
