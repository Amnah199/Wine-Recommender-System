import React, { useState } from "react";
import {
  ImageList,
  Card,
  CardActionArea,
  ImageListItem,
  ImageListItemBar,
  CardMedia,
  Popover,
  Button,
  IconButton,
} from "@mui/material";
import { Add } from "@mui/icons-material";
export const CustomImageList = (props) => {
  return (
    <ImageList cols={props.cols}>
      {props.data.map((dataPoint) => (
        <Card key={dataPoint[props.id]} variant="outlined">
          <CardActionArea onClick={() => props.onClick(dataPoint)}>
            <ImageListItem key={dataPoint[props.id]} style={{ opacity: 2 }}>
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
              <ImageListItemBar
                subtitle={dataPoint[props.label]}
                actionIcon={
                  props.button ? (
                    <IconButton
                      variant="contained"
                      style={{ color: "white", backgroundColor: "black" }}
                    >
                      {props.button}
                    </IconButton>
                  ) : (
                    <></>
                  )
                }
              />
            </ImageListItem>
          </CardActionArea>
        </Card>
      ))}
    </ImageList>
  );
};
