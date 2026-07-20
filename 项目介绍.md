
# 项目介绍 / Project Introduction

> 语言切换：点击目录跳转 → [中文版](#中文版) | [English Version](#english-version)

---

## 中文版

### 概述

**Content Moderation ECC** 是一个基于 ECC（Everything Claude Code）五层架构的智能内容审核 Skill，面向视频和文章两大类内容，实现从规则知识库到自主进化的完整闭环。

### ECC 五层架构

```
┌─────────────────────────────────────────────┐
│  Layer 5: 进化层                            │
│  新规则自动生成 · 跨平台规则迁移 · 版本管理  │
├─────────────────────────────────────────────┤
│  Layer 4: 迭代层                            │
│  误报修正 · 漏报补全 · 规则权重动态调整      │
├─────────────────────────────────────────────┤
│  Layer 3: 推理层                            │
│  多维度规则匹配 · 四级风险定级 · 审核报告    │
├─────────────────────────────────────────────┤
│  Layer 2: 记忆层                            │
│  审查案例库 · 误报记录 · 边界案例 · 进化日志 │
├─────────────────────────────────────────────┤
│  Layer 1: 知识库层                          │
│  法律法规合集 · 六大平台规则 · 违禁词库      │
└─────────────────────────────────────────────┘
```

### 知识库覆盖

#### 六大平台规则
| 平台 | 规则文件 | 核心覆盖 |
|------|----------|----------|
| 抖音 | `douyin.md` | 社区自律公约、暴力犯罪、色情低俗、虚假信息 |
| 快手 | `kuaishou.md` | 违规定级标准、黑灰产治理、网暴拦截 |
| B站 | `bilibili.md` | 创作公约、暑期专项、弹幕礼仪、二创规范 |
| 小红书 | `xiaohongshu.md` | 种草真实性、黑灰产矩阵号、同质化管控 |
| 视频号 | `wechat-video.md` | 账号注册、命名规范、直播连麦 |
| YouTube | `youtube.md` | 社区准则、Content ID、合理使用、选举误导 |

#### 四大法律法规
| 法规 | 文件 | 审核要点 |
|------|------|----------|
| 广告法 | `advertising-law.md` | 极限词清单、虚假广告、特殊行业限制 |
| 未成年人保护 | `minor-protection.md` | 防沉迷、禁止直播、个人信息保护 |
| 网络安全与数据 | `cybersecurity-data.md` | 违法信息禁止、深度合成标识、著作权 |
| 视听审核标准 | `content-review-standards.md` | 21类100条红线、违规处置标准 |

### 核心能力

| 能力 | 说明 |
|------|------|
| **多平台审查** | 一键对内容做抖音/B站/小红书等多平台合规评估 |
| **四级风险定级** | CRITICAL → HIGH → MEDIUM → LOW，精确匹配处置建议 |
| **自动化脚本** | `review.py` 支持违禁词扫描、极限词检测、敏感正则匹配 |
| **自主学习** | 每次审查自动存入案例库，构建违规类型索引 |
| **自主记忆** | 误报/漏报/边界案例分类归档，形成经验积累 |
| **自主迭代** | 误报 ≥ 3 次自动降低规则权重，漏报 ≥ 3 次提升敏感度 |
| **自助进化** | 从边界案例提取新规则，跨平台同步法规变更 |

### 审查维度矩阵

| 维度 | 依据 |
|------|------|
| 政治安全 | 网络安全法 + 视听审核标准第1-10条 |
| 色情低俗 | 广告法第9条 + 各平台公约 |
| 暴力恐怖 | 各平台社区公约 |
| 未成年人 | 未成年人网络保护条例 |
| 虚假信息 | 广告法第4条、第28条 |
| 侵权 | 著作权法 + 个人信息保护法 |
| 广告合规 | 广告法第9条 + 互联网广告管理办法 |
| AI生成内容 | 深度合成管理规定 |

### 项目结构

```
content-moderation-ecc/
├── SKILL.md                     # 核心文档（ECC架构总纲）
├── scripts/
│   └── review.py                # 审查脚本
└── references/
    ├── platforms/               # 6 个平台规则
    ├── laws/                    # 4 个法律法规
    └── memory/                  # 记忆与进化模块
        ├── review-log-template.md
        ├── case-library.md
        ├── false-positives.md
        ├── edge-cases.md
        ├── evolution-protocol.md
        └── evolution-log.md
```

---

## English Version

### Overview

**Content Moderation ECC** is an intelligent content moderation skill built on the ECC (Everything Claude Code) five-layer architecture, covering both video and article content types. It delivers a complete closed loop from rule knowledge base to autonomous evolution.

### ECC Five-Layer Architecture

```
┌─────────────────────────────────────────────┐
│  Layer 5: Evolution                         │
│  Auto rule generation · Cross-platform sync │
├─────────────────────────────────────────────┤
│  Layer 4: Iteration                         │
│  False positive fix · Missed detection fix  │
├─────────────────────────────────────────────┤
│  Layer 3: Inference                         │
│  Multi-rule matching · Risk grading · Report│
├─────────────────────────────────────────────┤
│  Layer 2: Memory                            │
│  Case library · False positives · Edge cases│
├─────────────────────────────────────────────┤
│  Layer 1: Knowledge Base                    │
│  Laws & regulations · 6 platform rules      │
└─────────────────────────────────────────────┘
```

### Knowledge Base Coverage

#### Six Platforms
| Platform | File | Key Coverage |
|----------|------|-------------|
| Douyin | `douyin.md` | Community guidelines, violence, pornography, misinformation |
| Kuaishou | `kuaishou.md` | Violation grading, black/gray market governance |
| Bilibili | `bilibili.md` | Creator code, youth protection, danmaku etiquette |
| Xiaohongshu | `xiaohongshu.md` | Review authenticity, matrix account governance |
| WeChat Video | `wechat-video.md` | Account registration, naming rules, livestream rules |
| YouTube | `youtube.md` | Community guidelines, Content ID, fair use, election misinformation |

#### Four Legal Frameworks
| Regulation | File | Review Focus |
|------------|------|-------------|
| Advertising Law | `advertising-law.md` | Absolute terms, false advertising, industry restrictions |
| Minor Protection | `minor-protection.md` | Anti-addiction, livestream ban, data protection |
| Cybersecurity & Data | `cybersecurity-data.md` | Illegal content, deepfake labeling, copyright |
| AV Content Standards | `content-review-standards.md` | 100 red lines across 21 categories |

### Core Capabilities

| Capability | Description |
|------------|-------------|
| **Multi-platform Review** | One-click compliance check across multiple platforms |
| **Four-tier Risk Grading** | CRITICAL → HIGH → MEDIUM → LOW with precise action items |
| **Automated Script** | `review.py` for banned words, absolute terms, regex scanning |
| **Autonomous Learning** | Every review auto-stored in case library with type indexing |
| **Autonomous Memory** | False positives, missed detections, edge cases systematically archived |
| **Autonomous Iteration** | Auto-lower weight on 3+ false positives; auto-raise on 3+ missed |
| **Autonomous Evolution** | New rules extracted from edge cases; cross-platform regulation sync |

### Review Dimensions Matrix

| Dimension | Basis |
|-----------|-------|
| Political Safety | Cybersecurity Law + AV Standards Art.1-10 |
| Pornography/Vulgarity | Advertising Law Art.9 + Platform guidelines |
| Violence/Terror | Platform community guidelines |
| Minor Protection | Minor Online Protection Regulations |
| Misinformation | Advertising Law Art.4, 28 |
| Infringement | Copyright Law + Personal Information Protection Law |
| Ad Compliance | Advertising Law Art.9 + Internet Ad Regulations |
| AI-Generated Content | Deep Synthesis Regulations |

### Project Structure

```
content-moderation-ecc/
├── SKILL.md                     # Core document (ECC architecture)
├── scripts/
│   └── review.py                # Review script
└── references/
    ├── platforms/               # 6 platform rules
    ├── laws/                    # 4 legal frameworks
    └── memory/                  # Memory & evolution modules
        ├── review-log-template.md
        ├── case-library.md
        ├── false-positives.md
        ├── edge-cases.md
        ├── evolution-protocol.md
        └── evolution-log.md
```
