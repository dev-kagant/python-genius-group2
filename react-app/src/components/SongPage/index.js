import React from "react";

const Song = () => {
    return (
        <div className="songpage_container">
            <div className="songpage_header">
                <div className="songpage-header_overlay">
                    <div className="songpage-header_details">
                        <div className="">Album Artwork
                            <img />
                        </div>
                        <div className="">
                            <p>Song Title</p>
                            <p>Artist</p>
                            <p>Album</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="songpage_main">
                <div className="songpage-main_left">
                    <button>Edit Lyrics</button>
                    <button>Edit Song Facts</button>
                    <p>Lyrics</p>
                </div>
                <div className="songpage-main_right">
                    <div>Song Facts</div>
                    <div>Song Bio</div>
                    <div>Video Url</div>
                </div>  
                <div>Song Player</div>              
            </div>
        </div>
    )
}

export default Song;
