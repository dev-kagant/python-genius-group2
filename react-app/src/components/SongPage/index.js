import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";

import * as songActions from "../../store/song";
import { deleteSong } from "../../store/song";

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

    const deleteSong = async () => {
        setErrors([]);
        await dispatch(deleteSong(songId))
        return history.push(`/songs`)
    }

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
                    <SongPlayer />
                    <SongVideo />
                    <button className="songpage-delete" onClick={deleteSong}>Delete This Song</button>
                </div>
            </div>
        </div>
    )
}

export default Song;
