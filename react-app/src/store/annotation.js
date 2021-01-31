// Initial State
const initialState = {
    currentSongAnnotations: []
}

// Action Types
const SET_CURRENT_SONG_ANNOTATIONS = "SET_CURRENT_SONG_ANNOTATIONS";
const SET_CURRENT_ANNOTATION = "SET_CURRENT_ANNOTATION";

// POJO Actions
export const setCurrentSongAnnotations = (annotations) => ({
    type: SET_CURRENT_SONG_ANNOTATIONS,
    payload: annotations
})

export const setCurrentAnnotation = (annotation) => ({
    type: SET_CURRENT_ANNOTATION,
    payload: annotation
})


//--------------------- Thunk Actions ---------------------

// POST NEW ANNOTATION
export const postAnnotation = (newAnnotation) => async dispatch => {
    const { song_Id, annotation, start, end, lyrics } = newAnnotation;
    console.log(lyrics)
    const response = await fetch("/api/annotations/create", {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            song_Id,
            annotation,
            start,
            end,
            lyrics
        })
    });
    return response;
}

// EDIT ANNOTATION
export const editAnnotation = (editedAnnotation, id) => async dispatch => {
    const response = await fetch (`/api/annotations/patch/${id}`, {
        method: "PATCH",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({"annotation": editedAnnotation})
    })
    if (response.ok) {
        const data = await response.json();
        dispatch(setCurrentAnnotation(data))
        return response;
    }
}

// DELETE ANNOTATION
export const deleteAnnotation = (id) => async dispatch => {
    const response = await fetch(`/api/annotations/delete/${id}`, {
        method: "DELETE",
        headers: {
            "content-type": "application/json"
        },
    })
    if (response.ok) {
        const data = await response.json();
        dispatch(setCurrentAnnotation(null))
    }
}

// GET CURRENT SONG ANNOTATIONS
export const getCurrentSongAnnotations = (id) => async dispatch => {
    const response = await fetch(`/api/annotations/get/songs/${id}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(setCurrentSongAnnotations(data))
        return data;
    }
}

// GET ANNOTATION BY ID
export const getAnnotationById = (id) => async dispatch => {
    const response = await fetch(`/api/annotations/get/${id}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(setCurrentAnnotation(data))
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
        case SET_CURRENT_ANNOTATION:
            return {
                ...state,
                currentAnnotation: action.payload
            };
        default:
            return state;
    }
}

export default annotationReducer;