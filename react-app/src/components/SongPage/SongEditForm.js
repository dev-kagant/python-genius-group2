import React, { useState } from "react";
import { format } from "date-fns";
import { useSelector, useDispatch } from "react-redux";
import { useParams, useHistory } from "react-router-dom"
import { deleteSong, editSong } from "../../store/song";

import "./styles/SongEditForm.css";


const SongEditForm = ({ setShowModal }) => {
  const dispatch = useDispatch();
  const history = useHistory();

  const [errors, setErrors] = useState([]);

  const currentSong = useSelector(state => state.song.currentSong);

  const { songId } = useParams();
  const [artist, setArtist] = useState(currentSong.artist);
  const [title, setTitle] = useState(currentSong.title);
  const [album, setAlbum] = useState(currentSong.album);
  const [song_url, setSong_url] = useState(currentSong.song_url);
  const [written_by, setWritten_by] = useState(currentSong.written_by);
  const [label, setLabel] = useState(currentSong.label);
  const [release_date, setRelease_date] = useState(currentSong.release_date);
  const [media_url, setMedia_url] = useState(currentSong.media_url);
  const [song_icon, setSong_icon] = useState(currentSong.song_icon);
  const [song_background_image, setSong_background_image] = useState(currentSong.song_background_image);


  const editThisSong = (e) => {
    e.preventDefault();
    setErrors([]);
    return dispatch(editSong({
      id: songId,
      artist,
      title,
      album,
      song_url,
      written_by,
      label,
      release_date,
      media_url,
      song_icon,
      song_background_image
    }))
      .then(() => { setShowModal(false) })
      .then(() => { history(`/songs/${songId}`) })
      .catch((res) => {
        if (res.data && res.data.errors) setErrors(res.data.errors);
      })
  }

  const deleteThisSong = () => {
    setErrors([]);
    return dispatch(deleteSong(songId))
      .then(() => { history.push(`/`) })
      .catch((res) => {
        if (res.data && res.data.errors) setErrors(res.data.errors);
      })
  }

  return (
    <form className="song-edit_form">
      <div className="song-edit_row">
        <div className="song-edit_input-container">
          <label className="song-edit_label">TITLE</label>
          <input
            className="song-edit_input-box"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div className="song-edit_input-container">
          <label className="song-edit_label">ARTIST</label>
          <input
            className="song-edit_input-box"
            type="text"
            value={artist}
            onChange={(e) => setArtist(e.target.value)}
            required
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container">
          <label className="song-edit_label">ALBUM</label>
          <input
            className="song-edit_input-box"
            type="text"
            value={album}
            onChange={(e) => setAlbum(e.target.value)}
            required
          />
        </div>
        <div className="song-edit_input-container">
          <label className="song-edit_label">LABEL</label>
          <input
            className="song-edit_input-box"
            value={label}
            onChange={(e) => setLabel(e.target.value)}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container">
          <label className="song-edit_label">WRITTEN BY</label>
          <input
            className="song-edit_input-box"
            value={written_by}
            onChange={(e) => setWritten_by(e.target.value)}
            type="text"
          />
        </div>
        <div className="song-edit_input-container">
          <label className="song-edit_label">RELEASE DATE</label>
          <input
            className="song-edit_input-box"
            value={format(new Date(release_date), "yyyy-MM-dd")}
            onChange={(e) => setRelease_date(e.target.value)}
            type="date"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">SONG ART URL</label>
          <input
            className="song-edit_input-box"
            value={song_icon}
            onChange={(e) => setSong_icon(e.target.value)}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">BANNER IMAGE URL</label>
          <input
            className="song-edit_input-box"
            value={song_background_image}
            onChange={(e) => setSong_background_image(e.target.value)}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">AUDIO URL</label>
          <input
            className="song-edit_input-box"
            value={song_url}
            onChange={(e) => setSong_url(e.target.value)}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">VIDEO URL</label>
          <input
            className="song-edit_input-box"
            value={media_url}
            onChange={(e) => setMedia_url(e.target.value)}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_buttons">
        <div className="song-edit_buttons-left">
          <button type="submit" className="song-edit_save" onClick={editThisSong}>Save</button>
          <button
            type="button"
            className="song-edit_cancel"
            onClick={() => setShowModal(false)}
          >Cancel</button>
        </div>
        <button type="button" className="song-edit_delete" onClick={deleteThisSong} >Delete</button>
      </div>

      {/* <ul>
        {errors.map((error, idx) => (
          <li key={idx} className="auth__error">
            <i className="fas fa-exclamation-circle"></i>
            {error}
          </li>))}
      </ul> */}
    </form>
  )
}

export default SongEditForm;
