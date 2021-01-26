import React from "react";

import "./styles/SongLyrics.css";

const SongLyrics = () => {
    return (
        <div className="songpage-lyrics_container">
            <div className="songpage-lyrics_buttons-container">
                <button className="songpage-lyrics_buttons">Edit Lyrics</button>
                <button className="songpage-lyrics_buttons">Edit Song Facts</button>
            </div>
            <div className="songpage-lyrics_lyrics">Lyrics</div>
        </div>
    )
}

export default SongLyrics;
