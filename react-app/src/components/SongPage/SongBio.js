import React from "react";
import { useSelector } from "react-redux";

import "./styles/SongBio.css";

const SongBio = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage-bio_container">
            <div className="songpage-bio_heading">About Song</div>
            <div className="songpage-bio_bio"><pre>{currentSong.song_bio}</pre></div>
        </div>
    )
}

export default SongBio;