import React, { useEffect } from "react";
import { format } from "date-fns";
import { useSelector } from "react-redux";

import "./styles/SongEditForm.css";

const SongEditForm = ({ setShowModal }) => {
  const currentSong = useSelector(state => state.song.currentSong);

  return (
    <form className="song-edit_form"> 
      <div className="song-edit_row">
        <div className="song-edit_input-container">
          <label className="song-edit_label">TITLE</label>
          <input 
            className="song-edit_input-box"
            type="text"
            value={currentSong.title}
            // onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div className="song-edit_input-container">
          <label className="song-edit_label">ARTIST</label>
          <input 
            className="song-edit_input-box"
            type="text"
            value={currentSong.artist}
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
            value={currentSong.album}
            required
          />
        </div>
        <div className="song-edit_input-container">
          <label className="song-edit_label">LABEL</label>
          <input 
            className="song-edit_input-box"
            value={currentSong.label}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container">
          <label className="song-edit_label">WRITTEN BY</label>
          <input 
            className="song-edit_input-box"
            value={currentSong.written_by}
            type="text"
          />
        </div>
        <div className="song-edit_input-container">
          <label className="song-edit_label">RELEASE DATE</label>
          <input 
            className="song-edit_input-box"
            value={format(new Date(currentSong.release_date), "yyyy-MM-dd")}
            type="date"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">SONG ART URL</label>
          <input 
            className="song-edit_input-box"
            value={currentSong.song_icon}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">BANNER IMAGE URL</label>
          <input 
            className="song-edit_input-box"
            value={currentSong.song_background_image}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">AUDIO URL</label>
          <input 
            className="song-edit_input-box"
            value={currentSong.song_url}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_row">
        <div className="song-edit_input-container--full-row">
          <label className="song-edit_label">VIDEO URL</label>
          <input 
            className="song-edit_input-box"
            value={currentSong.media_url}
            type="text"
          />
        </div>
      </div>
      <div className="song-edit_buttons">
        <div className="song-edit_buttons-left">
          <button type="submit" className="song-edit_save">Save</button>
          <button 
            type="button" 
            className="song-edit_cancel"
            onClick={() => setShowModal(false)}
          >Cancel</button>
        </div>
        <button type="button" className="song-edit_delete">Delete</button>
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