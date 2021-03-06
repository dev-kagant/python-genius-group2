import { signUp } from "../services/auth";
import { csrffetch } from "../services/csrf";

// State
const initialState = {
    currentSong: {},
    byId: {}
}

// Action types
const GET_ALL_SONGS = "song/GET_ALL_SONGS";

const SET_CURRENT_SONG = "song/SET_CURRENT_SONG";

// POJO Actions
export const getAllSongs = (songs) => ({
    type: GET_ALL_SONGS,
    payload: songs
})




export const setCurrentSong = (song) => ({
    type: SET_CURRENT_SONG,
    payload: song
})

//--------------------- Thunk Actions ---------------------

// GET ALL OF THE SONGS
export const fetchAllSongs = () => async (dispatch) => {
    const res = await csrffetch("/api/songs");
    dispatch(getAllSongs(res.data.songs));
}


// GET SONG BY ID
export const getSong = (id) => async dispatch => {
    const res = await fetch(`/api/songs/${id}`);
    if (res.ok) {
        const data = await res.json();
        dispatch(setCurrentSong(data));
    }
    // return res.data;
}

// CREATE NEW SONG
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

// EDIT A SONG
export const editSong = (song) => async (dispatch) => {
    const {
        id,
        artist,
        title,
        album,
        song_url,
        written_by,
        label,
        release_date,
        media_url,
        song_icon,
        song_background_image,
    } = song;
    const response = await fetch(`/api/songs/edit`, {
        method: "PATCH",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            id,
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
        })
    })
    if (response.ok) {
        const data = await response.json()
        return dispatch(setCurrentSong(data))
    }
}

// EDIT SONG LYRICS
export const editLyrics = ({ songId, lyrics }) => async dispatch => {
    const response = await fetch(`/api/songs/edit-lyrics`, {
        method: "PATCH",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            songId,
            lyrics
        })
    })
    if (response.ok) {
        const data = await response.json()
        return dispatch(setCurrentSong(data))
    }
}

// EDIT SONG BIO
export const editBio = ({ songId, song_bio }) => async dispatch => {
    const response = await fetch(`/api/songs/edit-bio`, {
        method: "PATCH",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            songId,
            song_bio
        })
    })
    if (response.ok) {
        const data = await response.json()
        return dispatch(setCurrentSong(data))
    }
}

// DELETE A SINGLE SONG
export const deleteSong = (song) => async (dispatch) => {
    const response = await fetch("/api/songs/delete", {
        method: "DELETE",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            song
        })
    });
    if (response.ok) {
        return dispatch(setCurrentSong({}))
    }
}

// --------------------- Reducer ---------------------
const songReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_SONGS:
            const newSongs = {};
            action.payload.forEach((song) => {
                newSongs[song.id] = song
            })
            return {
                ...state,
                byId: newSongs
            };
        // return state;
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
