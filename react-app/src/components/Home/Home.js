import React from 'react';
import SongTrends from './SongTrends.js';
import './styles/Home.css';

const Home = () => {
  return (
    <div className='charts__container'>
      <div className='charts__heading'>
        <div className='charts__heading-filter'>
          <h1 className='charts__title'> CHARTS </h1>
          <h3 className='charts__subtitle'> TRENDING ON CHEONJAE</h3>
        </div>
      </div>
      <SongTrends />
    </div>
  );
};

export default Home;
