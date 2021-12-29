import React from "react";
import AppBar from "@mui/material/AppBar";
import { Container, Typography } from "@mui/material";
import { Toolbar } from "@mui/material";
import WineBarIcon from "@mui/icons-material/WineBar";
import { Paper } from "@mui/material";
import { TrainRounded } from "@mui/icons-material";

const CustomAppBar = () => (
  <AppBar>
    <Toolbar variant="regular">
      <WineBarIcon sx={{ fontSize: 40 }} />
      <Typography variant="h3" noWrap>
        Wines.MS
      </Typography>
    </Toolbar>
  </AppBar>
);

export const App = () => {
  let isProfileReady = true;

  return (
    <div>
      <CustomAppBar />
      <Toolbar />
      <Container maxWidth="lg">
        {isProfileReady ? (
          <Typography variant="h3" textAlign={"center"}>
            Find Wines from Münster!
          </Typography>
        ) : (
          <Typography variant="h3" textAlign={"center"}>
            profile ready
          </Typography>
        )}
      </Container>
    </div>
  );
};
