import React from "react";
import { Typography, Card, CardContent } from "@mui/material";
import GoogleMapReact from "google-map-react";
import { CustomImageList } from "../components/CustomImageList";

const createMarker = (nr, lat, lng) => (
  <div
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
    {nr}
  </div>
);

export const Recommendations = (props) => {
  const defaultProps = {
    center: {
      lat: 51.96,
      lng: 7.65,
    },
    zoom: 12,
  };
  console.log(props.recoData.wines);
  return (
    <>
      <Card>
        <CardContent>
          <Typography variant="h5">Wines you might like</Typography>
          <CustomImageList
            data={props.recoData.wines}
            id={"id"}
            pictureUrl={"picture_url"}
            label={"name"}
            onClick={(elem) => window.open("/wine/" + elem.id, "_self")}
          />
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          <Typography variant="h5">Winesellers you might like</Typography>
          <div style={{ height: "30vh", width: "100%" }}>
            <GoogleMapReact
              bootstrapURLKeys={{ key: "" }}
              defaultCenter={defaultProps.center}
              defaultZoom={defaultProps.zoom}
            >
              {createMarker(1, "51.96", "7.65")}
              {createMarker(2, "51.97", "7.62")}
              {createMarker(3, "51.95", "7.63")}
            </GoogleMapReact>
          </div>
        </CardContent>
      </Card>
    </>
  );
};
