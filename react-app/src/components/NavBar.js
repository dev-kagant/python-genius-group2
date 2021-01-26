import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './styles/navbar.css'; 

const NavBar = ({ setAuthenticated }) => {
  return (
    <nav className='navbar-container'>
      <div className='navbar-inner-container1'>
        <ul>
          <li>
            <NavLink to="/" exact={true} activeClassName="active">
              천재 Cheonjae
            </NavLink>
          </li>
          <li>
            <NavLink to="/login" exact={true} activeClassName="active">
              Login
            </NavLink>
          </li>
          <li>
            <NavLink to="/sign-up" exact={true} activeClassName="active">
              Sign Up
            </NavLink>
          </li>
          <li>
            <NavLink to="/users" exact={true} activeClassName="active">
              Users
            </NavLink>
          </li>
          <li>
            <LogoutButton setAuthenticated={setAuthenticated} />
          </li>
        </ul>
      </div>
      <div className='navbar-inner-container2'>
        <NavLink to="/charts" exact={true} activeClassName="active">
          Charts
        </NavLink>
        <NavLink to="/add-a-song" exact={true} setAuthenticated={setAuthenticated}>
          Add A Song
        </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;