import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllSongs } from '../../store/song.js';
import './styles/home.css';

function SongTrends(){
    const songs = useSelector((state) => Object.values(state.song.byId));

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(fetchAllSongs());
    }, [dispatch]);

    return(
        <div className="main-page_container">
            <ul className="main-page_center">

                {songs && songs.map((song) =>
                <div className="song-data" key={song.title}>
                <li><img className="song-img" src={song.song_icon} alt={song.title}/></li>
                <div className="song-title"><li>{song.title}</li></div>
                <div className="song-artist"><li>{song.artist}</li></div>

                </div>
            )}
            </ul>
        </div>
    )

}

export default SongTrends;