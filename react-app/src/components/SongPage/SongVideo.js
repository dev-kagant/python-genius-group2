import React from "react";
import ReactPlayer from 'react-player'
import { useSelector } from 'react-redux'

import "./styles/SongVideo.css"

const SongVideo = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage-video_container">
            <div className="songpage-video_heading">Music Video</div>
            <div className="songpage-video_player-container">
                <ReactPlayer 
                    url={currentSong.media_url}
                    width='100%'
                    height='100%' 
                />
            </div>
        </div>
    )
}

export default SongVideo;