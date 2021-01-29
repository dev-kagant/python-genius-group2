import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import EditInputBox from "./EditInputBox";
import { updateUser } from "../../../store/user";
import "./EditUserForm.css";
import { useHistory } from "react-router-dom";

const EditUserForm = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.user.loggedInUser);

    const [username, setUsername] = useState(user.username || "");
    const [avatar, setAvatar] = useState(user.user_avatar || "");
    const [background, setBackground] = useState(user.user_background || "");
    const [bio, setBio] = useState(user.user_bio || "");
    const [email, setEmail] = useState(user.email || "");
    const [password, setPassword] = useState("");
    const [repeatPassword, setRepeatPassword] = useState("");

    const onUpdateUser = async (e) => {
        e.preventDefault();
        if (password === repeatPassword) {
            await dispatch(updateUser(
                username,
                avatar,
                background,
                bio,
                email,
                password
            ));
            history.push(`/users/${user.id}`)
        } else {
            alert("password doesn't match")
        }
    };

    return (
        <form onSubmit={onUpdateUser}>
            <div className="edit-user_heading">EDIT USER PROFILE</div>
            <div className="edit-user_main-left">
                <EditInputBox name="username" type="text" label="USERNAME" value={username} fn={setUsername}/>
                <EditInputBox name="user_avatar" type="text" label="AVATAR URL" value={avatar} fn={setAvatar}/>
                <EditInputBox name="user_background" type="text" label="HEADER BACKGROUND URL" value={background} fn={setBackground}/>
                {/* <div className="edit-user_input-container">
                    <label className="edit-user_input-label">USERNAME</label>
                    <input 
                        className="edit-user_input-box"
                        type="text"
                        name="username"
                        onChange={(e) => setUsername(e.target.value)}
                        value={username}
                    />
                </div>
                <div className="edit-user_input-container">
                    <label className="edit-user_input-label">AVATAR URL</label>
                    <input 
                        className="edit-user_input-box"
                        type="text"
                        name="user_avatar"
                        onChange={(e) => setAvatar(e.target.value)}
                        value={avatar}
                    />
                </div>
                <div className="edit-user_input-container">
                    <label className="edit-user_input-label">HEADER BACKGROUND URL</label>
                    <input 
                        className="edit-user_input-box"
                        type="text"
                        name="user_avatar"
                        onChange={(e) => setBackground(e.target.value)}
                        value={background}
                    />
                </div> */}
                <div className="edit-user_textarea">
                    <label className="edit-user_textarea-label">CHANGE BIO</label>
                    <textarea className="edit-user_textarea-box" value={bio} onChange={(e) => setBio(e.target.value)}/>
                </div>
            </div>
            <div className="edit-user_main-right">
                <div className="edit-user_main-right-inputs">
                    <EditInputBox name="email" type="email" label="CHANGE EMAIL" value={email} fn={setEmail}/>
                    <EditInputBox name="password" type="password" label="CHANGE PASSWORD" value={password} fn={setPassword}/>
                    <EditInputBox name="confirm_password" type="password" label="CONFIRM PASSWORD" value={repeatPassword} fn={setRepeatPassword}/>
                </div>
                <div className="edit-user_main-right-buttons">
                    <button type="submit" className="edit-user_save">Save</button>
                    <button type="button" className="edit-user_cancel">Cancel</button>
                </div>
            </div>
        </form>
    )
}

export default EditUserForm;