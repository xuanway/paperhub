# 📚 AI Paper Notes (PaperHub)

> AI · LLM · NLP · CV 顶会论文解读，每篇 5 分钟读懂核心思想。

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=flat&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

## 🌐 在线阅读

本地运行：`mkdocs serve`，然后访问 [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📊 会议覆盖

| 会议 | 论文数 | 链接 |
|------|-------|------|
| ICLR 2025 | 7 | [docs/ICLR2025/](docs/ICLR2025/) |
| CVPR 2025 | 4 | [docs/CVPR2025/](docs/CVPR2025/) |
| ACL 2025 | 2 | [docs/ACL2025/](docs/ACL2025/) |

## 🔍 研究领域

- 💡 LLM 推理
- 🔒 LLM 安全
- 🧩 多模态 VLM
- 🎨 图像生成
- 🧊 3D 视觉
- 💬 LLM/NLP

## 📂 目录结构

```
docs/
├── index.md                     # 总索引（首页）
├── ICLR2025/
│   ├── index.md                 # 会议索引
│   ├── llm_reasoning/           # LLM 推理
│   ├── multimodal_vlm/          # 多模态 VLM
│   └── llm_safety/              # LLM 安全
├── CVPR2025/
│   ├── index.md
│   ├── image_generation/        # 图像生成
│   └── 3d_vision/               # 3D 视觉
└── ACL2025/
    ├── index.md
    └── llm_nlp/                 # LLM/NLP
```

## 🚀 快速开始

### 安装依赖

```bash
pip install mkdocs-material mkdocs-minify-plugin
```

### 本地预览

```bash
mkdocs serve
```

### 构建静态站点

```bash
mkdocs build
```

### 部署到 GitHub Pages

```bash
mkdocs gh-deploy
```

## 📝 添加新笔记

1. 在对应会议/领域目录下创建 Markdown 文件
2. 添加 frontmatter（title, description, tags）
3. 在该领域的 `index.md` 中添加链接
4. 在 `mkdocs.yml` 的 `nav` 中注册页面

### 论文笔记模板

```markdown
---
title: "论文标题（中文）"
description: "一句话描述论文贡献。会议名称 论文解读。"
tags:
  - "研究领域"
  - "关键词"
  - "会议名称"
---

# 论文英文标题

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">一句话摘要。</p>
<p class="paper-seo-summary__tags">会议 · 领域 · 关键词</p>
</div>

**论文链接**：[arXiv XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)  
**机构**：XXX  
**发表**：会议名称

---

## 一句话总结

## 背景与动机

## 方法详解

## 实验结果

## 核心亮点

## 局限性
```

## 📄 License

本项目内容采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 授权。
