import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Depth from './Depth';

function App() {
  

  return (
    <>
     <div>
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<h2><Home/></h2>}/>
        <Route path='/depthReading' element={<Depth/>}/>
      </Routes>
      </BrowserRouter>
      </div>
    </>
  )
}

export default App
