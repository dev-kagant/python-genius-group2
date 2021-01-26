import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch } from "react-redux";

import * as songActions from "../../store/song";

import SongHeader from "./SongHeader";
import SongLyrics from "./SongLyrics";
import SongFacts from "./SongFacts";
import SongBio from "./SongBio";
import SongVideo from "./SongVideo";
import SongComments from "./SongComments";
import SongPlayer from "./SongPlayer";

import "./styles/index.css"

const Song = () => {
    const dispatch = useDispatch();

    const { songId } = useParams();

    // States
    const [loaded, setLoaded] = useState(false);
  

    // Load Song
    // useEffect(() => {
    //     dispatch(songActions.getSong(songId));

    // }, [dispatch, songId])

    // if (!loaded) {
    //     return null;
    // }

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
