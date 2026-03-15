# guard_core.py
import logging

def execute_trade(intent_signal, market_context, user_status):
    """
    核心风控校验层 (Risk Enforcement Layer)
    拦截一切违背策略纪律的人为主观干预
    """
    action = parse_claw_intent(intent_signal)
    
    # 核心护城河：情绪熔断与追高拦截
    if user_status.fomo_index > THRESHOLD or market_context.volatility == "EXTREME":
        if action.type == "BUY_LONG" and not action.is_pre_planned:
            send_telegram_alert("🚫 [Lobster Sentinel] 拦截警报：检测到非计划内 FOMO 追高动作，接口已暂时锁定。拒绝执行。")
            return "BLOCKED_BY_GUARD"
            
    # 刚性回撤校验
    if calculate_drawdown(action) > MAX_ALLOWED_DRAWDOWN:
        send_telegram_alert("🚫 [Lobster Sentinel] 拦截警报：该动作将突破预设最大回撤边界。拒绝执行。")
        return "RISK_LIMIT_EXCEEDED"
        
    # 验证通过，广播至 OKX Onchain OS
    return broadcast_to_okx_onchain(action)
