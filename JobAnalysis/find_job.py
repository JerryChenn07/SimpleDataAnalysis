# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

infos = pd.read_csv('./find_job.csv',
					names=["unique_id", 'position_name', 'work_year', 'salary', 'company_name', 'city', 'create_time'])

a = infos.salary.value_counts().plot.bar()
plt.show()
