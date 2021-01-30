import React from "react";
import { useSelector } from "react-redux";
import { format } from "date-fns";
import { useHistory } from "react-router-dom";

const UserActivitySongEntry = ({ song }) => {
    const history = useHistory();
    const currentViewUser = useSelector(state => state.user.currentViewUser);

    const toSongPage = () => {
        history.push(`/songs/${song.id}`)
    }

    return ( 
        <div className="user-page_activity-container" onClick={toSongPage}>
            <div className="activity_icon">
                {   song.song_icon ?
                    <img src={song.song_icon}/> :
                    <div className="activity_default-icon"/>
                }
            </div>
            <div className="activity_info">
                <div className="activity_heading">
                    <div className="activity_title">{`${currentViewUser.username} posted`}</div>
                    <div className="activity_date">{format(new Date(song.created), "yyyy-MM-dd")}</div>
                </div>
                <div className="activity_content-song">
                    {song.title}
                </div>
            </div>
        </div>
    )
}

export default UserActivitySongEntry;