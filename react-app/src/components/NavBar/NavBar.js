import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './navbar.css';

const NavBar = () => {
  const authenticated = useSelector(state => state.user.authenticated);
  const loggedInUser = useSelector(state => state.user.loggedInUser);
  const [searchKeyword, setSearchKeyword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
  }

  return (
    <nav className='navbar_container'>
      <div className="navbar_top">
        <div className='navbar_search-container'>
          <form className="nav-search__form" onSubmit={handleSubmit}>
            <input 
              className="nav-search__input" 
              placeholder="Search"
              type="search"
              name="search"
              onChange={(e) => setSearchKeyword(e.target.value)}
              value={searchKeyword}
            />
            <button className="nav-search__submit" type="submit">
              <i className="fas fa-search fa-lg"></i>
            </button>
          </form>
        </div>
        <div className="navbar_logo-container">
          <NavLink 
            to="/" 
            exact={true} 
            activeClassName="active" 
            className="home-link navbar_links"
          >
            천재
          </NavLink>
        </div>
        <div className="navbar_buttons-container">
          { 
            !authenticated ? 
            <>
              <NavLink to="/login" exact={true} className="login-link navbar_links"> Login </NavLink>
              <NavLink to="/sign-up" exact={true} className="signup-link navbar_links"> Sign Up </NavLink> 
            </> :
            <>
              {loggedInUser && 
                <NavLink 
                  to={`/users/${loggedInUser.id}`} 
                  exact={true} 
                  className="users-link navbar_links"
                >
                  {loggedInUser.username}
                </NavLink>
              }
              <LogoutButton className='logout' />
            </>
          }
        </div>
      </div>
      <div className='navbar_bottom'>
        <NavLink 
          to="/charts" 
          className="navbar_bottom-links navbar-charts navbar_links" 
          exact={true} 
          activeClassName="active navbar_links"
        >
          Charts
        </NavLink>
        <NavLink 
          to="/add-a-song" 
          className="navbar_bottom-links navbar-add-a-song navbar_links" 
          exact={true} 
        >
          Add A Song
        </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
