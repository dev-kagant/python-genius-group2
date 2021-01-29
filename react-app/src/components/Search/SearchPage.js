import React from "react";
import { useSelector } from "react-redux";
import {useHistory} from "react-router-dom";
import "./styles/search.css";

function SearchPage(){
    const history = useHistory();

    const songInfo = useSelector(state => state.search.song);
    const artistInfo = useSelector(state => state.search.artist);
    const lyricsInfo = useSelector(state => state.search.lyrics);

    return(
        <div className="search-page_container">
            <ul className="search-page_songInfo"> Songs {
                songInfo && songInfo.map((song)=>(
                    <div className="search-song_data" key={song.title} onClick={()=>history.push(`songs/${song.id}`)}>
                        <li><img className="song-img" src={song.song_icon} alt={song.title}/></li>
                        <div className="song-title"><li>{song.title}</li></div>
                        <div className="song-artist"><li>{song.artist}</li></div>
                    </div>
                ))
            }</ul>
            <ul className="search-page_artistInfo"> Artists {
                artistInfo && artistInfo.map((artist)=> (
                    <div className="search-artist_data" key={artist.artist} onClick={()=>history.push(`songs/${artist.id}`)}>
                        <li><img className="artist-img" src={artist.song_icon} /></li>
                        <div className="artist-name"><li>{artist.artist}</li></div>
                    </div>
                ))
            }</ul>
            <ul className="search-page_lyricsInfo"> Lyric Matches{
                lyricsInfo && lyricsInfo.map((lyrics)=>(
                    <div className="search-lyrics_data" key={lyrics.lyrics} onClick={()=>history.push(`songs/${lyrics.id}`)}>
                        <div className="lyric-container">
                            <div className="lyric-title">{lyrics.title}</div>
                            <li><img className="lyrics-img" src={lyrics.song_icon} /></li>
                            <div className="lyric-artist">{lyrics.artist}</div>
                            <div className="album-name">{lyrics.album}</div>
                        </div>
                        <div className="lyrics"><li><p>{lyrics.lyrics}</p></li></div>
                    </div>
                ))
            }</ul>
        </div>
    )
}

export default SearchPage;
