import React from "react";
import { useSelector } from "react-redux";

const UserAvatar = () => {
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    return ( 
        <div className="user-page_header-avatar">
            { currentViewUser.avatar ?
              <img src={currentViewUser.avatar} /> :
              <div className="user-page_header-default-avatar" />
            }
        </div>
    )
}

export default UserAvatar;