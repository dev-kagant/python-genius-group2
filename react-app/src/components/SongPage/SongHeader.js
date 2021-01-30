import React from "react";
import { useSelector } from "react-redux";

import "./styles/SongHeader.css"

const SongHeader = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage_header">
            {   currentSong.song_background_image ?
                <img
                    className="songpage-header_background"
                    src={currentSong.song_background_image}
                /> :
                <div className="songpage-header_default-background"/>
            }
            <div className="songpage-header_overlay" />
            <div className="songpage-header_details">
                {   currentSong.song_icon ?
                    <img
                        className="songpage-header_artwork"
                        src={currentSong.song_icon}
                    /> :
                    <div className="songpage-header_default-artwork" />
                }
                <div className="songpage-header_info">
                    <div className="songpage-header_title">{currentSong.title}</div>
                    <div className="songpage-header_artist">{currentSong.artist}</div>
                    <div className="songpage-header_album">{currentSong.album}</div>
                </div>
            </div>
        </div>
    )
}

export default SongHeader;
