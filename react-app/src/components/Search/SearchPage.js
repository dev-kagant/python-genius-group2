import React from "react";
import { useSelector } from "react-redux";
import "./styles/search.css";

function SearchPage(){
    const songInfo = useSelector(state => state.search.song);
    const artistInfo = useSelector(state => state.search.artist);
    const lyricsInfo = useSelector(state => state.search.lyrics);

    return(
        <div className="search-page_container">
            <ul className="search-page_songInfo"> Songs {
                songInfo && songInfo.map((song)=>(
                    <div className="search-song_data" key={song.title}>
                        <li><img className="song-img" src={song.song_icon} /></li>
                        <h1>{song.title}</h1>
                        <h1>{song.artist}</h1>
                    </div>
                ))
            }</ul>
            <div className="artistInfo"> Artists {
                artistInfo && artistInfo.map((artist)=> (
                    <div key={artist.artist}>
                        <img src={artist.song_icon} />
                        <h1>{artist.artist}</h1>
                    </div>
                ))
            }</div>
            <div className="lyricsInfo"> Lyric Matches{
                lyricsInfo && lyricsInfo.map((lyrics)=>(
                    <div key={lyrics.lyrics}>
                        <img src={lyrics.song_icon} />
                        <h1>{lyrics.title}</h1>
                        <h1>{lyrics.artist}</h1>
                        <h1>{lyrics.album}</h1>
                        <p>{lyrics.lyrics}</p>
                    </div>
                ))
            }</div>
        </div>
    )
}

export default SearchPage;
