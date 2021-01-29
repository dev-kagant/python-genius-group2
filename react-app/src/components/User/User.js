import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import EditUserModal from "../auth/EditUserModal/EditUserModal";
import { getUserById } from "../../store/user";
import UserBackground from "./UserBackground";
import UserAvatar from "./UserAvatar";
import UserBio from "./UserBio";
import UserStats from "./UserStats";
import UserActivitySongEntry from "./UserActivitySongEntry";
import UserActivityAnnotationEntry from "./UserActivityAnnotationEntry";
import "./User.css";

function User() {
  const dispatch = useDispatch();
  const history = useHistory();
  // Notice we use useParams here instead of getting the params
  // From props.
  const { userId }  = useParams();
  const [loaded, setLoaded] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [showSongActivity, setShowSongActivity] = useState(true); 
  const currentViewUser = useSelector(state => state.user.currentViewUser);
  const loggedInUser = useSelector(state => state.user.loggedInUser);

  console.log(showSongActivity)

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
      <UserBackground />
      <div className="user-page_main">
        <div className="user-page_main-left">
          <UserAvatar />
          <div className="user-page_username">@{currentViewUser.username}</div>
          { userId == loggedInUser.id ?
            <button 
              className="user-page_edit-button" 
              onClick={() => setShowForm(true)}
            >Edit</button> :
            null
          }
          <UserBio />
          <div className="user-page_stats">
            <div className="user-page_stats-heading">STATS</div>
            <div className="user-page_stats-container">
              <UserStats 
                fa="fa-sticky-note" 
                category={currentViewUser.annotations.length} 
                subtittle="ANNOTATIONS"
                setShowSongActivity={setShowSongActivity}
              />
              <UserStats 
                fa="fa-sticky-note" 
                category={currentViewUser.songs.length} 
                subtittle="SONGS"
                setShowSongActivity={setShowSongActivity}
              />
            </div>
          </div>
        </div>
        <div className="user-page_main-right">
          <div className="user-page_activities">
            <div className="user-page_activity-heading">ACTIVITIES</div>
            { showSongActivity ?  
              currentViewUser.songs.map(song => {
                return <UserActivitySongEntry song={song}/>
              }) :
              currentViewUser.annotations.map(annotation => {
                return <UserActivityAnnotationEntry annotation={annotation}/>
              })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default User;
