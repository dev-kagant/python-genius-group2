// import { fetch } from "../services/csrf";


// State
const initialState = {
    currentSong: {}
}

// Action types
const SET_CURRENT_SONG = "song/SET_CURRENT_SONG";

// POJO Actions
const setCurrentSong = (song) => ({
    type: SET_CURRENT_SONG,
    payload: song
})

// Thunk Actions
export const getSong = (id) => async dispatch => {
    const res = await fetch(`/api/songs/${id}`);
    if (res.ok) {
        const data = await res.json();
        dispatch(setCurrentSong(data));
    }
    // return res.data;
}

export const postSong = (song) => async dispatch => {
    const { 
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
    } = song;

    const response = await fetch("/api/songs/new_song", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        }, 
        body: JSON.stringify({
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
        })
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(setCurrentSong(data))
        return data.id
    }
}


// Reducer
const songReducer = (state=initialState, action) => {
    switch (action.type) {
        case SET_CURRENT_SONG:
            return {
                ...state,
                currentSong: action.payload
            };
        default:
            return state;
    }
}

export default songReducer