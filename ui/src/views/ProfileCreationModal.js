import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../components/CustomModal";
import { WineSelection } from "../components/profileCreationScreens/WineSelection";
import { TasteCustomization } from "../components/profileCreationScreens/TasteCustomization";
import { ProfileCustomization } from "../components/profileCreationScreens/ProfileCustomization";

export const ProfileCreationModal = (props) => {
  const [step, setStep] = useState(0);
  const [title, setTitle] = useState("");

  useEffect(() => {
    if (step == 0) {
      setTitle("Wine Selection");
    } else if (step == 1 || step == 2) {
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
    } else if (step == 1) {
      setStep(2);
    } else if (step == 2) {
      props.onClose();
    }
  };

  return (
    <CustomModal
      title={title}
      onClose={() => props.onClose()}
      onNext={onNext}
      onPrevious={onPrevious}
      nextDisabled={false}
      previousDisabled={step <= 0}
    >
      {step == 0 ? <WineSelection /> : <></>}
      {step == 1 ? <ProfileCustomization /> : <></>}
      {step == 2 ? <TasteCustomization /> : <></>}
    </CustomModal>
  );
};
