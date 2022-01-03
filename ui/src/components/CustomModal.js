import React from "react";
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Modal,
  Paper,
} from "@mui/material";
import { Box } from "@mui/system";
import { Container } from "@mui/material";
import { Button } from "@mui/material";

export const CustomModal = (props) => (
  <Dialog open={true} onClose={() => props.onClose()}>
    <DialogTitle>props.title</DialogTitle>
    <DialogContent>{props.children}</DialogContent>
    <DialogActions>
      <Button
        disabled={props.previousDisabled}
        onClick={() => {
          props.onPrevious();
        }}
      >
        Previous
      </Button>
      <Button disabled={props.nextDisabled} onClick={() => props.onNext()}>
        Next
      </Button>
    </DialogActions>
  </Dialog>
);