import React, { useState } from "react";
import {
  Button,
  Dialog,
  DialogContent,
  Divider,
  inputAdornmentClasses,
  Typography,
} from "@mui/material";
import { CustomModal } from "../CustomModal";
import { TextField } from "@mui/material";
import { SearchResultModal } from "./SearchResultsModal";
import { CustomImageList } from "../CustomImageList";
import { ContentCutOutlined } from "@mui/icons-material";

export const WineSelection = () => {
  const [searchString, setSearchString] = useState("");
  const [dialogOpen, setDialogOpen] = useState(false);
  const [selectedWines, setSelectedWines] = useState([]);
  return (
    <>
      <TextField
        style={{ marginTop: "1rem" }}
        label="Search field"
        type="search"
        label="Wine Search"
        placeholder="search for a wine you like"
        fullWidth
        onKeyDown={(event) =>
          event.keyCode == 13 && searchString.length > 3
            ? setDialogOpen(true)
            : null
        }
        onChange={(event) => setSearchString(event.target.value)}
      />
      {dialogOpen ? (
        <SearchResultModal
          searchString={searchString}
          onClose={(elem) => {
            setDialogOpen(false);
            if (elem && !selectedWines.includes(elem)) {
              let newSelectedWines = [...selectedWines];
              newSelectedWines.push(elem);

              setSelectedWines(newSelectedWines);
            }
          }}
        />
      ) : (
        <></>
      )}

      <Typography variant="h6">
        Selected Wines: {selectedWines.length}
      </Typography>
      <CustomImageList
        data={selectedWines}
        id={"id"}
        pictureUrl={"picture_url"}
        label={"name"}
        onClick={(elem) => {
          let newSelectedWines = [
            ...selectedWines.filter((value) => value != elem),
          ];
          setSelectedWines(newSelectedWines);
        }}
      />
    </>
  );
};
