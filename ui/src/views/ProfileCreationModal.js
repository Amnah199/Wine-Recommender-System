import React, { useEffect, useState } from "react";
import { CircularProgress, Typography } from "@mui/material";
import { CustomModal } from "../components/CustomModal";
import { WineSelection } from "../components/profileCreationScreens/WineSelection";
import { TasteCustomization } from "../components/profileCreationScreens/TasteCustomization";
import { ProfileCustomization } from "../components/profileCreationScreens/ProfileCustomization";
import { Modal } from "@mui/material";
import { LoadingOverlay } from "../components/LoadingOverlay";
import { temp_profile } from "../tempfile";
export const ProfileCreationModal = (props) => {
  const [step, setStep] = useState(0);
  const [title, setTitle] = useState("");
  const [selectedWines, setSelectedWines] = useState([]);
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (step == 0) {
      setTitle("Wine Selection");
    } else if (step == 1 || step == 2) {
      setTitle("Wine Profile");
    } else if (step == 2) {
      setTitle("Taste Profile");
    }
  }, [step]);

  const onPrevious = () => {
    if (step == 1) {
      setStep(0);
    } else if (step == 2) {
      setStep(1);
    }
  };
  const onNext = () => {
    if (step == 0) {
      setStep(1);
      setLoading(true);

      //change me
      setTimeout(() => {
        setProfile(temp_profile);
        setLoading(false);
      }, 100);
    } else if (step == 1) {
      setStep(2);
    } else if (step == 2) {
      props.onClose(profile);
    }
  };
  if (loading) {
    return <LoadingOverlay />;
  }

  return (
    <CustomModal
      title={title}
      onNext={onNext}
      onPrevious={onPrevious}
      nextDisabled={false}
      previousDisabled={step <= 0}
    >
      {step == 0 ? (
        <WineSelection
          selectedWines={selectedWines}
          setSelectedWines={setSelectedWines}
        />
      ) : (
        <></>
      )}

      {step == 1 ? (
        <ProfileCustomization
          profile={profile}
          onProfileChange={(changedProfile) => {
            setProfile({ ...changedProfile });
          }}
        />
      ) : (
        <></>
      )}
      {step == 2 ? <TasteCustomization profile={profile} /> : <></>}
    </CustomModal>
  );
};
