import React from 'react';

import angellist from './icons/angellist.png';
import linkedin from './icons/linkedin.png';

import './Footer.css';

function Footer() {
    return (
        <div className='footer-container'>
            <div className='ashley-links'>
                <a className='about-link' href='https://angel.co/u/kerri-gant' rel="noreferrer" target="_blank">
                    <img src={angellist} alt='angellist' />
                </a>
                <a className='ashley-link' href='https://github.com/dev-kagant' rel="noreferrer" target="_blank">
                    Ashley Gant
                </a>
                <a className='about-link' href='https://www.linkedin.com/in/kerrigant/' rel="noreferrer" target="_blank">
                    <img src={linkedin} alt='linkedin' />
                </a>
            </div>
            <div className='safiya-links'>
                <a className='about-link' href='' rel="noreferrer" target="_blank">
                    <img src={angellist} alt='angellist' />
                </a>
                <a className='safiya-link' href='https://github.com/Scain3' rel="noreferrer" target="_blank">
                    Safiya Cain
                </a>
                <a className='about-link' href='https://www.linkedin.com/in/safiya-cain-25327356/' rel="noreferrer" target="_blank">
                    <img src={linkedin} alt='linkedin' />
                </a>
            </div>
            <div className='kimi-links'>
                <a className='about-link' href='' rel="noreferrer" target="_blank">
                    <img src={angellist} alt='angellist' />
                </a>
                <a className='kimi-link' href='https://github.com/Kimi-Zou' rel="noreferrer" target="_blank">
                    Kimi Zou
                </a>
                <a className='about-link' href='https://www.linkedin.com/in/kimizou/' rel="noreferrer" target="_blank">
                    <img src={linkedin} alt='linkedin' />
                </a>
            </div>
            <div className='damien-links'>
                <a className='about-link' href='https://angel.co/u/damien-darko' rel="noreferrer" target="_blank">
                    <img src={angellist} alt='angellist' />
                </a>
                <a className='damien-link' href='https://github.com/djangothesolarboy' rel="noreferrer" target="_blank">
                    Damien Darko
                </a>
                <a className='about-link' href='https://www.linkedin.com/in/damien-darko/' rel="noreferrer" target="_blank">
                    <img src={linkedin} alt='linkedin' />
                </a>
            </div>
        </div>
    )
}

export default Footer;