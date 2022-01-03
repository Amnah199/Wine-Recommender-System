import React from "react";
import AppBar from "@mui/material/AppBar";
import { Container, Typography } from "@mui/material";
import { Toolbar } from "@mui/material";
import WineBarIcon from "@mui/icons-material/WineBar";
import { Paper } from "@mui/material";
import { TrainRounded } from "@mui/icons-material";
import { RecommendationScreen } from "./views/RecommendationScreen";

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
        <RecommendationScreen />
      </Container>
    </div>
  );
};
