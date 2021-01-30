import React from "react";
import { useSelector } from "react-redux";

const UserBackground = () => {
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    return ( 
        <div className="user-page_header-background">
            { currentViewUser.background ?
            <img src={currentViewUser.background} /> :
            <div className="user-page_header-default-background" />
            }
        </div>
    )
}

export default UserBackground;