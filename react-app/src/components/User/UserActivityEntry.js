import React from "react";
import { useSelector } from "react-redux";

const UserActivityEntry = () => {
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    return ( 
        <div className="user-page_activity-items"></div>
    )
}

export default UserActivityEntry;