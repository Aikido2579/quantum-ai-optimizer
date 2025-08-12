    import React from 'react'
import Plot from 'react-plotly.js'
export default function EEGChart({data=[]}){
  const traces = data.slice(0,4).map((channel,i)=>({ y: channel, type:'scatter', mode:'lines', name:'ch'+i }))
  return (<Plot data={traces} layout={{height:300, margin:{t:20}}} style={{width:'100%'}} />)
}
