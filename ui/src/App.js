import React, { createContext, useEffect, useState } from "react";
import AppBar from "@mui/material/AppBar";
import { CircularProgress, Container, Typography } from "@mui/material";
import { Toolbar } from "@mui/material";
import WineBarIcon from "@mui/icons-material/WineBar";
import { Paper } from "@mui/material";
import { TrainRounded } from "@mui/icons-material";
import { RecommendationScreen } from "./views/RecommendationScreen";
import SwaggerClient from "swagger-client";

export const SwaggerContext = React.createContext(null);

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
  const [swaggerClient, setSwaggerClient] = useState(null);
  useEffect(
    () =>
      new SwaggerClient("/swagger.json").then((client) => {
        setSwaggerClient(client.apis.WineAPI);
      }),
    []
  );

  return (
    <div>
      <CustomAppBar />
      <Toolbar />
      <Container maxWidth="lg">
        {swaggerClient ? (
          <SwaggerContext.Provider value={swaggerClient}>
            <RecommendationScreen />
          </SwaggerContext.Provider>
        ) : (
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignContent: "center",
            }}
          >
            <CircularProgress />
          </div>
        )}
      </Container>
    </div>
  );
};
