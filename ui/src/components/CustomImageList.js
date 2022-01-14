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
import { theme } from "../theming";
export const CustomImageList = (props) => {
  return (
    <ImageList cols={props.cols}>
      {props.data.map((dataPoint) => (
        <Card
          style={{ margin: "0.5rem" }}
          key={dataPoint[props.id]}
          elevation={3}
        >
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
                      size="small"
                      variant="contained"
                      style={{
                        color: "white",
                        backgroundColor: "#540804cc",
                        margin: "0.25rem",
                      }}
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
