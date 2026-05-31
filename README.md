# 📚 PaperHub — AI 顶会论文笔记

> AI · LLM · NLP · CV 顶会论文解读，每篇 5 分钟读懂核心思想。

[![Site](https://img.shields.io/badge/网站-在线阅读-blue)](https://xuanway.github.io/paperhub/)
[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=flat&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

## 🌐 在线地址

**https://xuanway.github.io/paperhub/**

---

## 📂 项目结构

```
paperhub/
├── docs/                        # 📝 所有内容源文件（你只需维护这里）
│   ├── index.md                 #    首页
│   ├── ICLR2025/                #    会议目录
│   │   ├── index.md             #    会议首页
│   │   ├── llm_reasoning/       #    Track 分类
│   │   │   ├── index.md         #    分类首页
│   │   │   └── deepseek_r1.md   #    论文笔记
│   │   ├── multimodal_vlm/
│   │   └── llm_safety/
│   ├── CVPR2025/
│   └── ACL2025/
├── scripts/
│   └── new_paper.sh             # 🛠️ 快速创建新论文笔记
├── mkdocs.yml                   # ⚙️ 站点配置（导航、主题）
├── requirements.txt             # 📦 Python 依赖
└── .github/workflows/deploy.yml # 🚀 自动部署（push 后约1分钟生效）
```

> `site/` 目录是构建产物，由 GitHub Actions 自动生成，**无需关注，不提交**。

---

## ✏️ 添加新论文（3步）

### 第一步：生成模板文件

```bash
bash scripts/new_paper.sh <会议> <分类> <文件名> "论文标题"
```

示例：

```bash
bash scripts/new_paper.sh ICLR2025 llm_reasoning attention "Attention Is All You Need"
bash scripts/new_paper.sh CVPR2025 image_generation sdxl "SDXL: Improving Latent Diffusion Models"
```

脚本自动创建含完整结构的 `.md` 文件，并提示需要在 `mkdocs.yml` 中添加的导航条目。

### 第二步：编辑论文内容

打开生成的 `.md` 文件，填写论文链接、背景、方法、实验结果等。

### 第三步：注册导航 + 推送

在 `mkdocs.yml` 的 `nav:` 中添加条目，然后：

```bash
git add .
git commit -m "add: 论文标题"
git push
```

**推送后约 1 分钟，网站自动更新。**

---

## 🚀 本地预览

```bash
# 安装依赖（首次）
pip install -r requirements.txt

# 启动本地服务（实时热更新）
mkdocs serve
# 访问 http://127.0.0.1:8000
```

---

## 📊 当前收录

| 会议 | 篇数 | 分类 |
|------|------|------|
| ICLR 2025 | 7 | LLM推理 · 多模态VLM · LLM安全 |
| CVPR 2025 | 4 | 图像生成 · 3D视觉 |
| ACL 2025  | 2 | LLM/NLP |

## 📄 License

本项目内容采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 授权。
