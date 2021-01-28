import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, Redirect } from "react-router-dom";

import { login } from "../../../store/user";
import "./LoginForm.css"

const LoginForm = () => {
  const dispatch = useDispatch();
  const authenticated = useSelector(state => state.user.authenticated);

  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const user = await dispatch(login(email, password));
    if (user.errors) {
      setErrors(user.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <form onSubmit={onLogin}>
      <div className="login-form_heading">LOGIN TO CHEONJAE GENIUS</div>
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div className="login-form_input-container">
        <label htmlFor="email" className="login-form_input-label">Email</label>
        <input
          className="login-form_input-box"
          name="email"
          type="text"
          placeholder="Email"
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className="login-form_input-container">
        <label htmlFor="password" className="login-form_input-label">Password</label>
        <input
          className="login-form_input-box"
          name="password"
          type="password"
          placeholder="Password"
          value={password}
          onChange={updatePassword}
        />
      </div>
      <button type="submit" className="login-form_submit">Log In</button>
      <Link to="/sign-up" className="login-form_redirect">CREATE AN ACCOUNT</Link>
    </form>
  );
};

export default LoginForm;
