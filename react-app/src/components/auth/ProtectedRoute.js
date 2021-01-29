import React from 'react';
import { useSelector } from 'react-redux';
import { Route, Redirect } from 'react-router-dom';

const ProtectedRoute = (props) => {
  const authenticated = useSelector(state => state.user.authenticated);

  return (
    <Route {...props}>
      {authenticated ? props.children  : <Redirect to="/login" />}
    </Route>
  )
};


export default ProtectedRoute;
