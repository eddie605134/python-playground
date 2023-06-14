import langchain

sentence = "被告人李四因涉嫌於2022年5月1日在新北市打劫一名路人，並奪走其手機與錢包。經法院審理後，李四被判有罪，需服刑二年並支付賠償金五萬元。"

# 初始化 LangChain
lc = langchain.LLMChain()

# 分析判決書
result = lc.analyze(sentence)

# 列印結果
print(result)