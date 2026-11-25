GPU-Fuzz: Finding Memory Errors in Deep Learning Frameworks
Authors：
[Zihao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=57095945671887581571)，[Hongyi Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7304838712342388648)，[Yanan Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=6829601179874686331)，[Zhenkai Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0769263537853147292)，[Shuai Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4833452633498763351)，[Fengwei Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=999143)

## 中文标题

GPU-Fuzz：发现深度学习框架中的内存错误

## 英文摘要

GPU memory errors are a critical threat to deep learning (DL) frameworks, leading to crashes or even security issues. We introduce GPU-Fuzz, a fuzzer locating these issues efficiently by modeling operator parameters as formal constraints. GPU-Fuzz utilizes a constraint solver to generate test cases that systematically probe error-prone boundary conditions in GPU kernels. Applied to PyTorch, TensorFlow, and PaddlePaddle, we uncovered 13 unknown bugs, demonstrating the effectiveness of GPU-Fuzz in finding memory errors.

## 中文摘要

GPU 内存错误是深度学习（DL）框架面临的严重威胁，会导致崩溃甚至引发安全问题。我们提出 GPU-Fuzz，一种将算子参数建模为形式化约束、从而高效定位此类问题的模糊测试工具。GPU-Fuzz 利用约束求解器生成测试用例，系统性地探查 GPU 内核中易出错的边界条件。将其应用于 PyTorch、TensorFlow 与 PaddlePaddle，我们发现了 13 个此前未知的缺陷，证明了 GPU-Fuzz 在发现内存错误方面的有效性。

## 英文关键词

GPU, Fuzzing, Deep Learning

## 中文关键词

GPU、模糊测试、深度学习
