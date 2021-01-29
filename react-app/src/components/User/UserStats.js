import React from "react";

const UserStats = ({ fa, category, subtittle }) => {

    return ( 
        <div className="stats-container">
            <div className="stats-content">
                <i className={`fas stats-icon fa-2x ${fa}`} />
                <div className="stats-number">{category}</div>
            </div>
            <div className="stats-subtitle">{subtittle}</div>
        </div>
    )
}

export default UserStats;