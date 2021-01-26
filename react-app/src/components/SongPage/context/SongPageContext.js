import React, { useState } from "react";

import { fetch } from "../../../services/csrf";

export const SongPageContext = React.createContext();

const SongPageContextProvider = ({ children }) => {
    // States
    const [currentSong, setCurrentSong] = useState();

    // Helper functions
    const loadSong = async (id) => {
        const res = await fetch(`/songs/{id}`)
        return res.data;
    }

    return (
        <SongPageContext.Provider
            value = {{
                currentSong, 
                setCurrentSong,
                loadSong
            }}
        >
            {children}
        </SongPageContext.Provider>
    )
}

export default SongPageContextProvider;