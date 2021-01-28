// Action types
const SEARCH_SONG = 'SEARCH_SONG';
const SEARCH_FOR_ARTIST = 'SEARCH_FOR_ARTIST';
const SEARCH_IN_LYRICS = 'SEARCH_IN_LYRICS';

// POJO Actions
const searchSong = (song) => {
    return{
        type: SEARCH_SONG,
        payload: song
    }
}

const searchArtist = (artist) => {
    return{
        type: SEARCH_FOR_ARTIST,
        payload: artist
    }
}

const searchLyrics = (lyrics) => {
    return{
        type = SEARCH_IN_LYRICS,
        payload: lyrics
    }
}

// Thunk Actions
export const fetchSongTitle = (term) => async(dispatch) => {
    const res = await fetch(`/api/search?term=${encodeURIComponent(term)}`)
    dispatch(searchSong(res.data.search_song))
}
export const fetchArtistName = (term) => async(dispatch) => {
    const res = await fetch(`/api/search?term=${encodeURIComponent(term)}`)
    dispatch(searchArtist(res.data.search_artist))
}
export const fetchSongLyrics = (term) => async(dispatch) => {
    const res = await fetch(`/api/search?term=${encodeURIComponent(term)}`)
    dispatch(searchLyrics(res.data.search_lyric))
}

const initialState = [];

const searchReducer = (state= initialState, action) => {
    switch(action.type){
        case SEARCH_SONG:
            return action.payload;
        case SEARCH_FOR_ARTIST:
            return action.payload;
        case SEARCH_IN_LYRICS:
            return action.payload;
    }
}
