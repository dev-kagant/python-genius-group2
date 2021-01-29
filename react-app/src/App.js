import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from 'react-redux';

import ProtectedRoute from "./components/auth/ProtectedRoute";
import HomePage from "./components/HomePage/Home";
import NavBar from "./components/NavBar/NavBar";
import LoginModal from "./components/auth/LoginModal/LoginModal";
import SignUpModal from "./components/auth/SignUpModal/SingUpModal";
import UsersList from "./components/UsersList";
import User from "./components/User/User";
import Song from "./components/SongPage";
import SongAddForm from "./components/SongPage/SongAddForm";

import { authenticate } from "./store/user";
import SongTrends from "./components/HomePage/SongTrends";
import Charts from "./components/Charts/Charts";

function App() {
  const dispatch = useDispatch();
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <HomePage />
          <LoginModal />
        </Route>
        <Route path="/sign-up" exact={true}>
          <HomePage />
          <SignUpModal />
        </Route>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>
        <Route path="/" exact={true} >
          <HomePage />
        </Route>
        <Route path="/charts">
          <Charts />
        </Route>
        <Route path="/songs/:songId" exact={true}>
          <Song />
        </Route>
        <ProtectedRoute path="/add-a-song" exact={true} >
          <SongAddForm />
        </ProtectedRoute>
        <Route path="/404" exact={true}>
          <h1>Sorry Page Not Found.</h1>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
