import { useSelector } from "react-redux";
import "./styles/search.css";

function SearchPage(){
    const songInfo = useSelector(state => Object.values(state.search.song));
    const artistInfo = useSelector(state => Object.values(state.search.artist));
    const lyricsInfo = useSelector(state => Object.values(state.search.lyrics));

    return(
        <div>
            <div className="songInfo"></div>
            <div className="artistInfo"></div>
            <div className="lyricsInfo"></div>
        </div>
    )
}
