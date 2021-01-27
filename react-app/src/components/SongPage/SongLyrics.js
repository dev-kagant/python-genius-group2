import React from "react";
import { useSelector } from "react-redux";

import "./styles/SongLyrics.css";

const SongLyrics = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage-lyrics_container">
            <div className="songpage-lyrics_buttons-container">
                <button className="songpage-lyrics_buttons">Edit Lyrics</button>
                <button className="songpage-lyrics_buttons">Edit Song Facts</button>
            </div>
            <div className="songpage-lyrics_lyrics">{currentSong.lyrics}</div>
        </div>
    )
}

export default SongLyrics;
