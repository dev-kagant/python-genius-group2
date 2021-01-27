import React from "react";
import { format } from "date-fns";
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
                <div className="songfacts-item_content">{format(new Date(currentSong.release_date), "yyyy-MM-dd")}</div> 
            </div>
        </div>
    )
}

export default SongFacts;