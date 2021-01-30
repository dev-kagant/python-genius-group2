import React, { useState } from 'react';
import "./styles/SongComments.css";

const Comments = () => {

    const [userComments, setUserComments] = useState(true)


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
                <div>User Id</div>
                <input
                    placeholder="Add a comment"
                    onClick={commenting}
                />
            </div>) : (
                    <div className="comments-container_heading">
                        <textarea
                            placeholder="Add a comment"
                        />
                        <button type="submit" onSubmit={postComment} onClick={doneCommenting}>Submit</button>
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
