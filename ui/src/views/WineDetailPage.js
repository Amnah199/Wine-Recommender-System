import {
  CardContent,
  Card,
  Typography,
  Link,
  CardActionArea,
  CardActions,
  Button,
} from "@mui/material";
import React, { useEffect, useState, useContext } from "react";
import {
  useLocation,
  useNavigate,
  useParams,
  useRoutes,
} from "react-router-dom";
import { LoadingOverlay } from "../components/LoadingOverlay";
import { ImageListItem, ImageListItemBar } from "@mui/material";
import { Grid } from "@mui/material";
import { CardHeader } from "@mui/material";
import Color from "color";
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
import { SwaggerContext, CustomAppBar } from "../App";
import { useCookies } from "react-cookie";
import { useTheme } from "@emotion/react";
import { ShoppingBasket } from "@mui/icons-material";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);
export const WineDetailPage = (props) => {
  const [cookies, setCookie, removeCookie] = useCookies();

  const theme = useTheme();
  const params = useParams();

  const swagger = useContext(SwaggerContext);
  const [data, setData] = useState(null);

  useEffect(() => {
    swagger.details.details_read({ id: params.id }).then((resp) => {
      setData(resp.body);
    });
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
        label: data.name,
        data: datapoints,
        backgroundColor: Color(theme.palette.primary.main).alpha(0.2).string(),
        borderColor: Color(theme.palette.primary.main).string(),
        borderWidth: 1,
      },
    ],
  };
  if (cookies.wineMsProfile) {
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
  console.log(data);
  return (
    <>
      <Card elevation={5} style={{ marginTop: "1rem" }}>
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
                  <Card>
                    <CardHeader title="Where to buy?" />
                    <CardContent>
                      <Grid container>
                        {data.availability.map((elem) => (
                          <Grid container item justifyContent={"space-between"}>
                            <Grid item>
                              <Typography variant="body1">
                                {elem.label}
                              </Typography>
                            </Grid>
                            <Grid item>
                              <Typography variant="body1">
                                <Link href={elem.link}>{elem.value}</Link>
                              </Typography>
                            </Grid>
                          </Grid>
                        ))}
                        <Grid item style={{ marginLeft: "auto" }}>
                          <Button
                            style={{ marginTop: "1rem" }}
                            variant="contained"
                            endIcon={<ShoppingBasket />}
                            href={data.availability[0].link}
                          >
                            open at {data.availability[0].label}
                          </Button>
                        </Grid>
                      </Grid>
                    </CardContent>
                  </Card>
                  <Card style={{ marginTop: "1rem" }}>
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
    </>
  );
};
