import React from 'react';
import './footer.css';
import FXFooter from '../../assets/FX-logo.jpg';

const footer = () => {
  return (
    <div className='footer'>
        <img className='logoFooter' src={FXFooter} alt='Factory X Logo'/>
    </div>
    
  )
}

export default footer