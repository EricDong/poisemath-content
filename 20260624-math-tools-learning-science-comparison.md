---
title: 主流数学学习工具的学习科学审视
date: 2026-06-24
tags: [learning-science, edtech, math, ai-tutoring]
---

# 以学习科学审视主流数学学习工具

> [R] 研究笔记。结论标来源,区分事实与推断。核心论断尽量做了 ≥2 来源交叉验证。
> 对象:Math Academy、Khan Academy(含 Khanmigo)、IXL、Beast Academy / Art of Problem Solving(AoPS)。

## 一、先立尺子:学习科学的几条硬约束

讨论"优劣"之前需要一把统一的尺,否则只是品牌偏好之争。认知科学(cognitive science of learning)对"什么让学习真正发生"已有数十年相对稳固的实证,以下几条是评判数学工具的关键维度:

**精熟学习(mastery learning)**。Bloom 提出,只有当先决知识(prerequisites)达到精熟,才让学生进入下一层。数学是高度层级化(hierarchical)的知识体——加两位数本身就隐含练了加一位数——所以前置缺口会沿知识链向上放大。

**期望性难度(desirable difficulties,Robert Bjork)**。真正提升长期保持(long-term retention)与迁移(transfer)的策略,在练习当下都"感觉更难、更慢":间隔(spacing)、交错(interleaving)、提取练习(retrieval practice)、生成(generation)。Bjork 的核心洞见是**学习期间的表现(performance)与真实学习(learning)可以分离、甚至反向**——练得越顺手,长期记得越差。这条直接判了"刷得爽=学得好"的死刑。

**记忆双强度模型**。Bjork 夫妇区分储存强度(storage strength,知识嵌入与互联的深度)和提取强度(retrieval strength,被调用的难易)。在提取强度下降后再复习,反而最大化储存强度的增益——这是间隔重复(spaced repetition)有效的底层机制。

**生产性挣扎与概念理解(productive struggle / conceptual understanding)**。程序性流畅(procedural fluency)≠ 概念理解 ≠ 可迁移推理。只在固定题型上反复正确,会制造"虚假精熟"(false mastery)。

把这五条当坐标轴,四个工具的定位差异就清楚了:**它们其实在解不同的问题**。

## 二、四个工具逐一审视

### Math Academy:把认知科学直接写进算法

Math Academy 在学习科学维度上是这批工具里**理论自觉最强**的——它几乎是把上面那把尺子逐条工程化。官方"How Our AI Works"页面把系统拆成四块:知识图谱(knowledge graph)、学生模型(student model)、诊断算法(diagnostic algorithm)、任务选择算法(task-selection algorithm)[来源: mathacademy.com]。

知识图谱手工搭建,横跨四年级到大学,数千个主题(topic)节点,每条边是显式的先决关系。诊断算法借图谱把"评估 500–1000 个主题"压缩一个数量级:每答对一题就向其先决主题与相关主题传递正证据,答错则向其"后继主题"传负证据,从而快速定位"知识前沿"(knowledge frontier)——学生恰好准备好学的边界[来源: mathacademy.com;justinmath.com]。

最具原创性的是它的间隔重复理论——**分数式隐式重复(Fractional Implicit Repetition, FIRe)**。传统间隔重复(如 Anki)假设卡片彼此独立,但数学不是:练"两位数乘法"会隐式练到"一位数乘法",重复应当沿知识图谱"向下滴流"(trickle down)到被涵盖(encompassed)的子技能。系统据此做"重复压缩"(repetition compression)——用一道高阶题一次性击倒多个到期复习,甚至让新课兼做复习,从而**在不拖慢学新内容的前提下完成必要复习**[来源: mathacademy.com;justinmath.com]。它还显式利用交错复习、最小化联想干扰(associative interference,把易混的相邻知识在时间上拉开),并按每个"学生-主题学习速度"个性化间隔节奏。

判断:Math Academy 是把 mastery learning + 期望性难度 + 间隔重复**端到端兑现得最彻底**的一个。代价是它本质上是高强度、文本驱动的"做题—讲解—复习"系统,缺乏游戏化包装,需要学习者有较强动机;偏中学到大学(代数及以上),不覆盖低龄启蒙,对概念的"探索式发现"也不是它的重点——它追求的是高效掌握既定课程体系。

### Khan Academy:精熟模型 + 把 LLM 当苏格拉底式导师

Khan Academy 的传统内核是"视频讲解 + 精熟练习(mastery system)":通过练习/测验逐级解锁,知识地图可视化。它的覆盖最广(K–大学预科 + 多学科)、完全免费,定位是**普惠的自学骨架**。

AI 整合体现在 **Khanmigo**——基于大语言模型(LLM,GPT 系列)的对话式导师。其设计原则在学习科学上是站得住的:**不直接给答案,而是用提问引导学生自己想**("doesn't give answers; it helps kids think through problems"),刻意保留生产性挣扎,这正是为了避免 LLM 把"认知卸载"(cognitive offloading)变成代替思考[来源: khanmigo.ai;Khan Academy Blog]。

