<div align="center">

# 孙明科 · Intellectual Property × AI

**专利代理师 ＋ 执业律师（双证）｜把 AI 塞进知识产权的每一个环节**

![Role](https://img.shields.io/badge/Role-Patent%20Attorney%20%2B%20Lawyer-1f6f4f)
![Focus](https://img.shields.io/badge/Focus-OA%20Response%20%C2%B7%20Invalidation%20%C2%B7%20Litigation-c25b3a)
![AI](https://img.shields.io/badge/AI-Agent%20Workflow-6b4de6)
![Skills](https://img.shields.io/badge/Skills-337%20Local%20Agents-2d8a4e)
![Location](https://img.shields.io/badge/Guangzhou-China-5b6570)

*Patent attorney and practicing lawyer, building an AI-augmented IP practice.*

</div>

---

## 我是谁

| | |
|---|---|
| **姓名** | 孙明科 |
| **身份** | 专利代理师 ＋ 执业律师（双证） |
| **机构** | 广州高炬知识产权代理有限公司 |
| **城市** | 中国 · 广州 |
| **主攻** | 发明专利一通（OA）答复、专利申请撰写、复审与无效、知识产权诉讼 |

做知识产权这一行，最难的不是写，是**判**——判断这个区别特征到底有没有贡献，判断这次修改会不会超范围，判断这个案子该答还是该撤。

我的工作方法是：把「查、比、写、校」这四件耗时但可标准化的事交给 AI，把「判断」和「责任」留给自己。

---

## 专业领域

| 方向 | 具体内容 |
|---|---|
| **发明专利 OA 答复** | 审查意见解读、权利要求修改与对照表、区别技术特征归纳、创造性三步法论证、公知常识举证抗辩 |
| **专利申请撰写** | 技术交底书评估、权利要求布局、说明书支撑与附图规范、申请前可行性分析 |
| **检索与评估** | 新颖性／创造性检索报告、FTO 侵权风险检索、现有技术比对表 |
| **复审与无效** | 复审请求、无效宣告请求与答辩、证据链组织、权利要求修改策略 |
| **IP 诉讼与维权** | 侵权比对分析、电商平台取证（1688／淘宝等）、诉讼代理 |
| **商标与其他** | 商标布局与异议（含欧盟商标）、著作权登记、高新技术企业材料 |

---

## AI × IP：一条被拆开重做的工作流

传统流程里，一个案子 70% 的时间花在检索、比对、成文、校对上。我的做法是用 Agent 流水线把这部分压掉，人的精力全部投到判断上。

| 环节 | AI 承担 | 我承担 |
|---|---|---|
| **交底书评估** | 技术方案拆解、关键词与检索式生成、最接近现有技术初筛 | 可专利性判断、权利要求布局策略 |
| **检索报告** | 跨库检索、文献聚类、特征比对表初稿、著录项目整理 | 新颖性／创造性结论、风险定级 |
| **OA 答复** | 权利要求修改对照表、意见陈述书初稿、法条与判例定位 | 修改是否超范围的终审、答复策略取舍 |
| **复审／无效** | 证据链梳理、类案检索与相似度标注、文本版本比对 | 法律论证、请求口审、出庭 |
| **诉讼与维权** | 侵权特征比对表、销售证据采集与固定、时间线整理 | 诉讼方案、谈判与代理 |

---

## 工具与方法

**检索数据源**　智慧芽（PatSnap）· PatSeek · Google Patents · 得理法律数据库 · 北大法宝

**文档交付**　结论先行、表格结构化；正式报告走 DOCX 模板，技术调研走 HTML

**Agent 流水线**　本地技能库驱动的「检索 → 分析 → 成文 → 自验」自动化链路，见下方 [AI 技能库](#ai-技能库本地常驻-337-项)

**三条不妥协的规矩**

1. **不编造。** 案号、法条原文、实验数据、证件号码——查不到就留空标注，等人补。这类东西编出来的代价远大于说一句「我不知道」。
2. **交付前自验。** 代码要跑通，文档要回读，文档声称的功能代码必须真的实现。没验证过的东西不叫交付。
3. **公开内容先脱敏。** 公众号／官网／开源仓库中的案件信息，发布前一律脱敏并经本人审核。

---

## AI 技能库（本地常驻 337 项）

通用大模型不懂这行的规矩：权利要求里的附图标记必须加括号，具体实施方式里的一律不加，说明书其余部分压根不许出现附图标记；三步法评述之前，还得先判断区别特征到底有没有贡献。

这些规矩口头交代一次没有用——**得固化进技能，让每次调用都自动生效**。所以我建了一套本地常驻的 Agent 技能库：

| 类别 | 数量 | 代表性技能 |
|---|:--:|---|
| 检索 · 查新 · FTO | 30 | `patent-novelty-search` `patent-fto` `patentkit-fto-search` `patseek-patent-search` `patentmax-search-strategy` `google-patents` |
| 撰写 · 交底书 · 提交 | 22 | `claims-drafting` `patent-claim-drafter` `cn-patent-drafter` `patent-disclosure-writer` `Paper-to-patent-Skill` `zhijing-cnipa-patent-efiling` |
| OA 答复 · 审查意见 | 8 | `patent-oa-response` `patent-oa-response-first` `cn-patent-oa-response` `patent-office-action-writer` |
| 复审 · 无效 · 侵权诉讼 | 10 | `patent-invalidation` `patent-reexamination` `patentkit-invalidity-search` `patentkit-infringement-search` |
| 质检 · 形式审查 · 复核 | 16 | `patent-precheck` `patent-logic-quality-check` `zhongzhixinjian-patent-preliminary-examination-check` |
| 分析 · 情报 · 布局 | 18 | `patent-landscape` `patent-portfolio-report` `analyze-patent-family-ip` `patent-mining-agent` |
| 商标 · 著作权 · 软著 | 13 | `trademark-services` `cn-software-copyright-docx` `copyright-registration-helper__skillhub` |
| 其他知识产权工具 | 21 | `patent-fee-monitor` `ip-mgmt-examination` `translate-patents-for-foreign-filing-ip` |

合计 **337** 个技能包，其中知识产权方向 **138** 个，另含 199 项通用能力（检索、文档、数据分析、自动化等）。
完整清单见 👉 [`skills-inventory.md`](./skills-inventory.md)。

**维护方式**　每周扫一遍 GitHub、ClawHub、SkillHub、CocoLoop、SkillsMP 五个平台，按「OA 答复 / 创造性 / 新颖性 / 权利要求 / 复审 / 无效 / FTO / 商标 / 版权 / 商业秘密」的优先级评估入库。清单由脚本自动扫描生成，数字随安装情况变动。

---

## 关于 2026 年新规的一点判断

自 2026-01-01 起（国家知识产权局令第 84 号），实用新型已不再是「形式审查」——初审全面纳入明显创造性审查，授权率断崖式下滑。**继续沿用「初审制、授权概率 85%+」的旧口径，是在给客户挖坑。**

新规真正的要点是：**无贡献特征不影响创造性**，堆砌无关特征规避审查这条路被堵死；能带来预料不到技术效果的创新特征必须写进权利要求，只在说明书里记载不算；审查员认定公知常识时通常应当举证。

我的做法：三步法评述前，先加一道「区别特征是否有贡献」的前置判断。

---

## 联系

- GitHub：[@happy2085](https://github.com/happy2085)
- 邮箱：*（按需填写，不建议公开明文邮箱地址）*

---

<div align="center">

<sub>本页内容仅代表个人执业经验与方法总结，不构成法律意见。</sub>

</div>
