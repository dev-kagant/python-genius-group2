import React from "react";
import { useSelector } from "react-redux";
import parse from "html-react-parser";

import "./styles/SongBio.css";

const SongBio = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage-bio_container">
            <div className="songpage-bio_heading">About Song</div>
            <div className="songpage-bio_bio">{parse(currentSong.song_bio)}</div>
        </div>
    )
}

export default SongBio;
