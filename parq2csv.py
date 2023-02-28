#
# author: carlosadean
# date: 2023-02-28
# requirements: 
#   - miniconda
#   - pandas 
#   - pyarrow
#
import pandas as pd
from datetime import datetime

# 4.2GB the smaller file
#parquet_file='/lustre/t1/cl/lsst/dp0.2/objectTable_tract_3454_DC2_2_2i_runs_DP0_2_v23_0_1_PREOPS-905_step3_11_20220220T032646Z.parq'
#parquet_file='/lustre/t1/cl/lsst/dp0.2/objectTable_tract_3635_DC2_2_2i_runs_DP0_2_v23_0_1_PREOPS-905_step3_12_20220218T172932Z.parq'
parquet_file='./objectTable_tract_3635_DC2_2_2i_runs_DP0_2_v23_0_1_PREOPS-905_step3_12_20220218T172932Z.parq'
csv_file='/lustre/t0/tmp/DP0_2_20220218T172932Z.csv'

df = pd.read_parquet(parquet_file)

print(datetime.now())
print('converting .parquet to .csv file...')
df.to_csv(csv_file)
print('')
print('conversion done')
print(datetime.now())
