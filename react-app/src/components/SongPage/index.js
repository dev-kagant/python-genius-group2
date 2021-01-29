import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";

import * as songActions from "../../store/song";

import SongHeader from "./SongHeader";
import SongLyrics from "./SongLyrics";
import SongFacts from "./SongFacts";
import SongBio from "./SongBio";
import SongVideo from "./SongVideo";
import SongComments from "./SongComments";
import SongPlayer from "./SongPlayer";
// import Annotations from '../Annotations/Annotations';

import "./styles/index.css"

const Song = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const { songId } = useParams();
    // States
    const [loaded, setLoaded] = useState(false);
    const [errors, setErrors] = useState([]);


    // Load Song
    useEffect(() => {
        dispatch(songActions.getSong(songId))
            .then(() => setLoaded(true))
            .catch(err => console.log(err))
    }, [dispatch, songId])

    if (!loaded) {
        return null;
    }

    return (
        <div className="songpage_container">
            <SongHeader />
            <div className="songpage_main">
                <div className="songpage-main_left">
                    {/* <Annotations/> */}
                    <SongLyrics />
                    <SongComments />
                </div>
                <div className="songpage-main_right">
                    <SongFacts />
                    <SongBio />
                    <SongPlayer />
                    <SongVideo />
                </div>
            </div>
        </div>
    )
}

export default Song;
