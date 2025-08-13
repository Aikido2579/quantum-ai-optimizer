import React, { useState, useEffect } from "react";

export default function App() {
  const [msgs, setMsgs] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = (event) => {
      setMsgs((prev) => [JSON.parse(event.data), ...prev]);
    };
    return () => ws.close();
  }, []);

  const runPipeline = async () => {
    await fetch("http://localhost:8000/run/pipeline", { method: "POST" });
  };

  return (
    <div>
      <h1>Quantum-AI Dashboard</h1>
      <button onClick={runPipeline}>Run Pipeline</button>
      <div>
        {msgs.map((m, i) => (
          <div key={i}>{m.status}</div>
        ))}
      </div>
    </div>
  );
}
