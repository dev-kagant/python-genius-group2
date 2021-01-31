import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";

import songReducer from "./song";
import userReducer from "./user";
import searchReducer from "./search";
import annotationReducer from "./annotation";

// Reducer
const rootReducer = combineReducers({
    song: songReducer,
    user: userReducer,
    search: searchReducer,
    annotation: annotationReducer
})

// Store Enhancer
let enhancer;

if (process.env.NODE_ENV === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require("redux-logger").default;
  const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

// Store Creator
const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
