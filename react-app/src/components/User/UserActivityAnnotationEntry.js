import React from "react";
import { useSelector } from "react-redux";
import { format } from "date-fns";


const UserActivityAnnotationEntry = ({ annotation }) => {
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    return ( 
        <div className="user-page_activity-container">
            <div className="activity_icon">
                <i className="fas fa-sticky-note stats-icon fa-2x"/>
            </div>
            <div className="activity_info">
                <div className="activity_heading">
                    <div className="activity_title">{`${currentViewUser.username} wrote`}</div>
                    <div className="activity_date">{format(new Date(annotation.created), "yyyy-MM-dd")}</div>
                </div>
                <div className="user-page_activity-content">
                    {annotation.annotation}
                </div>
            </div>
        </div>
    )
}

export default UserActivityAnnotationEntry;