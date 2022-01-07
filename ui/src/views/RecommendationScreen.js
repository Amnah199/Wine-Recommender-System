import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../components/CustomModal";
import { ProfileCreationModal } from "./ProfileCreationModal";
import { recos } from "../tempfile";
import { Recommendations } from "./Recommendations";
import { LoadingOverlay } from "../components/LoadingOverlay";

export const RecommendationScreen = () => {
  const [profile, setProfile] = useState(false);
  const [recoData, setRecoData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (profile) {
      setLoading(true);
      setTimeout(() => {
        setRecoData(recos);
        setLoading(false);
      }, 1000);
    }
  }, [profile]);

  return (
    <>
      {!profile ? (
        <ProfileCreationModal onClose={(profile) => setProfile(profile)} />
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
