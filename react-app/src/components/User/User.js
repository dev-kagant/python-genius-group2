import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { getUserById } from "../../store/user";
import "./User.css";

function User() {
  const dispatch = useDispatch();
  // Notice we use useParams here instead of getting the params
  // From props.
  const { userId }  = useParams();
  const [loaded, setLoaded] = useState(false);
  const currentViewUser = useSelector(state => state.user.currentViewUser);

  useEffect(() => {
    (async () => {
      if (!userId) return;
      await dispatch(getUserById(userId))
      .then(() => setLoaded(true));
    })()
  }, [userId, dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <div className="user-page_container">
      <div className="user-page_header-background">
        { currentViewUser.user_background ?
          <img src={currentViewUser.user_background} /> :
          <div className="user-page_header-default-background" />
        }
      </div>
      <div className="user-page_main">
        <div className="user-page_main-left">
          <div className="user-page_header-avatar">
            { currentViewUser.user_avatar ?
              <img src={currentViewUser.user_avatar} /> :
              <div className="user-page_header-default-avatar" />
            }
          </div>
          <div className="user-page_username">@{currentViewUser.username}</div>
          <button className="user-page_edit-button">Edit</button>
          <div className="user-page_bio">
            { currentViewUser.bio ?
              currentViewUser :
              `${currentViewUser.username} is keeping quiet for now.`
            }
          </div>
          <div className="user-page_stats">
            <div className="user-page_stats-heading">STATS</div>
            <div className="user-page_stats-container">
              <div className="user-page_stats-annotation stats-container">
                <i className="fas fa-sticky-note stats-icon fa-3x" />
                <div className="stats-content">0</div>
              </div>
              <div className="user-page_stats-song stats-container">
                <i className="fas fa-sticky-note stats-icon fa-3x" />
                <div className="stats-content">0</div>
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
