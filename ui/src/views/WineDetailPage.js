import { CardContent, Card, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { LoadingOverlay } from "../components/LoadingOverlay";
import { wineData } from "../tempfile";
import { ImageListItem, ImageListItemBar } from "@mui/material";
import { Grid } from "@mui/material";
import { CardHeader } from "@mui/material";
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
export const WineDetailPage = (props) => {
  const params = useParams();
  const [data, setData] = useState(null);
  useEffect(() => {
    console.log(params.id);
    setTimeout(() => setData(wineData), 100);
  }, []);

  if (!data) {
    return <LoadingOverlay />;
  }

  let labels = data.taste_data.map((elem) => elem.label);
  let datapoints = data.taste_data.map((elem) => elem.percentage);

  const chartData = {
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
    <Card>
      <CardContent>
        <Grid container spacing={1}>
          <Grid item xs={12} sm={3}>
            <ImageListItem>
              <img
                style={{
                  flex: 1,
                  alignSelf: "center",
                  resizeMode: "contain",
                }}
                src={data.picture_url + "?w=161&fit=crop&auto=format"}
              />
              <ImageListItemBar title={data.name} />
            </ImageListItem>
          </Grid>
          <Grid item sm={9}>
            <Card>
              <CardHeader title="Description" />
              <CardContent>{data.description}</CardContent>
            </Card>
            <Grid item container spacing={1} style={{ marginTop: "0.25rem" }}>
              <Grid item md={6} xs={12}>
                <Card style={{ height: "100%" }}>
                  <CardHeader title="Facts" />
                  <CardContent>
                    <Grid container>
                      {data.facts.map((elem) => (
                        <Grid container item justifyContent={"space-between"}>
                          <Grid item>
                            <Typography variant="body1">
                              {elem.label}
                            </Typography>
                          </Grid>
                          <Grid item>
                            <Typography variant="body1">
                              {elem.content}
                            </Typography>
                          </Grid>
                        </Grid>
                      ))}
                    </Grid>
                  </CardContent>
                </Card>
              </Grid>
              <Grid item md={6} xs={12}>
                <Card>
                  <CardHeader title="Tasteprofile" />
                  <CardContent>
                    <Radar data={chartData} />
                  </CardContent>
                </Card>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};
