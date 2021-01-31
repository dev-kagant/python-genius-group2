// Initial State
const initialState = {
    currentSongAnnotations: []
}

// Action Types
const SET_CURRENT_SONG_ANNOTATIONS = "SET_CURRENT_SONG_ANNOTATIONS";


// POJO Actions
export const setCurrentSongAnnotations = (annotations) => ({
    type: SET_CURRENT_SONG_ANNOTATIONS,
    payload: annotations
})



//--------------------- Thunk Actions ---------------------

// POST NEW ANNOTATION
export const postAnnotation = (song_Id, annotation, start, end) => 
    async dispatch => {
    const response = await fetch("/api/annotations/create", {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            song_Id,
            annotation,
            start,
            end
        })
    });

    return response;
}

// GET CURRENT SONG ANNOTATIONS
export const getCuurentSongAnnotations = (id) => async dispatch => {
    const response = await fetch(`/api/annotations/get/songs/${id}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(setCurrentSongAnnotations(data))
        return data;
    }
}

//--------------------- Reducer ---------------------
const annotationReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_CURRENT_SONG_ANNOTATIONS:
            return {
                ...state,
                currentSongAnnotations: action.payload
            };
        default:
            return state;
    }
}

export default annotationReducer;