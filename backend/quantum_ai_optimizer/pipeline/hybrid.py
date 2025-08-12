import os, json
import torch, torch.nn as nn, torch.optim as optim
def hybrid_run():
    os.makedirs('results', exist_ok=True)
    fp = 'data/processed/learning_log_features.csv'
    if not os.path.exists(fp):
        print('Run preprocess first')
        return
    import pandas as pd
    df = pd.read_csv(fp)
    X = df[['avg_time']].values if 'avg_time' in df.columns else df[['accuracy']].values
    y = (df['accuracy'] > df['accuracy'].mean()).astype(int).values
    if len(y) < 2:
        with open('results/quantum_metrics.json','w') as f:
            json.dump({'best_loss': None}, f)
        return
    class SimpleNet(nn.Module):
        def __init__(self, input_dim):
            super().__init__(); self.fc = nn.Linear(input_dim, 8); self.head = nn.Linear(8,2)
        def forward(self,x):
            x = torch.tanh(self.fc(x)); return self.head(x)
    model = SimpleNet(X.shape[1])
    opt = optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    X_t = torch.tensor(X, dtype=torch.float32)
    y_t = torch.tensor(y, dtype=torch.long)
    for epoch in range(3):
        logits = model(X_t)
        loss = loss_fn(logits, y_t)
        opt.zero_grad(); loss.backward(); opt.step()
    with open('results/quantum_metrics.json','w') as f:
        json.dump({'best_loss': float(loss.detach().cpu().numpy())}, f)
    print('Hybrid done')
