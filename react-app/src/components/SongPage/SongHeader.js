import React from "react";
import { useSelector } from "react-redux";

import "./styles/SongHeader.css"

const SongHeader = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage_header">
            <img 
                className="songpage-header_background" 
                src="https://cdn.shopify.com/s/files/1/0273/8923/1139/collections/blackpink-banner-ice-cream-1600x400.jpg?v=1601367701"
            />
            <div className="songpage-header_overlay" />
            <div className="songpage-header_details">
                <img 
                    className="songpage-header_artwork"
                    src="https://m.media-amazon.com/images/I/61Ewmjvup6L._AC_SL1000_.jpg"
                />
                <div className="songpage-header_info">
                    <div className="songpage-header_title">{currentSong.title}</div>
                    <div className="songpage-header_artist">Artist</div>
                    <div className="songpage-header_album">Album</div>
                </div>
            </div>
        </div>
    )
}

export default SongHeader;