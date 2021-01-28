import '../NavBar/navbar.css';
import './styles/home.css';
import React from 'react';
import SongTrends from './SongTrends.js';

const HomePage = () => {
    return(
        <div className="song-charts">
            <div className="chart-headings">
                <h1 className="charts-title"> CHARTS </h1>
                <h3 className="charts-trending"> TRENDING ON CHEONJAE</h3>
                <SongTrends />
            </div>
        </div>
    )
}

export default HomePage;
