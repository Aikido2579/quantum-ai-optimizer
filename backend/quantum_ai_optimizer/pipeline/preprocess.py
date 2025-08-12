import os, numpy as np, pandas as pd
def preprocess_run():
    os.makedirs('data/processed', exist_ok=True)
    logs_path = 'data/raw/sample_learning_logs.csv'
    if not os.path.exists(logs_path):
        pd.DataFrame({'student_id':[1,2,3],'problem_id':[101,102,103],'correct':[1,0,1],'time_on_task':[30,45,20]}).to_csv(logs_path, index=False)
    df = pd.read_csv(logs_path)
    features = df.groupby('student_id').agg({'correct':['mean','sum'],'time_on_task':'mean'})
    features.columns = ['accuracy','total_correct','avg_time']
    features.to_csv('data/processed/learning_log_features.csv')
    np.save('data/processed/eeg_features.npy', np.random.randn(20,64))
    np.save('data/processed/mri_features.npy', np.random.randn(5,10,10,10))
    print('Preprocessing done')
