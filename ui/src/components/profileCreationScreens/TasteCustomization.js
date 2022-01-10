import React, { useState } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../CustomModal";
import { Radar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

export const TasteCustomization = (props) => {
  let labels = props.profile.taste_data.map((elem) => elem.label);
  let datapoints = props.profile.taste_data.map((elem) => elem.percentage);

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Your Taste",
        data: datapoints,
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
      },
    ],
  };
  return (
    <div
      style={{
        maxWidth: "600px",
        alignContent: "center",
        marginInline: "auto",
      }}
    >
      <Radar data={data} />
    </div>
  );
};
