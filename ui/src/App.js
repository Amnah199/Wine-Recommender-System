import React, { createContext, useEffect, useState } from "react";
import AppBar from "@mui/material/AppBar";
import {
  CircularProgress,
  Container,
  MenuItem,
  Typography,
} from "@mui/material";
import { Toolbar } from "@mui/material";
import WineBarIcon from "@mui/icons-material/WineBar";
import { Paper } from "@mui/material";
import { TrainRounded } from "@mui/icons-material";
import { RecommendationScreen } from "./views/RecommendationScreen";
import SwaggerClient from "swagger-client";
import { Routes, Route } from "react-router-dom";
import { WineDetailPage } from "./views/WineDetailPage";

export const SwaggerContext = React.createContext(null);

const CustomAppBar = () => (
  <AppBar>
    <Toolbar variant="regular">
      <MenuItem onClick={() => window.open("/", "_self")}>
        <WineBarIcon sx={{ fontSize: 40 }} />
        <Typography variant="h3" noWrap>
          Wines.MS
        </Typography>
      </MenuItem>
    </Toolbar>
  </AppBar>
);

export const App = () => {
  const [swaggerClient, setSwaggerClient] = useState(null);
  useEffect(
    () =>
      new SwaggerClient("http://localhost:8000/WineAPI/swaggerconfig").then(
        (client) => {
          setSwaggerClient(client.apis.WineAPI);
        }
      ),
    []
  );

  return (
    <div>
      <CustomAppBar />
      <Toolbar />
      <Container maxWidth="lg">
        {swaggerClient ? (
          <SwaggerContext.Provider value={swaggerClient}>
            <Routes>
              <Route path="/" element={<RecommendationScreen />} />
              <Route path="/wine/:id" element={<WineDetailPage />} />
            </Routes>
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
