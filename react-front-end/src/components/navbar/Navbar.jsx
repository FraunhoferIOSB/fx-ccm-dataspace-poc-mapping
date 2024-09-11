import React from 'react';
import './navbar.css';
import FX from '../../assets/FX-logo.jpg';

const Navbar = () => {
  return (
    <div className='navbar'>
        <img className='Logo' src={FX} alt='Factory X logo'/>
    </div>
  )
}

export default Navbar