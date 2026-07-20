---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d20c59b7058d198d513775ca4f976157_da52b09b843011f192ac525400e6dd8f
    ReservedCode1: fBtaKEFy8K/5i1isQ1yAsiaMTDpnGrxNVXSLF9pcEipo14EZfKWfxXsQxf8ncW3Cxf++CAQnwRlQYbMeDQHtFI4M8P/m4ElBQOsUn49uuNWWD41xE9Zg7y9HaVFsgCZKRgRdYB0fuYnjsu3s3GNJrm2fCoyHO5V6O4CH2K9xAXmcvaH0Hu4sn0i4nnY=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d20c59b7058d198d513775ca4f976157_da52b09b843011f192ac525400e6dd8f
    ReservedCode2: fBtaKEFy8K/5i1isQ1yAsiaMTDpnGrxNVXSLF9pcEipo14EZfKWfxXsQxf8ncW3Cxf++CAQnwRlQYbMeDQHtFI4M8P/m4ElBQOsUn49uuNWWD41xE9Zg7y9HaVFsgCZKRgRdYB0fuYnjsu3s3GNJrm2fCoyHO5V6O4CH2K9xAXmcvaH0Hu4sn0i4nnY=
---

# 审查日志模板

## 模板用途

每次内容审查时使用此模板记录审查过程和结果，存入案例库用于记忆和迭代。

---

## 审查日志

```markdown
## [YYYY-MM-DD HH:mm] 审查ID: MOD-YYYYMMDD-NNN

### 基本信息
- **内容类型**: [视频/文章/直播/评论/弹幕/图片]
- **目标平台**: [抖音/快手/B站/小红书/视频号/YouTube/多平台]
- **内容来源**: [用户提交/批量审查/主动巡查]
- **内容标题**: [原始标题]
- **内容摘要**: [50字以内简要描述]

### 内容要素
- **时长/字数**: [视频时长/文章字数]
- **是否含AI生成**: [是/否/疑似]
- **是否商业内容**: [是/否/疑似]
- **是否涉及特殊行业**: [医疗/金融/教育/食品/其他]

---

### 违规检测结果

| # | 违规类别 | 具体描述 | 风险等级 | 规则依据 | 原文/画面时间戳 |
|---|----------|----------|----------|----------|------------------|
| 1 | | | CRITICAL/HIGH/MEDIUM/LOW | 广告法第X条 / 抖音公约第X类 / ... | |
| 2 | | | | | |
| 3 | | | | | |

---

### 审核结论

- [ ] 通过 - 无需修改
- [ ] 修改后发布 - 需修改 X 项
- [ ] 禁止发布 - 严重违规

**修改建议**:
1. ...
2. ...

---

### 审核备注

- 特殊情况说明:
- 需人工复核的理由:
- 类似历史案例参考:

---

### 后续跟踪

- 用户是否申诉: [是/否]
- 申诉结果: [维持/撤销/修改]
- 是否记录为边界案例: [是/否]
- 是否需要更新规则: [是/否]
```

---

## 使用说明

1. 审查完内容后，按模板填写
2. 保存至 `references/memory/case-library.md`（追加）
3. 标记为误报的案例同步追加至 `false-positives.md`
4. 边界案例同步追加至 `edge-cases.md`
5. 需要更新规则的记录同步至 `evolution-log.md`
*（内容由AI生成，仅供参考）*
