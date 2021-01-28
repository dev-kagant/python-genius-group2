import '../HomePage/styles/home.css';
import React from 'react';
import SongTrends from '../HomePage/SongTrends.js';

const Charts = () => {
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

export default Charts;
