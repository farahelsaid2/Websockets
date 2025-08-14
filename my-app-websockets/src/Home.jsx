import { useNavigate } from 'react-router-dom';

function Home (){
  
    const navigate = useNavigate ();
    const goToDepth = () => {navigate('/depthReading')};
    return(
<>
<div>
    <header className='header'> Connect your sensor and check your readings </header>
    <hr/>
    <a href="/depthReading"><button className='inButtons'>Depth</button></a>
    </div>
</>
);

}
export default Home;