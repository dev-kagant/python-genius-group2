import { signUp } from "../services/auth";
import { fetch } from "../services/csrf";

// State
const initialState = {
    currentSong: {},
    byId: {}
}

// Action types
const GET_ALL_SONGS = "song/GET_ALL_SONGS";

const SET_CURRENT_SONG = "song/SET_CURRENT_SONG";

// POJO Actions
const getAllSongs = (songs) => ({
    type: GET_ALL_SONGS,
    payload: songs
})




const setCurrentSong = (song) => ({
    type: SET_CURRENT_SONG,
    payload: song
})

// Thunk Actions

//GET ALL OF THE SONGS
export const fetchAllSongs = () => async(dispatch) => {
    const res = await fetch("/api/songs");
    dispatch(getAllSongs(res.data.songs));
}


//GET SONG BY ID
export const getSong = (id) => async dispatch => {
    const res = await fetch(`/api/songs/${id}`);
    dispatch(setCurrentSong(res.data));
    return res.data;
}


// Reducer
const songReducer = (state=initialState, action) => {
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
