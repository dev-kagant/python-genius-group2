import React, { useContext, useState } from 'react';
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom"
import parse from "html-react-parser";

import SongEditForm from "./SongEditForm";
import { Modal } from "../Modal/Modal";
import { editLyrics } from "../../store/song"

import "./styles/SongLyrics.css";

const SongLyrics = ({ addAnnotation, lyricRef }) => {
    const dispatch = useDispatch();
    const { songId } = useParams();

    const currentSong = useSelector(state => state.song.currentSong);
    const loggedInUser = useSelector(state => state.user.loggedInUser);

    const [errors, setErrors] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [lyrics, setLyrics] = useState(currentSong.lyrics);
    const [hideLyrics, setHideLyrics] = useState(true)


    const hidePageLyrics = () => {
        setHideLyrics(false)
    }

    const hideEditLyrics = (e) => {
        setHideLyrics(true)
    }

    const editSongLyrics = (e) => {
        e.preventDefault()
        setErrors([])
        return dispatch(editLyrics({ songId, lyrics }))
            .then(() => hideEditLyrics())
            .catch((res) => {
                if (res.data && res.data.errors) setErrors(res.data.errors);
            })
    }



    return (
        <>
            {(hideLyrics) ? 
            (
                <div className="songpage-lyrics_container">
                    <div className="songpage-lyrics_buttons-container">
                        <button className="songpage-lyrics_buttons" onClick={hidePageLyrics}>Edit Lyrics</button>
                        {   loggedInUser && currentSong.user_Id == loggedInUser.id && 
                            (<button
                            className="songpage-lyrics_buttons"
                            onClick={() => { setShowModal(true) }}
                            >Edit Song Facts</button>)
                        }
                        {showModal && (
                            <Modal onClose={() => setShowModal(false)}>
                                <SongEditForm setShowModal={setShowModal} />
                            </Modal>
                        )}
                    </div>
                    <div 
                        className="songpage-lyrics_lyrics" 
                        onMouseUp={addAnnotation}
                        ref={lyricRef}
                    >
                        {parse(currentSong.lyrics)}
                    </div>
            </div>) : (
                <div className="songpage-lyrics_container">
                    <div>
                        <button type="submit" className="songpage-lyrics_buttons" onClick={editSongLyrics}>Save Lyrics</button>
                        <button type="button" className="songpage-lyrics_buttons" onClick={hideEditLyrics}>Cancel</button>
                    </div>
                    <form>
                        <textarea
                            className="song-lyric_edit-box"
                            value={lyrics}
                            onChange={(e) => setLyrics(e.target.value)}
                            type="text"
                        />
                    </form>
                </div>
            )}    
        </>
    )
}

export default SongLyrics;
