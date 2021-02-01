import React from "react";

const UserStats = ({ fa, category, subtittle, setShowSongActivity }) => {

    const toggleActivity = () => {
        if (subtittle === "SONGS") {
            setShowSongActivity(true)
        } else {
            setShowSongActivity(false)
        }
    }

    return (
        <div className="stats-container" onClick={toggleActivity}>
            <div className="stats-content">
                <i className={`fas stats-icon fa-2x ${fa}`} />
                <div className="stats-number">{category}</div>
            </div>
            <div className="stats-subtitle">{subtittle}</div>
        </div>
    )
}

export default UserStats;
