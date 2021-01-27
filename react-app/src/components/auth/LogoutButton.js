import React from "react";
import { logout } from "../../services/auth";
import '../styles/navbar.css';

const LogoutButton = ({setAuthenticated}) => {
  const onLogout = async (e) => {
    await logout();
    setAuthenticated(false);
  };

  return <button className='logout' onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
