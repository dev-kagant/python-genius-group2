import React, { useEffect, useRef, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

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
import { remove } from "js-cookie";

const Song = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const lyricRef = useRef();
    const { songId } = useParams();

    // States
    const loggedInUser = useSelector(state => state.user.loggedInUser);
    const songAnnotations = useSelector(state => state.song.currentSong.annotations);
    const [errors, setErrors] = useState([]);
    const [ref, setRef] = useState();
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


    // Display Annotations
    useEffect(() => {
        if (!ref) return;
        if (!songAnnotations) return;
        // console.log(ref.childNodes[0])
        const node = (ref.childNodes[0])
        // displayAnnotation(ref, songAnnotations[3])
        // displayAnnotation(ref, songAnnotations[0])
        // songAnnotations.forEach(annotation => displayAnnotation(node, annotation));
        highLight(node)
    }, [songAnnotations, ref])


    // Remove span
    const removeSpan = (node) => {
        if (node.nodeName == "SPAN") {
            return node.firstChild
        } else {
            return node;
        }
    }

    // Highlight annotation
    const highLight = (node) => {
        const ranges = [];
        
        songAnnotations.forEach(annotation => displayAnnotation(node, annotation, ranges));
        ranges.forEach(range => {
            const highlight = document.createElement("mark");
            highlight.classList.add("highlight");
            range.surroundContents(highlight)
            console.log(range)
        }) 
        // range.surroundContents(highlight))
        console.log(ranges)
    }
    

    const displayAnnotation = (node, annotation, ranges) => {
        const range = document.createRange();
        range.setStart(node, annotation.start);
        range.setEnd(node, annotation.end);
        ranges.push(range);
    }


    // Get selection and open annotation box
    const addAnnotation = () => {
        if (!loggedInUser) return;

        const selection = document.getSelection();
        const range = selection.getRangeAt(0);
        const lyrics = selection.toString();

        console.log(selection.anchorNode);
        console.log(selection.focusNode);

        if(lyrics.length > 1) {
            setRange (range);
            setSelectedLyrics(lyrics);
            setShowAnnotation(true);
        }
    }

    

    if (!loaded) {
        return null;
    }

    return (
        <div className="songpage_container">
            <SongHeader />
            <div className="songpage_main">
                <div className="songpage-main_left">
                    <SongLyrics 
                        addAnnotation={addAnnotation} 
                        lyricRef={lyricRef}
                        setRef={setRef}
                    />
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
