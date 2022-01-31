import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../components/CustomModal";
import { ProfileCreationModal } from "./ProfileCreationModal";
import { Recommendations } from "./Recommendations";
import { LoadingOverlay } from "../components/LoadingOverlay";
import { useContext } from "react";
import { SwaggerContext } from "../App";
import { useLocation } from "react-router-dom";
import { useCookies } from "react-cookie";
export const RecommendationPage = (props) => {
  const [profile, setProfile] = useState(false);
  const [recoData, setRecoData] = useState(null);
  const [loading, setLoading] = useState(false);

  const [cookies, setCookie, removeCookie] = useCookies(["cookie-name"]);

  const swagger = useContext(SwaggerContext);
  useEffect(
    () => (cookies.profile ? setProfile(cookies.wineMsProfile) : null),
    []
  );
  useEffect(() => {
    if (profile) {
      setLoading(true);

      swagger.recommendations.recommendations_list().then((resp) => {
        console.log(resp.body);
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
            setCookie("wineMsProfile", profile);
            setProfile(profile);
          }}
        />
      ) : (
        <></>
      )}
      {recoData ? (
        <Recommendations recoData={recoData} profile={profile} />
      ) : (
        <></>
      )}
      {loading ? <LoadingOverlay /> : <></>}
    </>
  );
};
