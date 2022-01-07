import React from "react";
import { Modal, CircularProgress } from "@mui/material";
export const LoadingOverlay = () => (
  <Modal
    open={true}
    style={{
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }}
  >
    <CircularProgress />
  </Modal>
);
