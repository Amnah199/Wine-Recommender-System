import React from "react";
import { Typography, Card, CardContent, CardHeader } from "@mui/material";
import GoogleMapReact from "google-map-react";
import { CustomImageList } from "../components/CustomImageList";
import { createMarker } from "../components/CustomMarker";

export const Recommendations = (props) => {
  const defaultProps = {
    center: {
      lat: 51.96,
      lng: 7.65,
    },
    zoom: 12,
  };
  return (
    <>
      <Card style={{ marginTop: "1rem" }}>
        <CardContent>
          <CardHeader title="Wines you might like" />
          <CustomImageList
            data={props.recoData.wines}
            id={"id"}
            pictureUrl={"picture_url"}
            label={"name"}
            cols={4}
            onClick={(elem) => window.open("/wine/" + elem.id, "_self")}
          />
        </CardContent>
      </Card>
      <Card style={{ marginTop: "1rem" }}>
        <CardContent>
          <CardHeader title="Winesellers you might like" />
          <div style={{ height: "30vh", width: "100%" }}>
            <GoogleMapReact
              bootstrapURLKeys={{
                key: "",
              }}
              defaultCenter={defaultProps.center}
              defaultZoom={defaultProps.zoom}
            >
              {props.recoData.sellers.map((elem) =>
                createMarker(elem.rank, elem.lat, elem.lon, elem.name, "html")
              )}
            </GoogleMapReact>
          </div>
        </CardContent>
      </Card>
    </>
  );
};
