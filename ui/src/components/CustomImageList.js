import React from "react";
import {
  ImageList,
  Card,
  CardActionArea,
  ImageListItem,
  ImageListItemBar,
} from "@mui/material";

export const CustomImageList = (props) => {
  return (
    <ImageList cols={props.cols}>
      {props.data.map((dataPoint) => (
        <Card key={dataPoint[props.id]} variant="outlined">
          <CardActionArea onClick={() => props.onClick(dataPoint)}>
            <ImageListItem key={dataPoint[props.id]}>
              <img
                style={{
                  flex: 1,
                  width: 100,
                  height: 100,
                  alignSelf: "center",
                  resizeMode: "contain",
                }}
                src={dataPoint["picture_url"] + "?w=161&fit=crop&auto=format"}
              />
              <ImageListItemBar title={dataPoint[props.label]} />
            </ImageListItem>
          </CardActionArea>
        </Card>
      ))}
    </ImageList>
  );
};
