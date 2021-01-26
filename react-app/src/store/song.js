import { fetch } from "../services/csrf";

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
    const res = await fetch(`/songs/${id}`);
    dispatch(setCurrentSong(res.data.song));
    return res.data.song;
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