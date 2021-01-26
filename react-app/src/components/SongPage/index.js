import React, { useContext } from "react";
import { useParams } from "react-router-dom";

import SongPageContext from "./context/SongPageContext";

import SongHeader from "./SongHeader";
import SongLyrics from "./SongLyrics";
import SongFacts from "./SongFacts";
import SongBio from "./SongBio";
import SongVideo from "./SongVideo";
import SongComments from "./SongComments";
import SongPlayer from "./SongPlayer";

import "./styles/index.css"

const Song = () => {

    const { songId } = useParams();
    const { currentSong, setCurrentSong } = useContext(SongPageContext);

    return (
        <div className="songpage_container">
            <SongHeader />
            <div className="songpage_main">
                <div className="songpage-main_left">
                    <SongLyrics />
                    <SongComments />
                </div>
                <div className="songpage-main_right">
                    <SongFacts />
                    <SongBio />
                    <SongVideo />
                </div>  
            </div>
            <SongPlayer />
        </div>
    )
}

export default Song;
