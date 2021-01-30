import React, { useEffect, useRef, useState } from "react";
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
import Annotation from "../LyricAnnotation/Annotation";

import "./styles/index.css"

const Song = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const lyricRef = useRef();
    const { songId } = useParams();

    // States
    const [errors, setErrors] = useState([]);
    const [loaded, setLoaded] = useState(false);
    const [showAnnotation, setShowAnnotation] = useState(false);
    const [selectedLyrics, setSelectedLyrics] = useState(""); 
    const [range, setRange] = useState();


    // Load Song
    useEffect(() => {
        dispatch(songActions.getSong(songId))
            .then(() => setLoaded(true))
            .catch(err => console.log(err))
    }, [dispatch, songId])

    if (!loaded) {
        return null;
    }

    // Get selection and open annotation box
    const addAnnotation = () => {
        const selection = document.getSelection();
        const range = selection.getRangeAt(0);
        const lyrics = selection.toString();

        if(lyrics.length > 1) {
            setRange (range);
            setSelectedLyrics(lyrics);
            setShowAnnotation(true);
        }
    }

    // Highlight annotation
    const displayAnnotation = (start, end) => {
        const lyricNode = lyricRef.current.childNodes[0];

        const range = document.createRange();
        range.setStart(lyricNode, start);
        range.setEnd(lyricNode, end);

        const highlight = document.createElement("span");
        highlight.classList.add("highlight");
        // highlight.setAttribute("id", `${currentAnnotation.id}`)

        range.surroundContents(highlight);
    }

    return (
        <div className="songpage_container">
            <SongHeader />
            <div className="songpage_main">
                <div className="songpage-main_left">
                    <SongLyrics addAnnotation={addAnnotation} lyricRef={lyricRef}/>
                    <SongComments />
                </div>
                {   showAnnotation ?  
                    <Annotation 
                        lyrics={selectedLyrics} 
                        range={range}
                        setShowAnnotation={setShowAnnotation}
                    /> :
                    <div className="songpage-main_right">
                        <SongFacts />
                        <SongBio />
                        <SongPlayer />
                        <SongVideo />
                    </div>
                }   
            </div>
        </div>
    )
}

export default Song;
