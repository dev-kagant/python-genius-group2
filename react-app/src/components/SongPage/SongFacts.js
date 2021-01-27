import React from "react";
import { useSelector } from "react-redux";

import "./styles/SongFacts.css"

const SongFacts = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage-songfacts_container">
            <div className="songpage-songfacts_heading">Track Info</div>
            <div className="songpage-songfacts_items">
                <div className="songfacts-item_label">Written By</div>
                <div className="songfacts-item_content">{currentSong.written_by}</div>
            </div>
            <div className="songpage-songfacts_items">
                <div className="songfacts-item_label">Label</div>
                <div className="songfacts-item_content">{currentSong.label}</div>
            </div>
            <div className="songpage-songfacts_items">
                <div className="songfacts-item_label">Released Date</div>
                <div className="songfacts-item_content">{currentSong.release_date}</div>
            </div>
        </div>
    )
}

export default SongFacts;