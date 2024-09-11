import React from 'react';
import './App.css';
import { Home, Navbar, Footer} from './components';
import { Route, Routes } from 'react-router-dom';


function App() {
  return <Routes>
    <Route path='/' element = {<><Navbar /><Home /><Footer /></>}></Route>
  </Routes>
}

export default App;
