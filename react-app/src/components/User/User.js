import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import EditUserModal from "../auth/EditUserModal/EditUserModal";
import { getUserById } from "../../store/user";
import "./User.css";

function User() {
  const dispatch = useDispatch();
  const history = useHistory();
  // Notice we use useParams here instead of getting the params
  // From props.
  const { userId }  = useParams();
  const [loaded, setLoaded] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const currentViewUser = useSelector(state => state.user.currentViewUser);
  const loggedInUser = useSelector(state => state.user.loggedInUser);

  useEffect(() => {
    (async () => {
      if (!userId) return;
      const res = await dispatch(getUserById(userId))
      res.ok ? setLoaded(true) : history.push("/404");
    })()
  }, [userId, dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <div className="user-page_container">
      {showForm && <EditUserModal setShowForm={setShowForm}/>}
      <div className="user-page_header-background">
        { currentViewUser.background ?
          <img src={currentViewUser.background} /> :
          <div className="user-page_header-default-background" />
        }
      </div>
      <div className="user-page_main">
        <div className="user-page_main-left">
          <div className="user-page_header-avatar">
            { currentViewUser.avatar ?
              <img src={currentViewUser.avatar} /> :
              <div className="user-page_header-default-avatar" />
            }
          </div>
          <div className="user-page_username">@{currentViewUser.username}</div>
          { userId == loggedInUser.id ?
            <button 
              className="user-page_edit-button" 
              onClick={() => setShowForm(true)}
            >Edit</button> :
            <></>
          }
          <div className="user-page_bio">
            { currentViewUser.bio ?
              currentViewUser.bio :
              `${currentViewUser.username} is keeping quiet for now.`
            }
          </div>
          <div className="user-page_stats">
            <div className="user-page_stats-heading">STATS</div>
            <div className="user-page_stats-container">
              <div className="stats-container">
                <div className="stats-content">
                  <i className="fas fa-sticky-note stats-icon fa-2x" />
                  <div className="stats-number">{currentViewUser.annotations.length}</div>
                </div>
                <div className="stats-subtitle">ANNOTATION</div>
              </div>
              <div className="stats-container">
                <div className="stats-content">
                  <i className="fas fa-sticky-note stats-icon fa-2x" />
                  <div className="stats-number">{currentViewUser.songs.length}</div>
                </div>
                <div className="stats-subtitle">SONGS</div>
              </div>
            </div>
          </div>
        </div>
        <div className="user-page_main-right">
          <div className="user-page_activities">
            <div className="user-page_activity-heading">ACTIVITIES</div>
            <div className="user-page_activity-items"></div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default User;
