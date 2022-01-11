import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../components/CustomModal";
import { ProfileCreationModal } from "./ProfileCreationModal";
import { recos } from "../tempfile";
import { Recommendations } from "./Recommendations";
import { LoadingOverlay } from "../components/LoadingOverlay";
import { useContext } from "react";
import { SwaggerContext } from "../App";

export const RecommendationPage = (props) => {
  const [profile, setProfile] = useState(false);
  const [recoData, setRecoData] = useState(null);
  const [loading, setLoading] = useState(false);

  const swagger = useContext(SwaggerContext);

  useEffect(() => {
    if (profile) {
      setLoading(true);

      swagger.recommendations.recommendations_list().then((resp) => {
        setRecoData(resp.body);
        setLoading(false);
      });
    }
  }, [profile]);

  return (
    <>
      {!profile ? (
        <ProfileCreationModal
          onClose={(profile) => {
            setProfile(profile);
          }}
        />
      ) : (
        <></>
      )}
      {recoData ? (
        <Recommendations recoData={recoData} />
      ) : (
        <Typography variant="h4" textAlign={"center"}>
          Find Wines from Münster!
        </Typography>
      )}
      {loading ? <LoadingOverlay /> : <></>}
    </>
  );
};
