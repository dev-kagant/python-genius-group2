import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import SearchBar from '../Search/SearchBar';
import './navbar.css';

const NavBar = () => {
  const authenticated = useSelector(state => state.user.authenticated);
  const loggedInUser = useSelector(state => state.user.loggedInUser);

  return (
    <nav className='navbar__container'>
      <div className='navbar__top'>
        <div className='navbar__search-container'>
          <SearchBar />
        </div>
        <div className='navbar__logo-container'>
          <NavLink
            to='/'
            exact
            activeClassName='active'
            className='home-link'
          >
            천재
          </NavLink>
        </div>
        <div className='navbar__buttons-container'>
          {authenticated && loggedInUser && (
            <>
              <NavLink
                to={`/users/${loggedInUser.id}`}
                className='auth-link'
                exact
              >
                {loggedInUser.username}
              </NavLink>
              <LogoutButton className='logout' />
            </>
          )}
          {!authenticated && (
            <>
              <NavLink to='/login' exact className='auth-link'> Login </NavLink>
              <NavLink to='/sign-up' exact className='auth-link'> SignUp </NavLink>
            </>
          )}
        </div>
      </div>
      <div className='navbar__bottom'>
        <div className='navbar__bottom-buttons'>
          <NavLink
            to='/charts'
            className='navbar__bottom-links navbar__chart-link'
            activeClassName='active'
            exact
          >
            CHARTS
          </NavLink>
          <NavLink
            to='/add-a-song'
            className='navbar__bottom-links navbar__add-song-link'
            exact
          >
            ADD A SONG
          </NavLink>
        </div>

      </div>
    </nav>
  );
};

export default NavBar;
