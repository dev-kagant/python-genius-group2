import React from "react";
import { useSelector } from "react-redux";

const UserBio = () => {
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    return ( 
        <div className="user-page_bio">
            { currentViewUser.bio ?
            currentViewUser.bio :
            `${currentViewUser.username} is keeping quiet for now.`
            }
        </div>
    )
}

export default UserBio;