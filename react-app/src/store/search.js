// Action types
const SEARCH_SONG = 'SEARCH_SONG';
const SEARCH_FOR_ARTIST = 'SEARCH_FOR_ARTIST';
const SEARCH_IN_LYRICS = 'SEARCH_IN_LYRICS';

// POJO Actions
const searchSong = (song) => ({
    type: SEARCH_SONG,
    payload: song
})

const searchArtist = (artist) => ({
    type: SEARCH_FOR_ARTIST,
    payload: artist
})

const searchLyrics = (lyrics) => ({
    type: SEARCH_IN_LYRICS,
    payload: lyrics
})

// Thunk Actions
export const fetchSongInfo = (term) => async(dispatch) => {
    const res = await fetch(`/api/search?term=${encodeURIComponent(term)}`)

    // destructure res
    const data = await res.json();
    const artist = data.song_artist;
    const song = data.search_song;
    const lyrics = data.song_lyric;

    // make dispatch actions below
    dispatch(searchSong(song));
    dispatch(searchArtist(artist));
    dispatch(searchLyrics(lyrics));
}

const initialState = {song: null, artist: null, lyrics: null};

const searchReducer = (state=initialState, action) => {
    switch(action.type){
        case SEARCH_SONG:
            return {
                ...state,
                song: action.payload
            }
        case SEARCH_FOR_ARTIST:
            return {
                ...state,
                artist: action.payload
            }
        case SEARCH_IN_LYRICS:
            return {
                ...state,
                lyrics: action.payload
            }
        default:
            return state;
    }
}

export default searchReducer;
