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
import { RecommendationPage } from "./views/RecommendationPage";
import SwaggerClient from "swagger-client";
import { Routes, Route } from "react-router-dom";
import { WineDetailPage } from "./views/WineDetailPage";
import { swagger_url } from "./constants";
import { useNavigate } from "react-router-dom";

export const SwaggerContext = React.createContext(null);

const CustomAppBar = (props) => {
  const navigate = useNavigate();
  return (
    <AppBar>
      <Toolbar variant="regular">
        <MenuItem onClick={() => navigate("/")}>
          <WineBarIcon sx={{ fontSize: 40 }} />
          <Typography variant="h3" noWrap>
            Wines.MS
          </Typography>
        </MenuItem>
      </Toolbar>
    </AppBar>
  );
};

export const App = (props) => {
  const [swaggerClient, setSwaggerClient] = useState(null);
  useEffect(
    () =>
      new SwaggerClient(swagger_url).then((client) => {
        setSwaggerClient(client.apis);
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
            <Routes>
              <Route path="/" element={<RecommendationPage />} />
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
