# 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

import pandas as pd

df = pd.read_excel('data/Mundo.xlsx')

from pandasai import SmartDataframe

from pandasai.llm.openai import OpenAI

llm = OpenAI(api_token='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')

pandas_ai = SmartDataframe(llm)

pandas_ai.run(df, prompt='Plote um gráfico do tipo scatter comparando as colunas X3 e X4')