证据需要谨慎读。Khan Academy 自报:六个月约 20 项产品测试、1500 万+对话线程中,"下一题正确率"提升约 6.1%[来源: Khan Academy Blog]——这是平台内的过程性指标,不是独立的学习成效。学术上更值得重视的是一项本科物理的混合方法研究:Khanmigo 组与"用 Google 搜索"组都有显著学习增益,但**两组之间无统计显著差异**;学生主观上更偏好 Khanmigo 的分步引导[来源: jtl.uwindsor.ca]。换言之,正面叙事多来自厂商与体验评测,严格对照实验里"AI 导师优于现有替代物"尚未被有力证实——这是**事实与推断要分清**的地方。

判断:Khan Academy 的精熟框架稳健、覆盖广、免费,Khanmigo 的"引导而非代答"方向正确;但它的练习偏程序性,AI 的增量效果目前证据偏弱、且数学之外的学科明显更生(科学/人文支持不及数学打磨得好)[来源: kidsaitools.com]。

### IXL:强大的练习引擎,但不是教学系统

IXL 的核心是 **SmartScore** 驱动的自适应练习:海量细分技能,答对则题目变难、分数上升。它的自适应**只对表现(准确率、速度、难度)自适应**,不涉及"教"[来源: thelearningstandard.org]。

从学习科学看,IXL 的优点和短板都很鲜明。优点:大量提取练习、即时反馈、海量题量,作为"巩固已学技能"的引擎很强。短板被多方评测反复指出:(1) **缺乏前置的显式教学/讲解**——它假设学生已在别处学过概念,不负责从零教新知;(2) 题型以选择/短答为主,**难以培养深层概念理解**;(3) SmartScore 在接近精熟阈值处对错误惩罚过重——95 分答错一题可能掉回 80 分区,易致疲劳与挫败;(4) SmartScore 95 反映的是程序性任务上的一致性,**未必等于可迁移的推理**[来源: thelearningstandard.org;opened.co]。

有意思的是 IXL 自家研究反过来论证:这种"波动式逼近精熟"比"稳步上升"对学业成长影响更强——把分数回撤当成一种被设计出来的期望性难度[来源: ixl.com 研究 PDF]。这条厂商证据方向可信但需独立验证,不宜照单全收。

判断:IXL 是**优秀的练习/巩固引擎,而非教学系统**(a superb practice engine, not a teaching system)。它最适合"课堂已教概念 + 课后大量自适应巩固"的配套场景;若指望它独立把新概念教会,会落空。它的 AI 是经典的自适应难度算法,不是生成式 LLM。

### Beast Academy / AoPS:押注生产性挣扎与概念深度

AoPS 这一脉的哲学与前三者最不同:它**不追求高效覆盖标准,而追求把数学当作思维训练**。Beast Academy(2–5 年级,漫画形式)与上层的 AoPS 课程,刻意围绕**生产性挣扎、成长型思维(growth mindset)、深度而非进度**来设计:很多题没有速解,角色们"讨论、挣扎、坚持、突破",示范犯错是过程的一部分;不同角色代表不同解题风格,传递"没有唯一正解路径"[来源: artofproblemsolving.com;beastacademy.com]。

按学习科学的尺子,这恰好对准了"概念理解 + 迁移 + 期望性难度"这几根轴,是 IXL 的镜像反面:IXL 把摩擦降到最低以求流畅,AoPS 主动制造摩擦以求深度。代价是门槛高、进度慢、对学习者(和家长)的认知负荷与挫败容忍要求高,**面向资优/高动机人群**,不是普适方案。

AI 整合上 AoPS 走的是第三条路。它的 **Alcumus** 是早于 LLM 时代的自适应系统,按能力推送优化难度的题目;近年与 OpenAI 合作,**用 LLM 辅助评分者(grader)给学生作业写反馈、提质增效**,而非让 AI 直接面向学生当导师[来源: artofproblemsolving.com/alcumus;AoPS Blog]。这与其哲学一致:**核心思考必须由学生完成,AI 只进后台**,避免把生产性挣扎外包给模型。(注:我未找到 AoPS 关于生成式 AI 的单一权威立场声明,这一推断基于其产品形态与一贯理念,置信中等。)

## 三、AI 整合数学学习的三种范式

把四者放在一起,会看到三条清晰不同的 AI 路线,且**用的根本不是同一种"AI"**:

第一种是**算法即导师(algorithmic tutor)**——Math Academy 与 IXL/Alcumus。这里的"AI"是专家系统 + 自适应算法 + 知识追踪(Bayesian Knowledge Tracing 是 Math Academy 的初始心智模型),决定"下一步学/复习什么"。它确定、可解释、与学习科学直接对齐,但不会自然语言对话。Math Academy 是这条路的天花板。

第二种是**生成式对话导师(generative conversational tutor)**——Khanmigo。LLM 提供 24/7 的自然语言答疑与苏格拉底式引导。优点是交互自然、能应对开放问题;风险是事实可靠性(LLM 在初等运算上仍会错)、以及认知卸载——若学生用它要答案,等于绕过了学习本身。Khan 用"不直接给答案"的产品约束来对冲这一风险。

