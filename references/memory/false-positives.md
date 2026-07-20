---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d20c59b7058d198d513775ca4f976157_dbb67b10843011f18a64525400826444
    ReservedCode1: lBy2WfPkFe13YWzpXwwgDbSSyLJfBEpl6HxxOgpIHTcLMpSkjpn4WhAUf6OR6MSrDruUF1B+ZNxZ+y+f1SFR+mt7PfQgyZhUQeqFOphXy2+mih9OMcRYQfsWShTSOe1f3XtqmJl6AYYP27iEGbAfwM9tFUnym3SJCNNxcm5ob3ovBg1g9noeT++0tvo=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d20c59b7058d198d513775ca4f976157_dbb67b10843011f18a64525400826444
    ReservedCode2: lBy2WfPkFe13YWzpXwwgDbSSyLJfBEpl6HxxOgpIHTcLMpSkjpn4WhAUf6OR6MSrDruUF1B+ZNxZ+y+f1SFR+mt7PfQgyZhUQeqFOphXy2+mih9OMcRYQfsWShTSOe1f3XtqmJl6AYYP27iEGbAfwM9tFUnym3SJCNNxcm5ob3ovBg1g9noeT++0tvo=
---

# 误报案例记录

> 本文档记录用户反馈的误报案例，用于迭代优化审查规则权重。
> 同一类型误报累计 ≥ 3次 → 触发规则自进化（Layer 5）

---

## 误报统计

| 规则/检测项 | 误报次数 | 最近误报时间 | 权重调整 |
|-------------|----------|-------------|----------|
| （初始为空） | - | - | - |

---

## 误报记录格式

```markdown
### [FP-YYYYMMDD-NNN] 误报标题

- **原始审查ID**: MOD-YYYYMMDD-NNN
- **误报时间**: YYYY-MM-DD
- **平台**: 
- **违规判定**: [原判定的违规项和等级]
- **用户反馈**: [用户的具体意见]
- **误报原因分析**: 
  - 直接原因: 
  - 根因: 
- **修正措施**:
  - 规则调整: [提高阈值/添加例外/完全移除]
  - 权重变化: [降低/显著降低]
- **状态**: [已修正/待验证]
```

---

## 常见误报模式

> 以下为已知的容易产生误报的场景，审查时应特别注意：

1. **极限词语境豁免**: 如"我们尽力提供最好的服务"属于普通描述，非广告法禁止的绝对化用语
2. **科普/教育内容中的医学表述**: 医生讲解疾病时使用专业术语不违规
3. **影视剧剪辑中的暴力画面**: 需结合上下文判断是否为宣传教育目的
4. **历史资料中的敏感内容**: 历史纪录片、新闻资料中的历史画面需特殊对待
5. **艺术创作中的裸露**: 经典艺术作品（雕塑、绘画）不视为色情内容
*（内容由AI生成，仅供参考）*
