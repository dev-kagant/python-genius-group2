import React from "react";

const EditInputBox = ({ type, label, value, fn}) => {
    return (
        <div className="edit-user_input-container">
            <label className="edit-user_input-label">{label}</label>
            <input 
                className="edit-user_input-box"
                type={type}
                name="username"
                onChange={(e) => fn(e.target.value)}
                value={value}
            />
        </div>
    )
}

export default EditInputBox;