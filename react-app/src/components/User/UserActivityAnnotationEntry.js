import React from "react";
import { useSelector } from "react-redux";

const UserActivityAnnotationEntry = ({ annotation }) => {
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    return ( 
        <div className="user-page_activity-container">
            <div className="user-page_activity-icon">
                <i className="fas fa-sticky-note stats-icon fa-2x"/>
            </div>
            <div className="user-page_activity-info">
                <div className="user-page_activity-heading">
                    <div className="activity_title">{`${currentViewUser} wrote`}</div>
                    <div className="activity_date">{annotation.created}</div>
                </div>
                <div className="user-page_activity-content">
                    {annotation.song_facts}
                </div>
            </div>
        </div>
    )
}

export default UserActivityAnnotationEntry;