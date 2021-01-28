import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, Redirect } from 'react-router-dom';
import { signUp } from "../../../store/user";
import "./SignUpForm.css";

const SignUpForm = () => {
  const dispatch =useDispatch();
  const authenticated = useSelector(state => state.user.authenticated);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const user = await dispatch(signUp(username, email, password));
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div className="signup-form_heading">SIGN UP FOR CHEONJAE GENIUS</div>
      <div className="signup-form_input-container">
        <label className="signup-form_input-label">User Name</label>
        <input 
          className="signup-form_input-box"
          type="text"
          name="username"
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div className="signup-form_input-container">
        <label className="signup-form_input-label">Email</label>
        <input 
          className="signup-form_input-box"
          type="text"
          name="email"
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div className="signup-form_input-container">
        <label className="signup-form_input-label">Password</label>
        <input 
          className="signup-form_input-box"
          type="password"
          name="password"
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div className="signup-form_input-container">
        <label className="signup-form_input-label">Repeat Password</label>
        <input 
          className="signup-form_input-box"
          type="password"
          name="repeat_password"
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <button type="submit" className="signup-form_submit">Sign Up</button>
      <Link to="/login" className="signup-form_redirect">ALREADY HAVE AN ACCOUNT? SIGN IN HERE</Link>
    </form>
  );
};

export default SignUpForm;
