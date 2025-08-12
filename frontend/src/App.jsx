    import React, {useState, useRef} from 'react'
import EEGChart from './components/EEGChart'
export default function App(){
  const [msgs, setMsgs] = useState([])
  const wsRef = useRef(null)
  const start = ()=>{
    const ws = new WebSocket((location.protocol==='https:'?'wss':'ws') + '://' + location.host + '/ws/stream')
    ws.onmessage = (ev)=>{ const d = JSON.parse(ev.data); setMsgs(m=>[d].concat(m).slice(0,100)); }
    wsRef.current = ws
  }
  const runPipeline = async ()=>{ await fetch('/run/pipeline',{method:'POST'}); alert('Pipeline started') }
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Quantum-AI Dashboard</h1>
      <div className="mt-4 flex gap-2">
        <button onClick={start} className="px-4 py-2 bg-blue-600 text-white rounded">Start Stream</button>
        <button onClick={runPipeline} className="px-4 py-2 bg-green-600 text-white rounded">Run Pipeline</button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
        <div className="p-4 border rounded">
          <h2>EEG (last message)</h2>
          <EEGChart data={msgs.length?msgs[0].eeg[0]:[]} />
        </div>
        <div className="p-4 border rounded">
          <h2>Messages</h2>
          <div style={{maxHeight:300, overflow:'auto'}}>
            {msgs.map((m,i)=>(<pre key={i} className="text-xs">{JSON.stringify(m)}</pre>))}
          </div>
        </div>
      </div>
    </div>
  )
}