第三种是**AI 退居后台(AI behind the scenes)**——AoPS。把 LLM 用于辅助人类评分与反馈生产,学生端体验仍以人类设计的难题和(必要时)真人教师为主,刻意不让 AI 介入学生的思考过程。

值得注意的张力:**生成式 AI 越强,越考验产品如何防止它伤害学习**。竞赛数学上 Grok-4 等模型已能拿到 AIME 满分级成绩[来源: x.ai;epoch.ai],但"模型会解题"与"用模型能学会解题"是两回事——后者取决于产品是否守住生产性挣扎。这也是 Math Academy/AoPS 路线相对稳健、而纯 LLM 答疑需要谨慎设计的原因。

## 四、横向对比与适用判断

| 维度 | Math Academy | Khan Academy + Khanmigo | IXL | Beast Academy / AoPS |
|---|---|---|---|---|
| 核心定位 | 高效精熟整门课程 | 普惠自学骨架 | 自适应练习/巩固 | 思维与概念深度 |
| 精熟学习 | 极强(图谱+诊断) | 强(精熟系统) | 中(只对表现自适应) | 强(深度优先) |
| 间隔/交错/提取 | 极强(FIRe 原创) | 部分 | 提取强、间隔弱 | 隐含于难题设计 |
| 概念理解/迁移 | 中偏强 | 中 | 弱(程序性为主) | 极强 |
| 显式教学 | 有 | 有(视频) | **几乎无** | 有(教材+课程) |
| AI 类型 | 自适应专家系统 | 生成式 LLM 导师 | 自适应难度算法 | 自适应+后台 LLM 评分 |
| 适用人群 | 中学—大学、高动机自学者 | K–12 普适、预算敏感 | 已学概念后的巩固 | 资优/高动机 |
| 成效证据 | 机制论证强,独立 RCT 少 | 自报指标正面,独立对照未显著 | 厂商证据正面,需独立验证 | 长期口碑强,量化证据少 |

**给学习者的实操结论。** 若目标是"系统、快速地把代数到微积分这条主干学扎实",且你是自驱型,Math Academy 在学习科学落地上最优。若要免费、广覆盖、随时有 AI 答疑的自学起点,Khan + Khanmigo 是默认选项——但把 Khanmigo 当引导者而非答案机。若孩子在学校已学概念、需要大量自适应巩固,IXL 是高效配套,但别指望它教新知。若追求数学思维、概念深度与解题品味(且能承受慢与难),Beast Academy / AoPS 无可替代。

四者并非同一赛道的竞品,而是**精熟效率(Math Academy)— 普惠覆盖(Khan)— 巩固强度(IXL)— 思维深度(AoPS)**四种价值取向。最强的方案往往是组合:用 AoPS/Beast 养概念与韧性,用 Math Academy 或 Khan 跑主干进度,用 IXL 做针对性巩固,把生成式 AI 限制在"引导而非代答"。

---

*注:多处成效数据来自厂商自报或体验评测,已在文中标注;涉及 RCT 级独立证据的论断已特别说明其局限。AoPS 的 AI 立场为基于产品形态的中等置信推断。*

## Sources

- [Math Academy — How Our AI Works](https://www.mathacademy.com/how-our-ai-works)
- [Justin Skycak — Optimized, Individualized Spaced Repetition in Hierarchical Knowledge Structures](https://www.justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/)
- [Justin Skycak — How Math Academy Creates its Knowledge Graph](https://www.justinmath.com/how-math-academy-creates-its-knowledge-graph/)
- [Khanmigo — official](https://www.khanmigo.ai/)
- [Khan Academy Blog — How Khan Academy Is Building a Better AI Tutor](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/)
- [Journal of Teaching and Learning — Leveraging "Khanmigo" Generative AI-Powered Tool for Personalized Tutoring](https://jtl.uwindsor.ca/index.php/jtl/article/view/10052)
- [The Learning Standard — IXL Review (2026)](https://thelearningstandard.org/apps/ixl)
- [IXL — How the Dynamic Nature of IXL's SmartScore Supports Student Learning (PDF)](https://www.ixl.com/materials/us/research/How_IXLs_SmartScore_Supports_Student_Learning.pdf)
- [OpenEd — We Tried IXL](https://opened.co/tools/ixl)
- [Art of Problem Solving — Beast Academy and Your Gifted Learner](https://artofproblemsolving.com/blog/articles/beast-academy-math-and-your-gifted-learner)
- [Beast Academy — official](https://beastacademy.com/)
- [AoPS — Alcumus (AI-powered adaptive practice)](https://artofproblemsolving.com/alcumus)
- [AoPS Blog — WIRED Features AoPS Partnership with OpenAI](https://artofproblemsolving.com/blog/articles/wired-magazine-features-aops-partnership-with-openai)
- [Bjork & Bjork — Creating Desirable Difficulties to Enhance Learning (PDF)](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)
- [Epoch AI — Evaluating Grok 4's math capabilities](https://epoch.ai/blog/grok-4-math)
