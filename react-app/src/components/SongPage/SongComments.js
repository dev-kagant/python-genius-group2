import React, { useState } from 'react';
import { useSelector } from "react-redux"
import "./styles/SongComments.css";

const Comments = () => {
    const currentLoggedInUser = useSelector(state => state.user.loggedInUser);

    const [userComments, setUserComments] = useState(true)
    console.log(currentLoggedInUser)

    const commenting = () => {
        setUserComments(false)
    }
    const doneCommenting = () => {
        setUserComments(true)
    }
    const postComment = (e) => {
        e.preventDefault()
    }

    return (
        <div className="comments_container">
            {(userComments) ? (<div className="comments-container_heading">
                { currentLoggedInUser.avatar ?
                    <img src={currentLoggedInUser.avatar} /> :
                    <div className="comments_header-default-avatar" />
                }
                <input
                    placeholder="Add a comment"
                    onClick={commenting}
                />
            </div>) : (
                    <div className="comments-header_commenting">
                        <textarea
                            placeholder="Add a comment"
                        />
                        <div className="comments-header_button-box">
                            <button type="submit" onSubmit={postComment} className="comments_submit-button">Submit</button>
                            <button type="button" onClick={doneCommenting} className="comments_cancel-button">Cancel</button>
                        </div>
                    </div>)}
            <div className="comments-container_comments">
                <ul>
                    Mapping
                    <li className="solo-comment_container">
                        <div className="solo-comment_header">
                            <div>Username</div>
                            <div>Posted Date</div>
                        </div>
                        <div className="solo-comment_comment">
                            <p>Comment</p>
                        </div>
                        <div className="solo-comment_votes">
                            <button><i></i></button>
                            <div>+Votes</div>
                            <button><i></i></button>
                        </div>
                    </li>
                </ul>
            </div>
            <div className="comments_being-viewed">
                <button>Show More(45)</button>
            </div>
        </div >
    )
}

export default Comments;
