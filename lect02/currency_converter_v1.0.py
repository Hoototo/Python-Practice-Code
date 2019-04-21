"""
    作者: Nick
    功能: 汇率兑换
    版本：1.0
    日期: 21/03/2019
"""
# 汇率
USD_VS_RMB = 6.77

rmb_str_value = input('请输入人民币(CNY)金额: ', )  # 提示User输入人民币金额

rmb_value = eval(rmb_str_value)

usd_value = rmb_value / USD_VS_RMB

print('美元(USD)金额是: ', usd_value)
