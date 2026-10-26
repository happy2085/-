#!/usr/bin/env python3
# 扫描本机 ~/.workbuddy/skills，生成技能库清单 markdown（供 GitHub 档案仓库使用）
import os, re, datetime, collections

SKILLS_DIR = os.path.expanduser("~/.workbuddy/skills")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills-inventory.md")

IP_RE = re.compile(
    r"patent|^ip[-_]|[-_]ip[-_]|[-_]ip$|trademark|copyright|claim|invalidation|reexam|"
    r"软著|专利|商标|著作|无效|复审|高企|brand", re.I)

def bucket(name):
    n = name.lower()
    if re.search(r"trademark|copyright|软著|software-copyright|brand", n): return "商标 · 著作权 · 软著"
    if re.search(r"oa[-_]|office-action|response", n): return "OA 答复 · 审查意见"
    if re.search(r"reexam|invalid|infringement|litigation|law|legal", n): return "复审 · 无效 · 侵权与诉讼"
    if re.search(r"search|novelty|fto|prior-art|patentmax|patseek|patsnap|proboost|linkfox|google-patents|chukonu|query", n): return "检索 · 查新 · FTO"
    if re.search(r"draft|writer|writing|disclosure|drawing|filing|efiling|proposal", n): return "撰写 · 交底书 · 申请提交"
    if re.search(r"precheck|check|quality|validator|logic|preliminary-examination|review", n): return "质检 · 形式审查 · 复核"
    if re.search(r"landscape|portfolio|analysis|mining|panorama|insight|intel|family|citation|research|expert|assistant|kit|scanner|report", n): return "分析 · 情报 · 布局"
    return "其他知识产权工具"

names = sorted(d for d in os.listdir(SKILLS_DIR)
               if os.path.isdir(os.path.join(SKILLS_DIR, d)))
ip = [n for n in names if IP_RE.search(n)]
others = [n for n in names if not IP_RE.search(n)]

groups = collections.defaultdict(list)
for n in ip:
    groups[bucket(n)].append(n)

order = ["检索 · 查新 · FTO", "撰写 · 交底书 · 申请提交", "OA 答复 · 审查意见",
         "复审 · 无效 · 侵权与诉讼", "质检 · 形式审查 · 复核",
         "分析 · 情报 · 布局", "商标 · 著作权 · 软著", "其他知识产权工具"]

today = datetime.date.today().isoformat()
L = []
L.append("# AI 技能库清单\n")
L.append(f"> 统计口径：本机 `~/.workbuddy/skills` 顶层安装单元，统计日期 **{today}**。\n")
L.append(f"> 合计 **{len(names)}** 个技能包，其中知识产权方向 **{len(ip)}** 个，通用能力 **{len(others)}** 个。\n")
L.append("\n清单由脚本自动扫描生成，只列名称，不做能力描述。\n")

for g in order:
    items = sorted(groups.get(g, []))
    if not items:
        continue
    L.append(f"\n## {g} · {len(items)} 项\n")
    L.append("| # | 技能包 | # | 技能包 |")
    L.append("|---|---|---|---|")
    for i in range(0, len(items), 2):
        a = f"`{items[i]}`"
        b = f"`{items[i+1]}`" if i + 1 < len(items) else ""
        L.append(f"| {i+1} | {a} | {i+2 if b else ''} | {b} |")

L.append(f"\n## 通用能力（非知识产权） · {len(others)} 项\n")
L.append("<details>\n<summary>展开完整列表</summary>\n")
for i in range(0, len(others), 4):
    L.append(" · ".join(f"`{x}`" for x in others[i:i+4]) + "  ")
L.append("\n</details>\n")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(L))

print(f"total={len(names)} ip={len(ip)} others={len(others)}")
for g in order:
    print(f"  {g}: {len(groups.get(g, []))}")
print("written:", OUT)
