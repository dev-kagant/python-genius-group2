import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';

import { logout } from '../../store/user';
import '../NavBar/navbar.css';

const LogoutButton = () => {
  const dispatch = useDispatch();
  const history = useHistory();

  const onLogout = async (e) => {
    await dispatch(logout());
    history.push('/');
  };

  return <button className='logout' onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
