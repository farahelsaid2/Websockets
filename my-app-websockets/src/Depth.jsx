import { useEffect,useState } from "react";



function Depth (){
    const [depth, setDepth] = useState(null);
    const [state, setState] = useState('Connecting');

    useEffect( () => {
        const ws = new WebSocket ('ws://10.0.2.15:8765');

        ws.onopen = () => setState('Connected');
        ws.onmessage = (event) => setDepth(event.data);
        ws.onclose = () => setState('Disconnected');
        ws.onerror = () => setState('Error');
        return () => { ws.close();}
    },[]);

        const getColorClass = (reading) => {
        if (reading < 100) return 'low';
        if (reading < 250) return 'medium';
        else return 'high';
        }

    return(
        <>
        <div>
        <header className="header"> Depth reading </header>
        <p className="Info"> Status : {state} </p>
        <p className={`depth ${getColorClass(depth)}`}> Depth = {depth ? `${depth} meters` : 'No data'} </p>
        </div>
        </>
    );
}
export default Depth;