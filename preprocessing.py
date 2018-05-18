## 작성자: 최재필

## STATA 전처리 후 추가 전처리.

# STATA에서 한 처리들:
# - categorical data들 숫자 mapping
# - daysBeforeSale & hoursBeforeSale 변수 추가.

# 이 파일에서 할 작업들
# - csv파일을 pandas로 import
# - date 관련 column들 datetime type으로 변경.

import pandas as pd

df = pd.read_csv('autos_stata-ed.csv', sep=',')
