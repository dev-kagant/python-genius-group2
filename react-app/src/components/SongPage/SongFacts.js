import React from "react";

import "./styles/SongFacts.css"

const SongFacts = () => {
    return (
        <div className="songpage-songfacts_container">
            <div className="songpage-songfacts_heading">Track Info</div>
            <div className="songpage-songfacts_items">
                <div className="songfacts-item_label">Written By</div>
                <div className="songfacts-item_content">Composer</div>
            </div>
            <div className="songpage-songfacts_items">
                <div className="songfacts-item_label">Label</div>
                <div className="songfacts-item_content">Label Name</div>
            </div>
            <div className="songpage-songfacts_items">
                <div className="songfacts-item_label">Released Date</div>
                <div className="songfacts-item_content">Date</div>
            </div>
        </div>
    )
}

export default SongFacts;