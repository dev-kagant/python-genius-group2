import React, { useState } from "react";

export const SongPageContext = React.createContext();

const SongPageContextProvider = ({ children }) => {

    const [currentSong, setCurrentSong] = useState();

    return (
        <SongPageContext.Provider
            value = {{
                currentSong, setCurrentSong
            }}
        >
            {children}
        </SongPageContext.Provider>
    )
}

export default SongPageContextProvider;