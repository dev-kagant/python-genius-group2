import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import ProtectedRoute from './components/auth/ProtectedRoute';
import Home from './components/Home/Home';
import NavBar from './components/NavBar/NavBar';
import LoginModal from './components/auth/LoginModal/LoginModal';
import SignUpModal from './components/auth/SignUpModal/SingUpModal';
import UsersList from './components/UsersList';
import User from './components/User/User';
import Song from './components/SongPage';
import SongAddForm from './components/SongPage/SongAddForm';
import SearchPage from './components/Search/SearchPage';
import Footer from './components/Footer/Footer';

import { authenticate } from './store/user';

function App () {
  const dispatch = useDispatch();
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
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
        <Route path='/login' exact>
          <Home />
          <LoginModal />
        </Route>
        <Route path='/sign-up' exact>
          <Home />
          <SignUpModal />
        </Route>
        <ProtectedRoute path='/users' exact>
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact>
          <User />
        </ProtectedRoute>
        <Route path='/' exact>
          <Home />
        </Route>
        <Route path='/charts'>
          <Home />
        </Route>
        <Route path='/songs/:songId' exact>
          <Song />
        </Route>
        <ProtectedRoute path='/add-a-song' exact>
          <SongAddForm />
        </ProtectedRoute>
        <Route path='/search'>
          <SearchPage />
        </Route>
        <Route path='/404' exact>
          <h1>Sorry Page Not Found.</h1>
        </Route>
        <Route>
          <h1>Sorry Page Not Found.</h1>
        </Route>
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
