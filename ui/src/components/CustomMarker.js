import React, { useState } from "react";
import { Tooltip } from "@mui/material";
import { Popover } from "@mui/material";
import { Paper } from "@mui/material";
import { propTypes } from "google-map-react";
export const createMarker = (nr, lat, lng, info, url) => {
  const [hover, setHover] = useState(false);

  return (
    <div
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      lat={lat}
      lng={lng}
      style={{
        position: "absolute",
        width: 20,
        height: 20,

        border: "5px solid #f44336",
        borderRadius: 20,
        backgroundColor: "white",
        textAlign: "center",
        color: "#3f51b5",
        fontSize: 16,
        fontWeight: "bold",
        padding: 4,
      }}
      onClick={() => console.log("abcd")}
    >
      <Tooltip
        style={{ cursor: "pointer" }}
        placement="right"
        title={info}
        onClick={() => open(url)}
      >
        <div>{nr}</div>
      </Tooltip>
    </div>
  );
};
