import React from 'react';
import Member from './Member';
import './Footer.css';

function Footer () {
  return (
    <div className='footer-container'>
      <div className='footer__left'>
        <div className='footer__about'>
          천재 (CHEONJAE) IS A GENIUS CLONE CREATED
          FOR PASSIONATE K-POP FANS.
        </div>
        <div className='footer__copyright'>
          © 2021 CHEONJAE GENIUS
        </div>
      </div>
      <div className='footer__team'>
        <div className='footer__team-col'>
          <Member
            name='Kerri Gant'
            github='https://github.com/dev-kagant'
            linkedin='https://www.linkedin.com/in/kerrigant/'
            angellist='https://angel.co/u/kerri-gant'
          />
          <Member
            name='Safiya Cain'
            github='https://github.com/Scain3'
            linkedin='https://www.linkedin.com/in/safiya-cain-25327356/'
            angellist='https://angel.co/u/safiya-cain'
          />
        </div>
        <div className='footer__team-col'>
          <Member
            name='Kimi Zou'
            github='https://github.com/Kimi-Zou'
            linkedin='https://www.linkedin.com/in/kimizou/'
            angellist='https://angel.co/u/kimi-zou'
          />
          <Member
            name='Damien Darko'
            github='https://github.com/djangothesolarboy'
            linkedin='https://www.linkedin.com/in/damien-darko/'
            angellist='https://angel.co/u/damien-darko'
          />
        </div>
      </div>
    </div>
  );
}

export default Footer;
