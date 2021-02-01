import React, { useEffect, useRef, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as songActions from "../../store/song";
import { getCurrentSongAnnotations, getAnnotationById, setCurrentAnnotation } from "../../store/annotation";

import SongHeader from "./SongHeader";
import SongLyrics from "./SongLyrics";
import SongFacts from "./SongFacts";
import SongBio from "./SongBio";
import SongVideo from "./SongVideo";
import SongComments from "./SongComments";
import SongPlayer from "./SongPlayer";
import Annotation from "../LyricAnnotation/Annotation";
import EditAnnotation from "../LyricAnnotation/EditAnnotation";

import "./styles/index.css"
import { remove } from "js-cookie";

const Song = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const lyricRef = useRef();
    const { songId } = useParams();

    // States
    const loggedInUser = useSelector(state => state.user.loggedInUser);
    const songAnnotations = useSelector(state => state.annotation.currentSongAnnotations.annotations);
    const currentAnnotation = useSelector(state => state.annotation.currentAnnotation);
    const currentSong = useSelector(state => state.song.currentSong);
    const [errors, setErrors] = useState([]);
    const [ref, setRef] = useState();
    const [loaded, setLoaded] = useState(false);
    const [showAnnotation, setShowAnnotation] = useState(false);
    const [showEditAnnotation, setShowEditAnnotation] = useState(false);
    const [selectedLyrics, setSelectedLyrics] = useState("");
    const [range, setRange] = useState();

    // console.log(currentSong.id)
    // console.log(songAnnotations)

    // Load Song
    useEffect(() => {
        dispatch(getCurrentSongAnnotations(songId))
        dispatch(songActions.getSong(songId))
            .then(() => setLoaded(true))
            .catch(err => console.log(err))
    }, [dispatch, songId])

    // Display Annotations
    useEffect(() => {
        if (!ref || !songAnnotations) return;
        let index = 0
        for (let i = 0; i < songAnnotations.length; i++) {
            displayAnnotation(ref, songAnnotations[i], index);
            index += 2;
        }
    }, [songAnnotations, ref])

    const displayAnnotation = (ref, annotation, index) => {
        // get text node
        const node = (ref.childNodes[index])

        // re-create selections
        const range = document.createRange();
        range.setStart(node, annotation.start);
        range.setEnd(node, annotation.end);

        // highlight selections
        const highlight = document.createElement("mark");
        highlight.classList.add("highlight");
        highlight.setAttribute("id", annotation.id)
        range.surroundContents(highlight)

        // add click event listener to selection
        highlight.addEventListener("click", async (e) => {
            e.stopPropagation();
            await dispatch(getAnnotationById(e.target.id))
            setShowEditAnnotation(true);
        })
    }



    // Get selection and open annotation box
    const addAnnotation = async () => {
        if (!loggedInUser) return;

        await dispatch(setCurrentAnnotation(null))

        const selection = document.getSelection();
        const range = selection.getRangeAt(0);
        const lyrics = selection.toString();

        if (lyrics.length == 0) {
            setShowAnnotation(false);
            setShowEditAnnotation(false);
        }

        if (lyrics.length > 1) {
            setRange(range);
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
                {
                    showEditAnnotation &&
                    <EditAnnotation
                        setShowEditAnnotation={setShowEditAnnotation}
                    />
                }
                {
                    showAnnotation &&
                    <Annotation
                        selectedlyrics={selectedLyrics}
                        range={range}
                        setShowAnnotation={setShowAnnotation}
                    />}
                {
                    !showAnnotation &&
                    !showEditAnnotation &&
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
