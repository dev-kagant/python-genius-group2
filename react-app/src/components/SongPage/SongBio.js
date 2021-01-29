import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import parse from "html-react-parser";
import { editBio } from "../../store/song"
import { useParams } from "react-router-dom"

import "./styles/SongBio.css";

const SongBio = () => {
    const dispatch = useDispatch();

    const currentSong = useSelector(state => state.song.currentSong);

    const { songId } = useParams();
    const [song_bio, setSong_bio] = useState(currentSong.song_bio);
    const [hideBio, setHideBio] = useState(true)
    const [errors, setErrors] = useState([]);

    const hidePageBio = () => {
        setHideBio(false)
    }

    const hideEditBio = (e) => {
        setHideBio(true)
    }

    const editSongBio = (e) => {
        e.preventDefault()
        setErrors([])
        return dispatch(editBio({ songId, song_bio }))
            .then(() => hideEditBio())
            .catch((res) => {
                if (res.data && res.data.errors) setErrors(res.data.errors);
            })
    }

    return (
        <>
            {(hideBio) ? (<div className="songpage-bio_container">
                <div className="songpage-bio_heading">About Song</div>
                <div className="songpage-bio_bio">{parse(currentSong.song_bio)}</div>
                <button className="songpage-lyrics_buttons" onClick={hidePageBio}>Edit Song Bio</button>
            </div>) : (
                    < div >
                        <textarea
                            className="song-bio_edit-box"
                            value={song_bio}
                            onChange={(e) => setSong_bio(e.target.value)}
                            type="text"
                        />
                        <button type="submit" className="songpage-lyrics_buttons" onClick={editSongBio}>Save Bio</button>
                        <button type="button" className="songpage-lyrics_buttons" onClick={hideEditBio}>Cancel</button>
                    </div>)}
        </>
    )
}

export default SongBio;
