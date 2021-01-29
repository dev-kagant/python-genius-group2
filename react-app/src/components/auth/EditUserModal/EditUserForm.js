import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import EditInputBox from "./EditInputBox";
import { updateUser } from "../../../store/user";
import "./EditUserForm.css";
import { useHistory } from "react-router-dom";

const EditUserForm = ({ closeModal }) => {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.user.loggedInUser);

    const [errors, setErrors] = useState();
    const [username, setUsername] = useState(user.username || "");
    const [avatar, setAvatar] = useState(user.avatar || "");
    const [background, setBackground] = useState(user.background || "");
    const [bio, setBio] = useState(user.bio || "");
    const [email, setEmail] = useState(user.email || "");
    const [password, setPassword] = useState(user.password || "");
    const [repeatPassword, setRepeatPassword] = useState("");

    const onUpdateUser = async (e) => {
        e.preventDefault();
        if (password === repeatPassword) {
            const res = await dispatch(updateUser(
                username,
                avatar,
                background,
                bio,
                email,
                password
            ))
            if (res) setErrors(res);
            closeModal();
        } else {
            alert("password doesn't match")
        }
    };

    return (
        <form onSubmit={onUpdateUser} className="edit-user_form">
            <div className="edit-user_heading">EDIT USER PROFILE</div>
            {errors && errors.map(err => {
                return <div>{err}</div>
            })}
            <div className="edit-user_main">
                <div className="edit-user_main-left">
                    <EditInputBox type="text" label="USERNAME" value={username} fn={setUsername}/>
                    <EditInputBox type="text" label="AVATAR URL" value={avatar} fn={setAvatar}/>
                    <EditInputBox type="text" label="HEADER BACKGROUND URL" value={background} fn={setBackground}/>
                    <div className="edit-user_textarea">
                        <label className="edit-user_textarea-label">CHANGE BIO</label>
                        <textarea className="edit-user_textarea-box" value={bio} onChange={(e) => setBio(e.target.value)}/>
                    </div>
                </div>
                <div className="edit-user_main-right">
                    <div className="edit-user_main-right-inputs">
                        <EditInputBox type="email" label="CHANGE EMAIL" value={email} fn={setEmail}/>
                        <EditInputBox type="password" label="CHANGE PASSWORD" fn={setPassword}/>
                        <EditInputBox type="password" label="CONFIRM PASSWORD" fn={setRepeatPassword}/>
                    </div>
                    <div className="edit-user_main-right-buttons">
                        <button type="submit" className="edit-user_save">Save</button>
                        <button type="button" className="edit-user_cancel" onClick={closeModal}>Cancel</button>
                    </div>
                </div>
            </div>
        </form>
    )
}

export default EditUserForm;