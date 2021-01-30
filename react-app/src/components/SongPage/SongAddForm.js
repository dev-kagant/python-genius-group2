import React, { useState } from "react";
import { useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom";

import { postSong } from "../../store/song";
import "./styles/SongAddForm.css";

const SongAddForm = () => {
    const dispatch = useDispatch();
    const history = useHistory();

    const [artist, setArtist] = useState("");
    const [title, setTitle] = useState("");
    const [album, setAlbum] = useState("");
    const [song_url, setSong_url] = useState("");
    const [lyrics, setLyrics] = useState("");
    const [written_by, setWritten_by] = useState("");
    const [label, setLabel] = useState("");
    const [release_date, setRelease_date] = useState(null);
    const [media_url, setMedia_url] = useState("");
    const [song_icon, setSong_icon] = useState("");
    const [song_background_image, setSong_background_image] = useState("");
    const [song_bio, setSong_bio] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(postSong({
            artist,
            title,
            album,
            song_url,
            lyrics,
            written_by,
            label,
            release_date,
            media_url,
            song_icon,
            song_background_image,
            song_bio
        })).then((res) => { history.push(`/songs/${res}`) })
            .catch((res) => {
                if (res.data && res.data.errors) setErrors(res.data.errors);
            })
    }

    const stopAddingSong = () => {
        history.push("/")
    }

    return (
        <div className="song-add_container">
            <div className="song-add_heading">Add Song</div>
            <form className="song-add_main" onSubmit={handleSubmit}>
                <div className="song-add_left">
                    <div className="song-add_primary-heading-container">
                        <div className="song-add_primary">Primary info</div>
                        <div className="song-add_required">* required</div>
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">ARTIST *</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={artist}
                            onChange={(e) => setArtist(e.target.value)}
                            required
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">TITLE *</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            required
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">ALBUM *</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={album}
                            onChange={(e) => setAlbum(e.target.value)}
                            required
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">AUDIO URL *</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={song_url}
                            onChange={(e) => setSong_url(e.target.value)}
                            required
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">LYRICS *</label>
                        <textarea
                            className="song-add_textarea-lyrics"
                            value={lyrics}
                            onChange={(e) => setLyrics(e.target.value)}
                            required
                        />
                    </div>
                </div>
                <div className="song-add_right">
                    <div className="song-add_additional-heading-container">
                        <div className="song-add_additional">Additional info</div>
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">WRITTEN BY</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={written_by}
                            onChange={(e) => setWritten_by(e.target.value)}
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">LABEL</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={label}
                            onChange={(e) => setLabel(e.target.value)}
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">RELEASE DATE</label>
                        <input
                            className="song-add_input-box"
                            type="date"
                            value={release_date}
                            onChange={(e) => setRelease_date(e.target.value)}
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">VIDEO URL</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={media_url}
                            onChange={(e) => setMedia_url(e.target.value)}
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">SONG IMAGE URL</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={song_icon}
                            onChange={(e) => setSong_icon(e.target.value)}
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">SONG BACKGROUND IMAGE URL</label>
                        <input
                            className="song-add_input-box"
                            type="text"
                            value={song_background_image}
                            onChange={(e) => setSong_background_image(e.target.value)}
                        />
                    </div>
                    <div className="song-add_input-container">
                        <label className="song-add_label">BIO</label>
                        <textarea
                            className="song-add_textarea-bio"
                            type="text"
                            value={song_bio}
                            onChange={(e) => setSong_bio(e.target.value)}
                        />
                    </div>
                    <div className="song-add_buttons">
                        <button
                            type="submit"
                            className="song-add_save"
                        >Save</button>
                        <button
                            type="button"
                            className="song-add_cancel"
                            onClick={stopAddingSong}
                        >Cancel</button>
                    </div>
                </div>
            </form>
        </div>
    )
}

export default SongAddForm;
