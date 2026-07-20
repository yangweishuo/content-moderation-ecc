#!/usr/bin/env python3
"""
内容审核基础工具脚本 (Content Moderation Review Script)

提供基础审查能力：
- 违禁词快速扫描
- 广告法极限词检测
- 敏感内容正则匹配
- 审核报告生成

用法:
    python review.py --content "要审核的文本" [--platform douyin] [--output report.md]
    python review.py --file input.txt [--platform douyin] [--output report.md]
"""

import argparse
import re
import json
from datetime import datetime
from pathlib import Path


# ============================================================
# 知识库：违禁词和检测模式
# ============================================================

# 广告法极限词（绝对化用语）
AD_ABSOLUTE_WORDS = [
    "最好", "最佳", "最棒", "最优秀", "最先进", "最时尚", "最受欢迎",
    "最低价", "最便宜", "最新", "最大", "最高级", "最低", "最高",
    "国家级", "世界级", "顶级", "极品", "第一品牌",
    "首个", "首选", "独家", "独创", "独一无二", "首发", "绝无仅有",
    "第一", "唯一", "中国第一", "销量第一", "全网第一", "一流",
    "极致", "顶尖", "终极", "万能", "至尊", "巅峰",
    "王牌", "领袖品牌", "领导品牌", "冠军",
    "100%", "百分百", "纯天然",
]

# 广告法其他禁用语
AD_FORBIDDEN_WORDS = [
    "特效", "神效", "一盒见效", "三天见效", "永不复发",
    "无效退款", "假一赔十", "包治百病",
]

# 政治敏感词（示例，实际使用时需更全面）
POLITICAL_SENSITIVE_PATTERNS = [
    r"颠覆.*政权", r"分裂.*国家", r"独立.*台湾",
    r"法轮功", r"flg", r"falun",
]

# 色情低俗模式
SEXUAL_PATTERNS = [
    r"裸[体聊照]", r"约炮", r"一夜情", r"嫖娼",
    r"性交", r"口交", r"肛交", r"做爱",
    r"成人.*电影", r"18禁", r"色情",
    r"淫[秽魔荡]", r"骚[货逼]", r"浪[叫女]",
]

# 暴力恐怖模式
VIOLENCE_PATTERNS = [
    r"杀[死人光]", r"砍[死人]", r"炸[弹死]",
    r"恐怖.*袭击", r"圣战", r"斩首",
    r"枪支.*弹药", r"制造.*炸弹",
]

# 赌博相关模式
GAMBLING_PATTERNS = [
    r"赌[博场球]", r"六合彩", r"时时彩",
    r"百家乐", r"老虎机",
]

# 欺诈相关模式
FRAUD_PATTERNS = [
    r"日赚.*元", r"月入.*万", r"躺赚",
    r"加.*微信.*领取", r"免费.*领取.*红包",
]


def scan_absolute_words(content: str) -> list[dict]:
    """扫描广告法极限词"""
    results = []
    words_found = set()
    for word in AD_ABSOLUTE_WORDS:
        for match in re.finditer(re.escape(word), content):
            if word not in words_found:
                words_found.add(word)
                # 获取上下文
                start = max(0, match.start() - 20)
                end = min(len(content), match.end() + 20)
                context = content[start:end].strip()
                results.append({
                    "type": "广告法极限词",
                    "word": word,
                    "position": match.start(),
                    "context": f"...{context}...",
                    "risk": "MEDIUM",
                    "law": "广告法第九条第三款",
                    "suggestion": f"将'{word}'改为客观描述，避免绝对化用语"
                })
    return results


def scan_forbidden_words(content: str) -> list[dict]:
    """扫描广告法其他禁用语"""
    results = []
    words_found = set()
    for word in AD_FORBIDDEN_WORDS:
        for match in re.finditer(re.escape(word), content):
            if word not in words_found:
                words_found.add(word)
                start = max(0, match.start() - 20)
                end = min(len(content), match.end() + 20)
                context = content[start:end].strip()
                results.append({
                    "type": "广告法禁用语",
                    "word": word,
                    "position": match.start(),
                    "context": f"...{context}...",
                    "risk": "HIGH",
                    "law": "广告法",
                    "suggestion": f"删除或替换'{word}'"
                })
    return results


def scan_patterns(content: str, patterns: list[str], 
                  category: str, risk: str, law: str) -> list[dict]:
    """通用正则模式扫描"""
    results = []
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            start = max(0, match.start() - 15)
            end = min(len(content), match.end() + 15)
            context = content[start:end].strip()
            results.append({
                "type": category,
                "word": match.group(),  # Use match group for pattern matches
                "position": match.start(),
                "context": f"...{context}...",
                "risk": risk,
                "law": law,
                "suggestion": f"删除或修改'{match.group()}'相关内容"
            })
    return results


