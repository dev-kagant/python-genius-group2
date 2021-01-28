import React from "react";
import { useSelector } from "react-redux";
import "./styles/search.css";

function SearchPage(){
    const songInfo = useSelector(state => state.search.song);
    const artistInfo = useSelector(state => state.search.artist);
    const lyricsInfo = useSelector(state => state.search.lyrics);

    // const songArr = Object.values(songInfo);
    // const artistArr = Object.values(artistInfo);
    // const lyricsArr = Object.values(lyricsInfo);

    return(
        <div>
            <div className="songInfo"> Songs {
                songInfo && songInfo.map((song)=>(
                    <div key={song.title}>
                        <img src={song.song_icon} />
                        <h1>{song.title}</h1>
                        <h1>{song.artist}</h1>
                    </div>
                ))
            }</div>
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
