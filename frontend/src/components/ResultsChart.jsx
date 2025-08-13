import React, { useEffect, useState } from "react";
import axios from "axios";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";

export default function ResultsChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/results")
      .then((res) => {
        const runs = Object.entries(res.data).map(([name, metrics]) => ({
          run: name,
          accuracy: metrics.accuracy || 0,
          auc: metrics.auc || 0
        }));
        setData(runs);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="bg-white rounded-xl shadow p-4">
      <h2 className="text-xl font-bold mb-4">Model Performance</h2>
      <LineChart width={600} height={300} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="run" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="accuracy" stroke="#8884d8" />
        <Line type="monotone" dataKey="auc" stroke="#82ca9d" />
      </LineChart>
    </div>
  );
}