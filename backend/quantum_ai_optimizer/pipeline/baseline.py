import os, json, pandas as pd
from sklearn.ensemble import RandomForestClassifier
def baseline_run():
    os.makedirs('results', exist_ok=True)
    fp = 'data/processed/learning_log_features.csv'
    if not os.path.exists(fp):
        print('Run preprocess first')
        return
    df = pd.read_csv(fp)
    if len(df) < 2:
        with open('results/classical_scores.json','w') as f:
            json.dump({'accuracy':0.5}, f)
        return
    X = df[['avg_time']].values
    y = (df['accuracy'] > df['accuracy'].mean()).astype(int).values
    clf = RandomForestClassifier(n_estimators=50)
    clf.fit(X,y)
    with open('results/classical_scores.json','w') as f:
        json.dump({'accuracy': float(clf.score(X,y))}, f)
    print('Baseline done')