def review(content: str, platform: str = None) -> dict:
    """
    执行内容审查
    
    Args:
        content: 要审核的文本内容
        platform: 目标平台（可选，暂无差异化逻辑）
    
    Returns:
        审核结果字典
    """
    all_violations = []
    
    # 1. 广告法极限词扫描
    all_violations.extend(scan_absolute_words(content))
    
    # 2. 广告法禁用语扫描
    all_violations.extend(scan_forbidden_words(content))
    
    # 3. 色情低俗扫描
    all_violations.extend(
        scan_patterns(content, SEXUAL_PATTERNS, "色情低俗", "CRITICAL", 
                      "各平台社区公约")
    )
    
    # 4. 政治敏感扫描
    all_violations.extend(
        scan_patterns(content, POLITICAL_SENSITIVE_PATTERNS, "政治敏感", 
                      "CRITICAL", "网络安全法第十二条")
    )
    
    # 5. 暴力恐怖扫描
    all_violations.extend(
        scan_patterns(content, VIOLENCE_PATTERNS, "暴力恐怖", "CRITICAL",
                      "各平台社区公约")
    )
    
    # 6. 赌博扫描
    all_violations.extend(
        scan_patterns(content, GAMBLING_PATTERNS, "赌博内容", "HIGH",
                      "各平台社区公约")
    )
    
    # 7. 欺诈扫描
    all_violations.extend(
        scan_patterns(content, FRAUD_PATTERNS, "疑似欺诈", "HIGH",
                      "各平台社区公约")
    )
    
    # 按风险等级排序
    risk_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    all_violations.sort(key=lambda x: risk_order.get(x["risk"], 99))
    
    # 统计
    critical_count = sum(1 for v in all_violations if v["risk"] == "CRITICAL")
    high_count = sum(1 for v in all_violations if v["risk"] == "HIGH")
    medium_count = sum(1 for v in all_violations if v["risk"] == "MEDIUM")
    low_count = sum(1 for v in all_violations if v["risk"] == "LOW")
    
    # 判定结论
    if critical_count > 0:
        conclusion = "禁止发布 - 存在严重违规内容"
    elif high_count > 0:
        conclusion = "禁止发布 - 存在高度违规内容，建议大幅修改"
    elif medium_count > 0:
        conclusion = "修改后发布 - 存在中度违规内容"
    elif low_count > 0:
        conclusion = "建议优化后发布 - 存在低度风险内容"
    else:
        conclusion = "通过 - 未检测到违规内容"
    
    return {
        "review_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "platform": platform or "通用",
        "content_length": len(content),
        "conclusion": conclusion,
        "violations": all_violations,
        "summary": {
            "critical": critical_count,
            "high": high_count,
            "medium": medium_count,
            "low": low_count,
            "total": len(all_violations)
        }
    }


def generate_report(result: dict, output_path: str = None) -> str:
    """生成Markdown审核报告"""
    lines = []
    lines.append("## 内容审核报告")
    lines.append("")
    lines.append(f"- **审核时间**: {result['review_time']}")
    lines.append(f"- **目标平台**: {result['platform']}")
    lines.append(f"- **内容长度**: {result['content_length']} 字符")
    lines.append(f"- **审核结论**: **{result['conclusion']}**")
    lines.append("")
    
    s = result["summary"]
    lines.append("### 违规统计")
    lines.append(f"| 等级 | 数量 |")
    lines.append(f"|------|------|")
    lines.append(f"| 🔴 严重违规 | {s['critical']} |")
    lines.append(f"| 🟠 高度违规 | {s['high']} |")
    lines.append(f"| 🟡 中度违规 | {s['medium']} |")
    lines.append(f"| 🟢 低度风险 | {s['low']} |")
    lines.append(f"| **合计** | **{s['total']}** |")
    lines.append("")
    
    if result["violations"]:
        lines.append("### 违规详情")
        lines.append("| # | 类别 | 违禁内容 | 风险等级 | 法规依据 | 上下文 | 修改建议 |")
        lines.append("|---|------|----------|----------|----------|--------|----------|")
        for i, v in enumerate(result["violations"], 1):
            word = v.get("word", "")[:30]
            suggestion = v.get("suggestion", "")[:50]
            lines.append(
                f"| {i} | {v['type']} | {word} | {v['risk']} | "
                f"{v['law']} | {v['context'][:40]} | {suggestion} |"
            )
    else:
        lines.append("✅ 未检测到违规内容。")
    
    report = "\n".join(lines)
    
    if output_path:
        Path(output_path).write_text(report, encoding="utf-8")
        print(f"报告已保存至: {output_path}")
    
    return report


def main():
    parser = argparse.ArgumentParser(description="内容审核工具")
    parser.add_argument("--content", type=str, help="要审核的文本内容")
    parser.add_argument("--file", type=str, help="从文件读取内容")
    parser.add_argument("--platform", type=str, default=None,
                        help="目标平台 (douyin/kuaishou/bilibili/xiaohongshu/wechat-video/youtube)")
    parser.add_argument("--output", type=str, default=None,
                        help="审核报告输出路径")
    parser.add_argument("--json", action="store_true",
                        help="以JSON格式输出结果")
    args = parser.parse_args()
    
    # 获取内容
    if args.content:
        content = args.content
    elif args.file:
        content = Path(args.file).read_text(encoding="utf-8")
    else:
        content = input("请输入要审核的内容（输入后按回车，Ctrl+Z+回车结束）:\n")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        if lines:
            content = content + "\n".join(lines)
    
    # 执行审查
    result = review(content, args.platform)
    
    # 输出
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        report = generate_report(result, args.output)
        print(report)


if __name__ == "__main__":
    main()
