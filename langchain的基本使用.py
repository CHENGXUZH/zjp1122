# 1、导入langchain的model模型的一个类
from langchain_openai import ChatOpenAI

# 2、ChatOpenAI给我们提供了调用各种大模型的通用能力
llm = ChatOpenAI(
    # 1、模型的名字
    model="glm-4",
    # 2、api_key
    api_key="729e04798461fea10c44168c81ab18ed.Cnw6nhTKXh4XXmbU",
    # 3、温度创新性 0-1
    temperature=0.9,
    # 4、接口的地址
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

# 3、调用模型进行推理
result = llm.invoke("刘亦菲好不好看")
print(result.content)