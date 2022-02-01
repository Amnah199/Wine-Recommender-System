import React from "react";
import {
  Table,
  TableRow,
  Card,
  CardHeader,
  CardContent,
  CardActionArea,
  CardActions,
  IconButton,
  TableHead,
  TableBody,
  TableCell,
} from "@mui/material";
import { Radar } from "react-chartjs-2";
import { useCookies } from "react-cookie";
import Color from "color";
import { useTheme } from "@emotion/react";
import { useState } from "react";
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";
import { ChangeCircle } from "@mui/icons-material";
import { cookie_name } from "../constants";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

export const TasteDataWidget = (props) => {
  const [cookies, setCookie, removeCookie] = useCookies();
  const theme = useTheme();

  let [radarVisible, setRadarVisible] = useState(true);

  let labels = props.data.taste_data.map((elem) => elem.label);
  let datapoints = props.data.taste_data.map((elem) => elem.percentage);

  const chartData = {
    labels: labels,
    datasets: [
      {
        label: props.data.name,
        data: datapoints,
        backgroundColor: Color(theme.palette.primary.main).alpha(0.2).string(),
        borderColor: Color(theme.palette.primary.main).string(),
        borderWidth: 1,
      },
    ],
  };
  if (cookies.wineMsProfile) {
    console.log(cookies.wineMsProfile);
    let profile_points = cookies.wineMsProfile.taste_data.map(
      (elem) => elem.percentage
    );
    chartData.datasets.push({
      label: "Your Taste",
      data: profile_points,
      backgroundColor: Color(theme.palette.secondary.main).alpha(0.2).string(),
      borderColor: Color(theme.palette.secondary.main).string(),
      borderWidth: 1,
    });
  }
  return (
    <Card>
      <CardHeader
        title="Tasteprofile"
        action={
          <IconButton
            color="primary"
            onClick={() => setRadarVisible(!radarVisible)}
          >
            <ChangeCircle />
          </IconButton>
        }
      />
      <CardContent>
        {radarVisible ? (
          <Radar data={chartData} />
        ) : (
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>property</TableCell>
                <TableCell>Wine Value</TableCell>
                <TableCell>Your Value</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {props.data.structure_data.map((elem) => (
                <TableRow>
                  <TableCell>{elem.label}</TableCell>
                  <TableCell>
                    {Math.round(elem.percentage * 100) / 100}
                  </TableCell>
                  {cookies[cookie_name].structure_data[elem.label] ? (
                    <TableCell>
                      {Math.round(
                        cookies[cookie_name].structure_data[elem.label] * 100
                      ) / 100}
                    </TableCell>
                  ) : (
                    <TableCell>0</TableCell>
                  )}
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
};
