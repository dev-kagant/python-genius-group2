// State
const initialState = {
    authenticated: false,
    loggedInUser: null
}

// Action Types
const IS_AUTHENTICATED = "user/IS_AUTHENTICATED";
const NOT_AUTHENTICATED = "user/NOT_AUTHENTICATED";
const SET_LOGGINED_USER = "user/SET_LOGGINED_USER";

// POJO Actions
export const isAuthenticated = () => ({
    type: IS_AUTHENTICATED,
    payload: true
})

export const notAuthenticated = () => ({
    type: NOT_AUTHENTICATED,
    payload: false
})

export const setLogginedUser = (user) => ({
    type: SET_LOGGINED_USER,
    payload: user
})

// Thunk Actions
export const login = (email, password) => async dispatch => {
    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            password
        })
    });
    const data = await response.json();
    if (response.ok) {
        dispatch(isAuthenticated()); 
        dispatch(setLogginedUser(data));
    };
    return data;
}

export const signUp = (username, email, password) => async dispatch => {
    const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username,
            email,
            password,
        }),
    });
    const data = await response.json();
    if (response.ok) {
        dispatch(isAuthenticated()); 
        dispatch(setLogginedUser(data));
    };
    return data;
}

export const logout = () => async dispatch => {
    const response = await fetch("/api/auth/logout", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    if (response.ok) {
        dispatch(notAuthenticated()); 
        dispatch(setLogginedUser(null));
    };
};

export const authenticate = () => async dispatch => {
    const response = await fetch('/api/auth/',{
        headers: {
            'Content-Type': 'application/json'
        }
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(isAuthenticated()); 
        dispatch(setLogginedUser(data));
        return data;
    } 
}


// Reducer
const userReducer = (state=initialState, action) => {
    switch (action.type) {
        case SET_LOGGINED_USER:
            return {
                ...state,
                loggedInUser: action.payload
            };
        case IS_AUTHENTICATED:
            return {
                ...state,
                authenticated: action.payload
            };
        case NOT_AUTHENTICATED:
            return {
                ...state,
                authenticated: action.payload
            };
        default:
            return state;
    }
}

export default userReducer;