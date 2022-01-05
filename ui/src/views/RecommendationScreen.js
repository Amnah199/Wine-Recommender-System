import React, { useState } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../components/CustomModal";
import { ProfileCreationModal } from "./ProfileCreationModal";

export const RecommendationScreen = () => {
  const [profileSelectionOpen, setProfileSelectionOpen] = useState(true);
  const [recoData, setRecoData] = useState(null);

  return (
    <>
      {profileSelectionOpen ? (
        <ProfileCreationModal onClose={() => setProfileSelectionOpen(false)} />
      ) : (
        <></>
      )}
      {recoData ? (
        <Typography variant="h4" textAlign={"center"}>
          profile ready
        </Typography>
      ) : (
        <Typography variant="h4" textAlign={"center"}>
          Find Wines from Münster!
        </Typography>
      )}
    </>
  );
};
