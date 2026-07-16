# style-lab — poisemath 风格实验室

目的,通过「AI 初稿 → Eric 二改 → diff 分析」的循环,把 khazix-writer 逐步改造成 Eric 自己的 poisemath-writer。

## 目录结构

```
style-lab/
├── README.md        本文件,工作流说明
├── originals/       AI 初稿快照(二改前的原始版本,永不修改)
└── style-log.md     风格差异台账(证据库,poisemath-writer 增量规则的唯一来源)
```

## 工作流(一轮循环)

1. **出稿**,用 poisemath-writer(或 khazix-writer)产出初稿到 `draft/`,**同时立刻复制一份到 `style-lab/originals/` 同名文件**。这一步是整个闭环的前提,忘了快照这轮就废了。
2. **二改**,Eric 直接在 `draft/` 里的文件上改,想怎么改怎么改,不用留痕迹。
3. **触发分析**,Eric 说一声「改完了,分析一下」(或类似表达),Claude 执行下面的对比分析协议。
4. **沉淀**,分析结果记入 `style-log.md`,达到晋升门槛的规则提案后写进 poisemath-writer SKILL.md 的「Eric 风格增量层」。

## 对比分析协议(Claude 执行)

1. 用 word-level diff 对比 `originals/<文件>` 与 `draft/<文件>`,例如
   `git diff --no-index --word-diff=plain "style-lab/originals/X.md" "draft/X.md"`
2. **先过滤内容性修改**,事实订正、补充真实细节(如替换【真实细节】占位)、增删素材,这些不是风格信号,单独记一行即可。
3. 对剩下的**风格性修改**逐条归类,维度包括,词汇替换 / 句式改写 / 节奏调整(拆并段、长短句) / 结构挪动 / 标点习惯 / 称呼与人称 / 语气立场(更收敛还是更放开) / 删除(AI 写了但 Eric 不要的类型)。
4. **同样重要,记录 Eric 原样保留的部分**,尤其是 khazix 风格里被验证有效的手法,这决定增量层「不改什么」。
5. 每条观察写入 `style-log.md`,附 AI 原文→Eric 改后 的原文引用,并核对既有条目,同类模式出现则计数 +1。
6. 向 Eric 汇报本轮学到了什么,并列出达到晋升门槛的规则提案,Eric 拍板后写进 SKILL.md。

## 规则晋升门槛

- 同一模式在 **≥2 篇不同文章** 中出现 → 提案晋升为 poisemath-writer 正式规则
- 只出现 1 次 → 留在台账里继续观察
- 与 khazix 基座规则直接冲突的 Eric 习惯 → 即使只出现 1 次也优先提案(基座覆盖比新增规则更关键)
- 规则写进 SKILL.md 时,在台账条目上标记「已晋升 YYYY-MM-DD」,避免重复提案
