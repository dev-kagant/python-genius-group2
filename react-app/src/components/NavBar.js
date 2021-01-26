import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './styles/navbar.css';

const NavBar = ({ setAuthenticated }) => {
  return (
    <nav className='navbar-container'>
      <div >
        <ul className='navbar-inner-container1'>
          <li>
            <input type="search" placeholder="Search bar" />
          </li>
          <li>
            <NavLink to="/" exact={true} activeClassName="active" className="home-link">
              천재
            </NavLink>
          </li>
          <div>
            <li>
              <NavLink to="/login" exact={true} activeClassName="active" className="login-link">
                Login
              </NavLink>
            </li>
            <li>
              <NavLink to="/sign-up" exact={true} activeClassName="active" className="signup-link">
                Sign Up
              </NavLink>
            </li>
            <li>
              <NavLink to="/users" exact={true} activeClassName="active" className="users-link">
                Users
              </NavLink>
            </li>
            <li>
              <LogoutButton setAuthenticated={setAuthenticated} />
            </li>
          </div>
        </ul>
      </div>
      <div className='navbar-inner-container2'>
        <NavLink to="/charts" className="second-nav-links" exact={true} activeClassName="active">
          Charts
        </NavLink>
        <NavLink to="/add-a-song" className="second-nav-links" exact={true} setAuthenticated={setAuthenticated}>
          Add A Song
        </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
