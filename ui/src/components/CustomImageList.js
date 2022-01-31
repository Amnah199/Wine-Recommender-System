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
import { Add, WineBar } from "@mui/icons-material";
import { theme } from "../theming";
export const CustomImageList = (props) => {
  let [backupVisible, setBackupVisible] = useState(false);
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
              {!backupVisible ? (
                <img
                  style={{
                    width: "10rem",

                    alignSelf: "center",
                    resizeMode: "contain",
                  }}
                  onError={() => setBackupVisible(true)}
                  src={
                    "http:" + dataPoint["url"] + "?w=161&fit=crop&auto=format"
                  }
                />
              ) : (
                <WineBar
                  height={200}
                  width={100}
                  style={{
                    flex: 1,
                    width: 100,
                    height: 100,
                    alignSelf: "center",
                    resizeMode: "contain",
                  }}
                />
              )}
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
