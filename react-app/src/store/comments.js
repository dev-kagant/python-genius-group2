
//Action types
const ADD_COMMENT = 'ADD_COMMENT';
const GET_COMMENTS = 'GET_COMMENTS';

//POJO Actions
const getComments = (comments) => ({
    type: GET_COMMENTS,
    comments
})
const addComment = (comment) => ({
    type: ADD_COMMENT,
    comment
});

//Thunk Actions
export const getSongComments = (songId) => async (dispatch) => {
    const response = await fetch(`/api/comments/${songId}`, {
        method: "GET",
    })
    if (response.ok) {
        const song = await response.json();
        dispatch(getComments(song.comments))
        console.log(song.comments)
        return song.comments
    }
}

export const addNewComment = ({ user_comment, user_Id, song_Id }) => async (dispatch) => {
    const response = await fetch("/api/comments/new_comment", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            user_comment,
            user_Id,
            song_Id
        })
    });
    if (response.ok) {
        const comment = await response.json()
        console.log(comment)
        await dispatch(addComment(comment))
    }
}



const initialState = { comments: [] }

const commentReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_COMMENTS:
            return {
                ...state,
                comments: [action.comments]
            };
        case ADD_COMMENT:
            const newComments = [...state.comments]
            newComments[0].push(action.comment)
            return {
                ...state,
                comments: newComments
            }
        default:
            return state;
    }
}

export default commentReducer;
