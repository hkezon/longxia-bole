# longxia-bole
An emotion-isolated, autonomous trading execution agent for OKX Onchain OS.
参赛作品：Lobster Sentinel (龙虾) —— 情绪隔离型强制可信交易执行体
一句话简介：Lobster Sentinel 不是一个替用户预测方向的 AI，而是一个运行在本地隔离环境、把交易纪律写进执行链、并在极端行情下强制拦截人类非理性干预的自主交易契约代理。
项目简介：重定义 AI Agent 的执行边界
Lobster Sentinel (龙虾) 是深度耦合 OKX AI Agent / Onchain OS 场景设计的底层执行基础设施。
目前市面上的 Web3 AI 陷入了一个误区：疯狂内卷“预测胜率”，却忽视了交易中最致命的一环——执行损耗。在真实的黑暗森林中，摧毁账户的往往不是糟糕的策略，而是执行阶段的犹豫、扛单、冲动以及临场修改计划。
Lobster Sentinel 的诞生，正是为了隔离这种“人为的不稳定因素”。它通过本地化的隔离环境（Docker），将 Claw 解析出的复杂交易意图转化为机器可读的硬性规则。一旦策略下发，Lobster Sentinel 就会化身为冷酷无情的“机器狱警”，主动完成从监控到执行的闭环，甚至在必要时拒绝执行持有人临时起意的违规指令。
本作品的核心价值在于完成三大升维：
从“规则自动化”跃升为“可信执行契约”：将纪律从抽象原则转化为不可轻易篡改的系统状态机。
抗 FOMO 熔断机制：不仅监控市场，更反向监控“人类情绪”，拦截非理性下单。
极简的本地安全飞地：通过容器化部署保障 API 绝对安全，以 Telegram 作为唯一风控审计日志流。
在这场交易的博弈中，Lobster Sentinel 想证明的不是“AI 比人更聪明”，而是：在极端波动下，绝对的机器纪律，是对抗人性的唯一解。
核心功能与执行逻辑流
Lobster Sentinel 的设计逻辑，是一条单向的、不可逆的风控状态机。
1. 意图解析与市场监控 (Intent Parsing & Market Monitoring)
它不再依赖传统的死板参数，而是深度利用 Onchain OS 的底座能力。将人类模糊的自然语言策略（如：“如果大饼跌破关键支撑，分批把我的山寨币清仓”）转化为标准化的执行 Policy。同时，系统持续静默读取市场波动率与流动性状态。

2. 核心护城河：抗 FOMO 熔断与指令拦截 (Anti-FOMO Interception)
这是 Lobster Sentinel 最具颠覆性的功能。当系统检测到极端瞬时波动（如价格偏离均线阈值），而交易员试图通过干预下达高风险指令（如追高）时，Agent 会在本地 API 接口层执行硬拦截 (Hard Block)。它不仅不会执行，还会将风险警告推送到日志端。它不是你的交易助手，它是你的纪律防火墙。

3. 睡眠期的防爆仓护城河 (Sleep-Mode Liquidation Guard)
针对无法 24 小时盯盘的交易者，一旦进入 Sleep-Mode，Agent 完全接管账户风控。严格按照预设的波动率阈值进行动态减仓与刚性止损，彻底杜绝尾部风险带来的灾难。
4. 过程透明与审计台账 (Transparent Audit Trail)
所有的触发条件、拦截动作、执行参数，全部作为不可修改的日志推送到用户的接收端。交易过程从“黑箱操作”变成了完全可追溯的审计台账。

Provide a caption (optional)
与 OKX Onchain OS / Claw 的深度整合 (Integration)
Lobster Sentinel 绝对不是一个简单调用 OKX API 的外部 Python 脚本，它是作为 Onchain OS 的一个原生 “Guard 执行插件” 存在的。
意图与执行的剥离：Claw 负责处理复杂的非结构化信息和市场逻辑判断（Brain），而 Lobster Sentinel 将其转化为硬性执行流（Muscle）。
工作流式代理逻辑：完全贴合 Onchain OS 强调的 Agent 任务式逻辑。不是零散的功能堆叠，而是提供了一个完整的 Condition -> Guard Check -> Execute -> Settle 工作流标准。
为什么它具有极高的可复制性？ (Reproducibility)
真正的 Web3 基础设施不应该只存在于 PPT 和云端黑盒中。Lobster Sentinel 在设计之初，就确立了“本地化极简部署” (Self-hosted Execution Enclave)的原则。
我们深知，没有人愿意把拥有真实资金权限的API Key 随便交给一个第三方云平台。因此，我们的工程交付标准如下：
容器化隔离环境：提供完整的 Dockerfile 与 Python 依赖清单（requirements.txt）。任何有基础终端能力的交易员，都能在 5 分钟内在自己的本地环境中拉起这只“龙虾”。
解耦的交互层：无需复杂的 Web 前端。系统深度集成 Telegram 机器人，将其作为最高权限的管理终端和只读审计面板，极致轻量。
风控校验代码开源：
核心风控拦截模块逻辑已完全公开，确立了“风控前置”的执行契约：

Provide a caption (optional)
结语：去中心化时代的机器契约
在 Web3 的下半场，我们最不缺的，就是那些声称能计算出底部的模型；我们最缺的，是能在黑暗森林里拿得住枪、守得住风控底线的重装执行者。
Lobster Sentinel (龙虾) 交出的答卷极度克制：我们将 OKX Onchain OS 的强大能力收敛进一个安全的本地容器；将人类脆弱的临场决策，移交给冰冷、透明的机器逻辑。
这不仅仅是一个 AI 交易工具，更是一份不可篡改的机器交易契约。把策略交给 AI，把纪律交给代码。只有在极端波动中能够硬性守住底线的系统，才配称为真正的 Agent 基础设施。
