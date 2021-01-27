import React, { useState } from 'react';
import { useSelector } from "react-redux";
import parse from "html-react-parser";

import SongEditForm from "./SongEditForm";
import { Modal } from "../Modal/Modal";
import "./styles/SongLyrics.css";

const SongLyrics = () => {
    const currentSong = useSelector(state => state.song.currentSong);
    const [showModal, setShowModal] = useState(false);

    return (
        <div className="songpage-lyrics_container">
            <div className="songpage-lyrics_buttons-container">
                <button className="songpage-lyrics_buttons">Edit Lyrics</button>
                <button 
                    className="songpage-lyrics_buttons"
                    onClick={() => {setShowModal(true)}}
                >Edit Song Facts</button>
                {showModal && (
                    <Modal onClose={() => setShowModal(false)}>
                        <SongEditForm setShowModal={setShowModal} />
                    </Modal>
                )}
            </div>
            <div className="songpage-lyrics_lyrics">{parse(currentSong.lyrics)}</div>
        </div>
    )
}

export default SongLyrics;
