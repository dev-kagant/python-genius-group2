import React from "react";
import ReactPlayer from 'react-player'
import { useSelector } from 'react-redux'

import "./styles/SongPlayer.css"

const SongPlayer = () => {
    const currentSong = useSelector(state => state.song.currentSong);

    return (
        <div className="songpage-player_container">
            <div className="songpage-player_player">
                <ReactPlayer 
                    url={currentSong.song_url}
                    width='100%'
                    height='100%' 
                />
            </div>
        </div>     
    )
}

export default SongPlayer;